"""Run actual navigation examples, regression tests and local README link checks."""
import csv
import hashlib
import importlib.util
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artifacts'
os.environ['MPLBACKEND'] = 'Agg'
os.environ['PYTHONIOENCODING'] = 'utf-8'


def run(*args, cwd=ROOT):
    result = subprocess.run([sys.executable, *map(str, args)], cwd=cwd,
                            capture_output=True, text=True, encoding='utf-8')
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode:
        print(result.stderr)
        raise RuntimeError(f'Command failed: {args}')
    return result.stdout


def main():
    OUT.mkdir(exist_ok=True)
    run('-m', 'unittest', 'discover', '-s', 'tests', '-v')
    for name in ('README.md', 'README.zh-CN.md'):
        for target in re.findall(r'\]\(([^)]+)\)', (ROOT / name).read_text(encoding='utf-8')):
            if not target.startswith(('http:', 'https:', '#')):
                assert (ROOT / target.split('#')[0]).exists(), (name, target)
    for line in (ROOT / 'docs/assets/SHA256SUMS.txt').read_text().splitlines():
        digest, name = line.split('  ', 1)
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    grid_script = ROOT / 'docs/evidence-week01/gridworld_shortest_path_smoke.py'
    output = run(grid_script, cwd=OUT)
    for expected in ('Movement steps: 18', 'Episode return: 2', 'SMOKE TEST PASSED'):
        assert expected in output, expected
    assert (OUT / 'gridworld_trajectory.png').stat().st_size > 0
    spec = importlib.util.spec_from_file_location('gridworld', grid_script)
    grid = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(grid)
    path = grid.shortest_path(grid.START, grid.GOAL)
    assert len(path) == 19 and path[0] == grid.START and path[-1] == grid.GOAL
    assert all(grid.grid[p] == 0 for p in path)
    assert all(abs(a[0]-b[0])+abs(a[1]-b[1]) == 1 for a,b in zip(path,path[1:]))
    grid.grid[:] = 1
    grid.grid[grid.START] = grid.grid[grid.GOAL] = 0
    assert grid.shortest_path(grid.START, grid.GOAL) is None
    for world, gx, gy in [('basic_world', 9, 9), ('u_trap_world', 5, 9)]:
        files = [OUT / f'{world}_repeat{i}.csv' for i in range(2)]
        for dest in files:
            run(ROOT / 'tools/run_random_baseline.py', '--seed', 42,
                '--world', ROOT / f'src/irsim_env/worlds/{world}.yaml',
                '--scenario', world, '--goal-x', gx, '--goal-y', gy,
                '--episodes', 2, '--max-steps', 100, '--output', dest)
        assert files[0].read_bytes() == files[1].read_bytes(), 'Seeded repeats differ'
        with files[0].open() as file:
            rows = list(csv.DictReader(file))
        assert len(rows) == 2
        for row in rows:
            assert sum(row[k] == 'True' for k in ('success','collision','timeout')) == 1
            assert 1 <= int(row['steps']) <= 100 and float(row['path_length']) >= 0
        run(ROOT / 'src/eval/evaluate_csv.py', '--file', files[0])
    print('VERIFICATION PASSED: metrics, errors, links, hashes, GridWorld and seeded IR-SIM repeats')


if __name__ == '__main__':
    main()
