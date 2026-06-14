from collections import deque

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    
    # Find Start (S) and End (E) coordinates
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                end = (r, c)

    # Queue for BFS: stores (current_pos, path_taken)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (r, c), path = queue.popleft()

        # Check if we reached the goal
        if (r, c) == end:
            return path

        # Explore neighbors (Up, Down, Left, Right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and 
                maze[nr][nc] != 1 and (nr, nc) not in visited):
                
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None  # No path found

# --- Example Usage ---
grid = [
    ["S", 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, "E"]
]

solution = solve_maze(grid)

if solution:
    print(f"Path found! Length: {len(solution)}")
    for step in solution:
        print(step)
else:
    print("No path exists.")