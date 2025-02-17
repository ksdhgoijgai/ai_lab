from collections import deque

def generate_graph(x, y, d):
    queue = deque([((0, 0), [])])
    visited = set()
    visited.add((0, 0))

    while queue:
        (curr_x, curr_y), path = queue.popleft()

        if curr_x == d or curr_y == d:
            return path + [(curr_x, curr_y)]

        next_states = [
            (x, curr_y),
            (curr_x, y),
            (0, curr_y),
            (curr_x, 0),
            (curr_x - min(curr_x, y - curr_y), curr_y + min(curr_x, y - curr_y)),
            (curr_x + min(curr_y, x - curr_x), curr_y - min(curr_y, x - curr_x))
        ]

        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(curr_x, curr_y)]))

    return None

x, y, d = 5, 3, 4
path = generate_graph(x, y, d)

if path:
    print("Path to the solution:")
    for state in path:
        print(state)
else:
    print("No solution found.")

