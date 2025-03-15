import random


class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1]) for column in range(cols)] for row in range(
            rows)]
        print(f"Initial environment:")
        for row in self.grid:
            print(row)

    def get_state(self, x_position, y_position):
        return [x_position, y_position, self.grid[x_position][y_position]]

    def clean_room(self, x_position, y_position):
        self.grid[x_position][y_position] = 0

    def is_clean(self):
        return all(all(cell == 0 for cell in row) for row in self.grid)


class VacuumAgent:

    def __init__(self, env):
        self.env = env

        # region random_locaticon
        # self.x = random.randint(0, env.rows - 1)
        # self.y = random.randint(0, env.cols - 1)
        # engregion

        # ? n = row_number
        # ? m = col_number
        # ? if want to start from the top right corner: possible starts (0, 0) - (0, 1) - (1, 0)
        self.x, self.y = 1, env.cols - 1
        # self.x, self.y = 0, 1 # ? if want to start from the top left corner: possible starts (0, m) - (0, m - 1) - (1, m)
        # self.x, self.y = 0, 1 # ? if want to start from the bottom right corner: possible starts (n, 0) - (n, 1) - (n - 1, 0)
        # self.x, self.y = 0, 1 # ? if want to start from the bottom left corner: possible starts (n, m) - (n, m - 1) - ( n - 1, m)
        self.visited = set()
        self.steps = 0
        self.path = []
        self.target_path = self.generate_spiral_path()

    def generate_spiral_path(self):
        corners = [
            (0, 0),
            (0, self.env.cols - 1),
            (self.env.rows - 1, 0),
            (self.env.rows - 1, self.env.cols - 1)
        ]
        start_corner = min(corners, key=lambda corner: abs(
            self.x - corner[0]) + abs(self.y - corner[1]
                                      ))

        spiral_path = []
        visited_positions = set()
        x_position, y_position = start_corner
        delta_x, delta_y = 0, 1

        for _ in range(self.env.rows * self.env.cols):
            if (x_position, y_position) not in visited_positions and 0 <= x_position < self.env.rows and 0 <= y_position < self.env.cols:
                spiral_path.append((x_position, y_position))
                visited_positions.add((x_position, y_position))

            possible_directions = [
                (delta_x, delta_y), (delta_y, -delta_x), (-delta_x, -delta_y), (-delta_y, delta_x)]
            moved = False
            for new_delta_x, new_delta_y in possible_directions:
                next_x, next_y = x_position + new_delta_x, y_position + new_delta_y
                if 0 <= next_x < self.env.rows and 0 <= next_y < self.env.cols and (next_x, next_y) not in visited_positions:
                    delta_x, delta_y = new_delta_x, new_delta_y
                    moved = True
                    break

            if not moved:
                break

            x_position, y_position = x_position + delta_x, y_position + delta_y

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

    # ? can change to any number since we're cheating :-) make sure to choose any corner or near room in agent x and y
    rows = 6
    cols = 6

    print(f"Grid size: {rows}x{cols}")

    env = Environment(rows, cols)
    agent = VacuumAgent(env)

    while not env.is_clean():
        agent.action()

    print(f"All rooms are clean! Total steps taken: {agent.steps}")
    print(f"Path followed: {agent.path}")


if __name__ == "__main__":
    main()
