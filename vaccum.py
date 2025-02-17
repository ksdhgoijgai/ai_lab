class VacuumCleaner:
    def __init__(self, grid, start_position=(0, 0)):
        self.grid = grid
        self.position = start_position

    def suck(self):
        x, y = self.position
        if self.grid[x][y] == 1:
            print(f"Sucking dirt at position {self.position}")
            self.grid[x][y] = 0

    def move(self):
        x, y = self.position
        if self.grid[x][y] == 0 and y + 1 < len(self.grid[0]):
            self.position = (x, y + 1)
        elif y + 1 >= len(self.grid[0]) and x + 1 < len(self.grid):
            self.position = (x + 1, 0)

    def identify_room(self):
        x, y = self.position

        return "Room A" if x < len(self.grid) // 2 else "Room B"

    def vacuum(self):
        while any(1 in row for row in self.grid):
            self.suck()
            print(f"In {self.identify_room()} at {self.position}")
            self.move()

    def print_grid(self):
        for row in self.grid:
            print(' '.join(map(str, row)))



floor = []
m = int(input("Enter the No. of Rows: "))
n = int(input("Enter the No. of Columns: "))
print("Enter clean status for each cell (1 - dirty, 0 - clean)")
for i in range(m):
        l1=[]
        for j in range(n):
          l1.append(int(input("enter the value")))
        floor.append(l1)

vacuum = VacuumCleaner(floor)
vacuum.print_grid()
vacuum.vacuum()
vacuum.print_grid()
