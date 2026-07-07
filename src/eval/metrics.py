from typing import Dict, List


def compute_eval_metrics(episodes: List[Dict]) -> Dict[str, float]:
    """
    Compute evaluation metrics for robot navigation episodes.

    Each episode should contain:
    - success: bool
    - collision: bool
    - timeout: bool
    - steps: int
    - path_length: float
    """

    if not episodes:
        raise ValueError("No episodes provided for evaluation.")

    total = len(episodes)

    success_count = sum(1 for ep in episodes if ep.get("success", False))
    collision_count = sum(1 for ep in episodes if ep.get("collision", False))
    timeout_count = sum(1 for ep in episodes if ep.get("timeout", False))

    avg_steps = sum(ep.get("steps", 0) for ep in episodes) / total
    avg_path_length = sum(ep.get("path_length", 0.0) for ep in episodes) / total

    return {
        "SR": success_count / total,
        "CR": collision_count / total,
        "TR": timeout_count / total,
        "avg_steps": avg_steps,
        "avg_path_length": avg_path_length,
        "num_episodes": total,
    }


def format_metrics(metrics: Dict[str, float]) -> str:
    """Format evaluation metrics into a readable string."""

    return (
        f"SR={metrics['SR']:.2%}, "
        f"CR={metrics['CR']:.2%}, "
        f"TR={metrics['TR']:.2%}, "
        f"AvgSteps={metrics['avg_steps']:.2f}, "
        f"AvgPathLength={metrics['avg_path_length']:.2f}, "
        f"N={int(metrics['num_episodes'])}"
    )


if __name__ == "__main__":
    sample_episodes = [
        {
            "success": True,
            "collision": False,
            "timeout": False,
            "steps": 120,
            "path_length": 5.4,
        },
        {
            "success": False,
            "collision": True,
            "timeout": False,
            "steps": 80,
            "path_length": 3.1,
        },
        {
            "success": False,
            "collision": False,
            "timeout": True,
            "steps": 300,
            "path_length": 7.8,
        },
    ]

    results = compute_eval_metrics(sample_episodes)
    print(format_metrics(results))
