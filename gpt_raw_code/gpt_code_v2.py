import random


class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1])
                      for _ in range(cols)] for _ in range(rows)]
        print(f"Initial environment: {self.grid}")

    def get_state(self, x, y):
        print(f"Getting state at ({x}, {y}): {self.grid[x][y]}")
        return [x, y, self.grid[x][y]]

    def clean_room(self, x, y):
        print(f"Cleaning room at ({x}, {y})")
        self.grid[x][y] = 0

    def is_clean(self):
        clean_status = all(all(cell == 0 for cell in row) for row in self.grid)
        print(f"Checking if all rooms are clean: {clean_status}")
        return clean_status


class VacuumAgent:
    def __init__(self, env):
        self.env = env
        self.x, self.y = 0, 0
        self.visited = set()
        self.steps = 0
        self.path = []

    def action(self):
        print(f"Agent at position ({self.x}, {self.y})")
        state = self.env.get_state(self.x, self.y)
        self.visited.add((self.x, self.y))
        self.path.append((self.x, self.y))

        if state[2] == 1:  # Room is dirty
            self.env.clean_room(self.x, self.y)
            print(f"Step {self.steps}: Cleaned room at ({self.x}, {self.y})")
        else:
            print(f"Step {self.steps}: Room at ({self.x}, {self.y}) is clean")

        # Move logic (try to visit all rooms)
        if self.y + 1 < self.env.cols and (self.x, self.y + 1) not in self.visited:
            print(f"Moving right to ({self.x}, {self.y + 1})")
            self.y += 1
        elif self.y - 1 >= 0 and (self.x, self.y - 1) not in self.visited:
            print(f"Moving left to ({self.x}, {self.y - 1})")
            self.y -= 1
        elif self.x + 1 < self.env.rows and (self.x + 1, self.y) not in self.visited:
            print(f"Moving down to ({self.x + 1}, {self.y})")
            self.x += 1
        elif self.x - 1 >= 0 and (self.x - 1, self.y) not in self.visited:
            print(f"Moving up to ({self.x - 1}, {self.y})")
            self.x -= 1

        self.steps += 1

# Main program


def main():
    rows, cols = 4, 4  # Example size (changeable)
    print(f"Grid size: {rows}x{cols}")

    env = Environment(rows, cols)
    agent = VacuumAgent(env)

    global all_rooms_clean
    all_rooms_clean = False

    while not env.is_clean():
        agent.action()

    print(f"All rooms are clean! Total steps taken: {agent.steps}")
    print(f"Path followed: {agent.path}")


if __name__ == "__main__":
    main()
