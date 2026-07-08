from pathlib import Path
import csv
import random
import math

import irsim
import numpy as np


def get_xy(state):
    return float(state[0][0]), float(state[1][0])


def distance_to_goal(state, goal_x=9.0, goal_y=9.0):
    x, y = get_xy(state)
    return math.sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2)


def run_episode(episode_id, max_steps=200):
    world_file = Path(__file__).with_name("basic_world.yaml")
    env = irsim.make(str(world_file), display=False, save_ani=False, log_level="WARNING")

    start_state = env.get_robot_state()
    start_x, start_y = get_xy(start_state)

    success = False
    collision = False
    timeout = False
    path_length = 0.0

    prev_x, prev_y = start_x, start_y

    for step in range(max_steps):
        linear_v = random.uniform(0.0, 1.0)
        angular_v = random.uniform(-1.0, 1.0)
        action = np.array([[linear_v], [angular_v]])

        env.step(action)

        state = env.get_robot_state()
        x, y = get_xy(state)

        path_length += math.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
        prev_x, prev_y = x, y

        if distance_to_goal(state) < 0.3:
            success = True
            break

        if env.done():
            # For this first demo, env.done() means the simulation stopped.
            # Later we will separate collision / arrival more carefully.
            break

    else:
        timeout = True
        step = max_steps

    if not success and not timeout:
        collision = True

    return {
        "scenario": "basic_world",
        "episode_id": episode_id,
        "success": success,
        "collision": collision,
        "timeout": timeout,
        "steps": step + 1,
        "path_length": round(path_length, 4),
    }


def main():
    output_file = Path("results/basic_world_random_eval.csv")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    episodes = []
    for episode_id in range(10):
        result = run_episode(episode_id)
        episodes.append(result)
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
        writer.writerows(episodes)

    print(f"\nSaved results to {output_file}")


if __name__ == "__main__":
    main()
