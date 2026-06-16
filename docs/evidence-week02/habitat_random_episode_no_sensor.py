import random
from pathlib import Path

import numpy as np
import habitat_sim


def find_scene():
    candidates = list(Path("data").rglob("*.glb"))

    if not candidates:
        raise FileNotFoundError("No .glb scene file found under ./data")

    preferred = [p for p in candidates if "skokloster" in p.name.lower()]
    scene = preferred[0] if preferred else candidates[0]

    return str(scene)


def make_cfg(scene_path):
    sim_cfg = habitat_sim.SimulatorConfiguration()
    sim_cfg.scene_id = scene_path
    sim_cfg.enable_physics = False

    agent_cfg = habitat_sim.agent.AgentConfiguration()

    # Important:
    # No RGB / depth sensors here.
    # This avoids the rendering path as much as possible.
    agent_cfg.sensor_specifications = []

    agent_cfg.action_space = {
        "move_forward": habitat_sim.agent.ActionSpec(
            "move_forward",
            habitat_sim.agent.ActuationSpec(amount=0.25),
        ),
        "turn_left": habitat_sim.agent.ActionSpec(
            "turn_left",
            habitat_sim.agent.ActuationSpec(amount=10.0),
        ),
        "turn_right": habitat_sim.agent.ActionSpec(
            "turn_right",
            habitat_sim.agent.ActuationSpec(amount=10.0),
        ),
    }

    return habitat_sim.Configuration(sim_cfg, [agent_cfg])


def main():
    print("Step 1: locating Habitat test scene")
    scene_path = find_scene()
    print(f"Scene found: {scene_path}")

    print("Step 2: building Habitat-Sim config")
    cfg = make_cfg(scene_path)

    print("Step 3: starting Simulator()")
    sim = habitat_sim.Simulator(cfg)

    print("Step 4: initializing agent")
    agent = sim.initialize_agent(0)

    if sim.pathfinder.is_loaded:
        start_position = sim.pathfinder.get_random_navigable_point()
        state = agent.get_state()
        state.position = start_position
        agent.set_state(state)
        print(f"Random navigable start position: {np.round(start_position, 3)}")
    else:
        print("Warning: pathfinder/navmesh not loaded. Using default agent position.")

    print("Step 5: running one random navigation episode")

    actions = ["move_forward", "turn_left", "turn_right"]

    for step in range(10):
        action = random.choice(actions)
        sim.step(action)

        state = agent.get_state()
        position = np.round(state.position, 3)

        print(f"step={step + 1:02d}, action={action}, position={position}")

    sim.close()

    print("HABITAT SMOKE TEST PASSED: Simulator started and one no-sensor random navigation episode ran.")


if __name__ == "__main__":
    main()
