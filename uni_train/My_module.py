import random


class Environment:

    """
        environment class that represent the environment in this problem
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.rooms = [
            [random.choice([0, 1]) for column in range(cols)] for row in range(rows)
        ]
        print(f"starting space:")
        for row in range(self.rows):
            for column in range(self.cols):
                print(self.rooms[row][column], end="\t")
            print()
        print()

    def get_state(self, x, y) -> list:
        """return state at (x, y)"""
        return [x, y, self.rooms[x][y]]

    def clean_room(self, x, y):
        """set the room at (x, y) to zero (clean the room)"""
        self.rooms[x][y] = 0

    def is_clean(self):
        """return true if all rooms are 0 (clean) if not return false"""
        return all(all(cell == 0 for cell in row) for row in self.rooms)


class Agent:

    """
        agent class that represent the agent in this problem 
    """

    def __init__(self, env):
        self.env = env
        self.x = random.randint(0, env.rows - 1)
        self.y = random.randint(0, env.cols - 1)
        self.visited = set()
        self.steps = 0
        self.path = []
        self.target_path = self.create_path()

    def create_path(self) -> list:
        """generate a path from one the selected corners"""
        corners = [
            (0, 0),   # top left
            (0, self.env.cols - 1),   # top right
            (self.env.rows - 1, 0),   # bottom left
            (self.env.rows - 1, self.env.cols - 1)   # bottom right
        ]
        # select the start corner based one the manhattan distance of agent starting location and corners
        start_corner = min(corners, key=lambda corner: abs(
            self.x - corner[0]) + abs(self.y - corner[1]))

        path = []
        visited_locations = set()
        x, y = start_corner
        delta_x, delta_y = 0, 1

        # this loop create the path that the agent will follow to clean all room
        for _ in range(self.env.rows * self.env.cols):   # loop rows * cols times
            # if current locarion is not visited and x is between the 0 _ rows - 1 and y is between 0 _ cols - 1
            if ((x, y) not in visited_locations) and (0 <= x < self.env.rows) and (0 <= y < self.env.cols):
                # append the (x, y) to path to traverse over later on
                path.append((x, y))
                # add the (x, y) to visited_locations set to have it in memory to not visit this room later
                visited_locations.add((x, y))

            possible_directions = [
                (delta_x, delta_y),   # move to right
                (delta_y, -delta_x),   # move to bottom
                (-delta_x, -delta_y),   # move to left
                (-delta_y, delta_x)   # move to top
            ]
            moved = False   # var to control if there is no more possible move break the parent loop and return the path
            # check if the possible next room is valid and feasible to move, if is change the delta__x and delta_y to the selected ones so the x and y changed and added to the path and visited_locations
            for new_delta_x, new_delta_y in possible_directions:
                next_x, next_y = x + new_delta_x, y + new_delta_y
                if (0 <= next_x < self.env.rows) and (0 <= next_y < self.env.cols) and ((next_x, next_y) not in visited_locations):
                    delta_x, delta_y = new_delta_x, new_delta_y
                    moved = True
                    break

            # if inner loop didn't change the deltas, then there was no more possible move so we have to break the parent to not adding reapeted room and fall in infinite loop
            if not moved:
                break

            x, y = x + delta_x, y + delta_y

        return path

    def action(self):
        """do an action based on the current location"""
        state = self.env.get_state(self.x, self.y)
        # add current location to visited set
        self.visited.add((self.x, self.y))
        # append current location to path list for later report
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
