from collections import deque
import numpy as np
import matplotlib.pyplot as plt


GRID_SIZE = 10
START = (0, 0)
GOAL = (9, 9)

# 0 = free cell, 1 = obstacle
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

obstacles = [
    (1, 2), (2, 2), (3, 2), (4, 2),
    (4, 3), (4, 4), (4, 5),
    (6, 1), (6, 2), (6, 3),
    (7, 6), (8, 6), (9, 6),
    (2, 7), (3, 7), (4, 7), (5, 7),
]

for r, c in obstacles:
    grid[r, c] = 1

grid[START] = 0
grid[GOAL] = 0


def get_neighbors(position):
    r, c = position
    moves = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    neighbors = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
            if grid[nr, nc] == 0:
                neighbors.append((nr, nc))

    return neighbors


def shortest_path(start, goal):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

    if goal not in came_from:
        return None

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


def calculate_return(path):
    step_penalty = -1
    goal_reward = 20

    movement_steps = len(path) - 1
    episode_return = movement_steps * step_penalty + goal_reward

    return episode_return


def render_trajectory(path):
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, origin="upper")

    rows = [p[0] for p in path]
    cols = [p[1] for p in path]

    plt.plot(cols, rows, marker="o", linewidth=2, label="Trajectory")
    plt.scatter(START[1], START[0], marker="s", s=120, label="Start")
    plt.scatter(GOAL[1], GOAL[0], marker="*", s=180, label="Goal")

    plt.xticks(range(GRID_SIZE))
    plt.yticks(range(GRID_SIZE))
    plt.grid(True)
    plt.title("Shortest-Path Navigation Episode Smoke Test")
    plt.legend()

    output_file = "gridworld_trajectory.png"
    plt.savefig(output_file, dpi=200, bbox_inches="tight")
    plt.close()

    return output_file


def main():
    print("Step 1 OK: GridWorld environment created")
    print(f"Grid size: {GRID_SIZE} x {GRID_SIZE}")
    print(f"Start position: {START}")
    print(f"Goal position: {GOAL}")
    print(f"Number of obstacles: {len(obstacles)}")

    print("\nStep 2: Running one shortest-path navigation episode")
    path = shortest_path(START, GOAL)

    if path is None:
        print("SMOKE TEST FAILED: no valid path found")
        return

    episode_return = calculate_return(path)

    print("Step 3 OK: valid path found")
    print(f"Path length including start and goal: {len(path)}")
    print(f"Movement steps: {len(path) - 1}")
    print(f"Episode return: {episode_return}")

    print("\nTrajectory:")
    for i, position in enumerate(path):
        print(f"step {i:02d}: {position}")

    output_file = render_trajectory(path)

    print(f"\nStep 4 OK: trajectory rendered to {output_file}")
    print("SMOKE TEST PASSED: one shortest-path navigation episode ran successfully.")


if __name__ == "__main__":
    main()