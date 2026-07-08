from pathlib import Path

import irsim
import numpy as np


def main():
    world_file = Path(__file__).with_name("basic_world.yaml")

    print("=== IR-SIM Basic World Demo ===")
    print("World file:", world_file)

    env = irsim.make(str(world_file), display=False, save_ani=False, log_level="WARNING")

    print("Environment created.")
    print("Robot number:", env.robot_number)

    print("Initial robot state:")
    print(env.get_robot_state())

    for step in range(50):
        # diff robot action: [[linear_velocity], [angular_velocity]]
        action = np.array([[0.5], [0.1]])

        env.step(action)

        if step % 10 == 0:
            print(f"step={step}")
            print(env.get_robot_state())

        if env.done():
            print(f"Environment done at step {step}")
            break

    print("Final robot state:")
    print(env.get_robot_state())

    print("Basic world demo finished.")


if __name__ == "__main__":
    main()
