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
        self.target_path = self.generate_spiral_path()

    def generate_spiral_path(self):
        corners = [(0, 0), (0, self.env.cols - 1), (self.env.rows - 1, 0), (self.env.rows - 1, self.env.cols - 1)]
        start_corner = min(corners, key=lambda corner: abs(self.x - corner[0]) + abs(self.y - corner[1]))
        
        spiral_path = []
        visited = set()
        x, y = start_corner
        dx, dy = 0, 1

        for _ in range(self.env.rows * self.env.cols):
            if (x, y) not in visited and 0 <= x < self.env.rows and 0 <= y < self.env.cols:
                spiral_path.append((x, y))
                visited.add((x, y))

            # Check all possible directions to avoid deadlock
            possible_directions = [(dx, dy), (dy, -dx), (-dx, -dy), (-dy, dx)]
            moved = False
            for ndx, ndy in possible_directions:
                nx, ny = x + ndx, y + ndy
                if 0 <= nx < self.env.rows and 0 <= ny < self.env.cols and (nx, ny) not in visited:
                    dx, dy = ndx, ndy
                    moved = True
                    break

            if not moved:
                break  # No valid move left, stop generating path

            x, y = x + dx, y + dy

        return spiral_path

    def action(self):
        state = self.env.get_state(self.x, self.y)
        self.visited.add((self.x, self.y))
        self.path.append((self.x, self.y))

        if state[2] == 1:
            self.env.clean_room(self.x, self.y)
            print(f"Step {self.steps}: Cleaned room at ({self.x}, {self.y})")
        else:
            print(f"Step {self.steps}: Room at ({self.x}, {self.y}) is clean")

        if len(self.visited) == self.env.rows * self.env.cols:
            print(f"All rooms visited. Ending exploration.")
            return

        if self.target_path:
            self.x, self.y = self.target_path.pop(0)

        self.steps += 1

# Main program
def main():
    # rows, cols = 1, 1
    rows = random.randint(1, 20)
    cols = random.randint(1, 20)
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
