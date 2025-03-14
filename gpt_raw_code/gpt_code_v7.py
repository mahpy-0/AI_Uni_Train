import random

class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
        print(f"Initial environment:")
        for row in self.grid:
            print(row)

    def get_state(self, x, y):
        return [x, y, self.grid[x][y]]

    def clean_room(self, x, y):
        self.grid[x][y] = 0

    def is_clean(self):
        return all(all(cell == 0 for cell in row) for row in self.grid)

class VacuumAgent:
    def __init__(self, env):
        self.env = env
        self.x = random.randint(0, env.rows - 1)
        self.y = random.randint(0, env.cols - 1)
        self.visited = set()
        self.steps = 0
        self.path = []

    def action(self):
        state = self.env.get_state(self.x, self.y)
        self.visited.add((self.x, self.y))
        self.path.append((self.x, self.y))

        if state[2] == 1:  # Dirty room
            self.env.clean_room(self.x, self.y)
            print(f"Step {self.steps}: Cleaned room at ({self.x}, {self.y})")
        else:
            print(f"Step {self.steps}: Room at ({self.x}, {self.y}) is clean")

        # Improved Movement Logic - Systematic exploration
        if len(self.visited) < self.env.rows * self.env.cols:
            unvisited_cells = [(i, j) for i in range(self.env.rows) for j in range(self.env.cols) if (i, j) not in self.visited]
            if unvisited_cells:
                self.x, self.y = random.choice(unvisited_cells)

        self.steps += 1

# Main program
def main():
    rows, cols = 4, 4  # Changeable grid size
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
