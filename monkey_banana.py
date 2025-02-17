class MonkeyBananaProblem:
    def __init__(self):
        self.state = {
            "monkey": "floor",
            "box": "corner",
            "banana": "hanging",
            "monkey_position": "corner",
        }

    def move_monkey(self, position):
        if self.state["monkey"] == "floor":
            self.state["monkey_position"] = position
            print(f"Monkey moves to {position}")

    def push_box(self):
        if self.state["monkey"] == "floor" and self.state["monkey_position"] == "corner":
            self.state["box"] = "under_banana"
            self.state["monkey_position"] = "under_banana"
            print("Monkey pushes the box under the banana")

    def climb_box(self):
        if self.state["monkey_position"] == "under_banana" and self.state["box"] == "under_banana":
            self.state["monkey"] = "on_box"
            print("Monkey climbs onto the box")

    def grab_banana(self):
        if self.state["monkey"] == "on_box" and self.state["box"] == "under_banana":
            self.state["banana"] = "grabbed"
            print("Monkey grabs the banana!")

    def solve(self):
        print("Initial State:", self.state)
        self.move_monkey("corner")
        self.push_box()
        self.climb_box()
        self.grab_banana()
        print("Final State:", self.state)

if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    problem.solve()
