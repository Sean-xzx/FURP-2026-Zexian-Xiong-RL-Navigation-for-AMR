from pathlib import Path
import argparse
import csv
import math
import random

import irsim
import numpy as np


def get_xy(state):
    return float(state[0][0]), float(state[1][0])


def distance_to_goal(state, goal_x, goal_y):
    x, y = get_xy(state)
    return math.sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2)


def run_episode(world_file, scenario, episode_id, goal_x, goal_y, max_steps):
    env = irsim.make(str(world_file), display=False, save_ani=False, log_level="WARNING")

    start_state = env.get_robot_state()
    prev_x, prev_y = get_xy(start_state)

    success = False
    collision = False
    timeout = False
    path_length = 0.0

    step = 0

    for step in range(max_steps):
        linear_v = random.uniform(0.0, 1.0)
        angular_v = random.uniform(-1.0, 1.0)
        action = np.array([[linear_v], [angular_v]])

        env.step(action)

        state = env.get_robot_state()
        x, y = get_xy(state)

        path_length += math.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
        prev_x, prev_y = x, y

        if distance_to_goal(state, goal_x, goal_y) < 0.35:
            success = True
            break

        if env.done():
            collision = True
            break
    else:
        timeout = True
        step = max_steps - 1

    return {
        "scenario": scenario,
        "episode_id": episode_id,
        "success": success,
        "collision": collision,
        "timeout": timeout,
        "steps": step + 1,
        "path_length": round(path_length, 4),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", required=True, help="Path to IR-SIM world YAML file")
    parser.add_argument("--scenario", required=True, help="Scenario name")
    parser.add_argument("--goal-x", type=float, required=True)
    parser.add_argument("--goal-y", type=float, required=True)
    parser.add_argument("--episodes", type=int, default=10)
    parser.add_argument("--max-steps", type=int, default=300)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    world_file = Path(args.world)
    output_file = Path(args.output)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    results = []

    for episode_id in range(args.episodes):
        result = run_episode(
            world_file=world_file,
            scenario=args.scenario,
            episode_id=episode_id,
            goal_x=args.goal_x,
            goal_y=args.goal_y,
            max_steps=args.max_steps,
        )
        results.append(result)
        print(result)

    with output_file.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scenario",
                "episode_id",
                "success",
                "collision",
                "timeout",
                "steps",
                "path_length",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSaved results to {output_file}")


if __name__ == "__main__":
    main()
