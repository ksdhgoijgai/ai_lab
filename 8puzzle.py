from queue import PriorityQueue


GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.empty_tile = self.find_empty_tile()
        self.moves = moves
        self.previous = previous
        self.cost = self.moves + self.manhattan_distance()

    def find_empty_tile(self):

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def manhattan_distance(self):
        # Calculate the Manhattan distance for the heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    target_i = (value - 1) // 3
                    target_j = (value - 1) % 3
                    distance += abs(target_i - i) + abs(target_j - j)
        return distance

    def generate_neighbors(self):
        neighbors = []
        x, y = self.empty_tile
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Swap the empty tile with the adjacent tile
                new_board = [list(row) for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(tuple(tuple(row) for row in new_board), self.moves + 1, self))

        return neighbors

    def __lt__(self, other):
        return self.cost < other.cost

def a_star(initial_board):
    # Initialize the initial state
    initial_state = PuzzleState(initial_board)
    pq = PriorityQueue()
    pq.put(initial_state)
    visited = set()

    while not pq.empty():
        current = pq.get()

        if current.board == GOAL:
            return current

        visited.add(current.board)

        for neighbor in current.generate_neighbors():
            if neighbor.board not in visited:
                pq.put(neighbor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
        return

    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous

    for step in reversed(path):
        for row in step:
            print(row)
        print()

# Example usage
initial_board = ((1, 2, 3), (0, 4, 5), (7, 8, 6))
solution = a_star(initial_board)
print_solution(solution)
