"""Seed the existing evaluator without changing its implementation."""
import argparse
from pathlib import Path
import random
import runpy
import sys

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__, add_help=False)
    parser.add_argument('--seed', type=int, default=42)
    args, forwarded = parser.parse_known_args()
    if '--episodes' in forwarded and int(forwarded[forwarded.index('--episodes') + 1]) < 1:
        parser.error('--episodes must be positive')
    if '--max-steps' in forwarded and int(forwarded[forwarded.index('--max-steps') + 1]) < 1:
        parser.error('--max-steps must be positive')
    random.seed(args.seed)
    np.random.seed(args.seed)
    script = Path(__file__).resolve().parents[1] / 'src/irsim_env/evaluate_random_policy.py'
    sys.argv = [str(script), *forwarded]
    runpy.run_path(str(script), run_name='__main__')


if __name__ == '__main__':
    main()
