"""Regression checks for preserved evaluation behavior."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src/eval'))
from metrics import compute_eval_metrics
from evaluate_csv import load_episodes_from_csv


class EvaluationTests(unittest.TestCase):
    def test_archived_results(self):
        for name, expected in [('u_trap', (0, 1, 0, 44.4)),
                               ('basic_world', (0, .1, .9, 191.6))]:
            result = compute_eval_metrics(load_episodes_from_csv(ROOT / f'results/{name}_random_eval.csv'))
            for key, value in zip(('SR', 'CR', 'TR', 'avg_steps'), expected):
                self.assertAlmostEqual(result[key], value)
            self.assertEqual(result['num_episodes'], 10)

    def test_sample_is_separate(self):
        result = compute_eval_metrics(load_episodes_from_csv(ROOT / 'results/sample_eval_results.csv'))
        self.assertEqual(result['num_episodes'], 5)
        self.assertEqual(result['SR'], .4)

    def test_empty_input_rejected(self):
        with self.assertRaisesRegex(ValueError, 'No episodes'):
            compute_eval_metrics([])

    def test_missing_file_cli(self):
        result = subprocess.run([sys.executable, str(ROOT / 'src/eval/evaluate_csv.py'),
                                 '--file', str(ROOT / '__missing__.csv')], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('CSV file not found', result.stderr)

    def test_malformed_csv(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'bad.csv'
            path.write_text('scenario,success,collision,timeout,steps,path_length\nx,true,false,false,bad,1\n')
            with self.assertRaises(ValueError):
                load_episodes_from_csv(path)


if __name__ == '__main__':
    unittest.main()
