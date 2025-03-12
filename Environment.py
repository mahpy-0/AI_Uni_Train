# from static_info import (
#     ENV,
#     AGENT_LOC
# )

import random

# region function_base

# def environment(action: str) -> list:
#     """
#     take a action\n
#     action =: suck | go_right | go_left | go_up | go_down | start
#     """
#     if action == "suck":
#         ENV[AGENT_LOC[0]][AGENT_LOC[1]] = 0
#         return [
#             AGENT_LOC[0],
#             AGENT_LOC[1],
#             ENV[AGENT_LOC[0]][AGENT_LOC[1]]
#         ]

#     elif action == "go_down":
#         AGENT_LOC[0] += 1
#         return [
#             AGENT_LOC[0],
#             AGENT_LOC[1],
#             ENV[AGENT_LOC[0]][AGENT_LOC[1]]
#         ]

#     elif action == "go_up":
#         AGENT_LOC[0] -= 1
#         return [
#             AGENT_LOC[0],
#             AGENT_LOC[1],
#             ENV[AGENT_LOC[0]][AGENT_LOC[1]]
#         ]

#     elif action == "go_right":
#         AGENT_LOC[1] += 1
#         return [
#             AGENT_LOC[0],
#             AGENT_LOC[1],
#             ENV[AGENT_LOC[0]][AGENT_LOC[1]]
#         ]

#     elif action == "go_left":
#         AGENT_LOC[1] -= 1
#         return [
#             AGENT_LOC[0],
#             AGENT_LOC[1],
#             ENV[AGENT_LOC[0]][AGENT_LOC[1]]
#         ]

#     elif action == "start":
#         return [
#             AGENT_LOC[0],
#             AGENT_LOC[1],
#             ENV[AGENT_LOC[0]][AGENT_LOC[1]]
#         ]

# endregion

# region class_base

class Environment():
    def __init__(self):
        self._ENV = None
        self._DIMENSIONS = None
        self._agent_location = None

        self._rows = None
        self._columns = None

    def create_ENV(self):

        rows = random.randint(1, 10)
        columns = random.randint(1, 10)

        tiles = []
        for row in range(rows):
            row_numbers = []
            for column in range(columns):
                row_numbers.append(random.randint(0, 1))
            tiles.append(row_numbers)

        self._ENV = tiles.copy
        self._DIMENSIONS = (rows, columns)
        self._rows = rows
        self._columns = columns

    def start_agent_loc(self):
        agent_row = random.randint(0, self._rows - 1)
        agent_column = random.randint(0, self._columns - 1)
        self._agent_location = [agent_row, agent_column]

    def get_rows(self):
        return self._rows

    def get_columns(self):
        return self._columns

    def get_ENV(self):
        return self._ENV

    def print_state(self):
        for row in range(self._rows):
            for column in range(self._columns):
                print(self._ENV[row][column], end= "\t")
            print()

    def think(self, action: str) -> list:

        """
        take a action

        action =: suck | go_right | go_left | go_up | go_down | start

        return precept as list for agent

        precept: 
            [0] := agent row
            [1] := agent column
            [2] := environment state
        """

        if action == "suck":
            self._ENV[self._agent_location[0]][self._agent_location[1]] = 0
            return [
                self._agent_location[0],
                self._agent_location[1],
                self._ENV[self._agent_location[0]][self._agent_location[1]]
            ]

        elif action == "go_down":
            self._agent_location[0] += 1
            return [
                self._agent_location[0],
                self._agent_location[1],
                self._ENV[self._agent_location[0]][self._agent_location[1]]
            ]

        elif action == "go_up":
            self._agent_location[0] -= 1
            return [
                self._agent_location[0],
                self._agent_location[1],
                self._ENV[self._agent_location[0]][self._agent_location[1]]
            ]

        elif action == "go_right":
            self._agent_location[1] += 1
            return [
                self._agent_location[0],
                self._agent_location[1],
                self._ENV[self._agent_location[0]][self._agent_location[1]]
            ]

        elif action == "go_left":
            self._agent_location[1] -= 1
            return [
                self._agent_location[0],
                self._agent_location[1],
                self._ENV[self._agent_location[0]][self._agent_location[1]]
            ]

        elif action == "start":
            return [
                self._agent_location[0],
                self._agent_location[1],
                self._ENV[self._agent_location[0]][self._agent_location[1]]
            ]

# endregion
