import argparse
import csv
from pathlib import Path

from metrics import compute_eval_metrics, format_metrics


def load_episodes_from_csv(csv_path: Path):
    episodes = []

    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            episodes.append(
                {
                    "scenario": row["scenario"],
                    "success": row["success"].lower() == "true",
                    "collision": row["collision"].lower() == "true",
                    "timeout": row["timeout"].lower() == "true",
                    "steps": int(row["steps"]),
                    "path_length": float(row["path_length"]),
                }
            )

    return episodes


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate robot navigation results from a CSV file."
    )
    parser.add_argument(
        "--file",
        type=str,
        default="results/sample_eval_results.csv",
        help="Path to evaluation CSV file.",
    )

    args = parser.parse_args()
    csv_path = Path(args.file)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    episodes = load_episodes_from_csv(csv_path)
    metrics = compute_eval_metrics(episodes)

    print(f"Loaded {len(episodes)} episodes from {csv_path}")
    print(format_metrics(metrics))


if __name__ == "__main__":
    main()
