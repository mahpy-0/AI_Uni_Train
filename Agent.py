from math import floor
# from static_info import (
#     set_clean_flag,
#     DIMENSIONS,
#     is_corner,
#     last_action
# )

from static_info import set_clean_flag

# is_corner = is_corner
# last_action = last_action


# region function_base

# def agent(precept: list) -> str:

#     """
#     return `action` for environment\n
#     take a list with 3 parameter inside:\n
#     precet[0] -> row\n
#     precet[1] -> column\n
#     precet[2] -> state\n
#     state =: 0 -> clean, 1 -> dirty"""

#     if precept[2]:

#         return "suck"

#     elif is_corner:
#         if precept[0] == 0 & precept[1] == 0:
#             if (precept[0] == 0) & (precept[1] == 0) & (last_action == ""):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_right"
#                 return "go_right"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_right"
#                 return "go_right"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1):
#                 set_clean_flag()
#                 return "suck"

#             elif (precept[0] == DIMENSIONS[0]) & (precept[1] == DIMENSIONS[1] - 1):
#                 set_clean_flag()
#                 return "suck"
#         elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0):

#             if (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0) & (last_action == ""):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_right"
#                 return "go_right"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_right"
#                 return "go_right"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1):
#                 set_clean_flag()
#                 return "suck"

#             elif (precept[0] == 0) & (precept[1] == DIMENSIONS[1] - 1):
#                 set_clean_flag()
#                 return "suck"
#         elif (precept[0] == 0) & (precept[1] == DIMENSIONS[1] - 1):

#             if (precept[0] == 0) & (precept[1] == DIMENSIONS[1] - 1) & (last_action == ""):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_left"
#                 return "go_left"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_left"
#                 return "go_left"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] == 0) & (precept[1] == 0):
#                 set_clean_flag()
#                 return "suck"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0):
#                 set_clean_flag()
#                 return "suck"
#         elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1):

#             if (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1) & (last_action == ""):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
#                 last_action = "go_left"
#                 return "go_left"

#             elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_down"
#                 return "go_down"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
#                 last_action = "go_left"
#                 return "go_left"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
#                 last_action = "go_up"
#                 return "go_up"

#             elif (precept[0] == 0) & (precept[1] == 0):
#                 set_clean_flag()
#                 return "suck"

#             elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0):
#                 set_clean_flag()
#                 return "suck"

#     else:

#         if (precept[0] <= floor(DIMENSIONS[0]/2)) & (precept[0] - 1 >= 0):
#             return "go_up"

#         elif (precept[0] > floor(DIMENSIONS[0]/2)) & (precept[0] + 1 < DIMENSIONS[0]):
#             return "go_down"

#         elif (precept[1] <= floor(DIMENSIONS[1]/2)) & (precept[1] - 1 >= 0):
#             return "go_left"

#         elif (precept[1] > floor(DIMENSIONS[1]/2)) & (precept[1] + 1 < DIMENSIONS[1]):
#             return "go_right"

#         else:
#             is_corner = True
#             return "suck"

# endregion

# region class_base

class Agent():
    def __init__(self, ENV):
        self._is_corner = False
        self._last_action = ""
        self._ACTIVE_ENV = ENV
        self._action_selector = {
            "clean_this_tile": "suck",
            "go_down": "move_down",
            "go_up": "move_up",
            "go_right": "move_right",
            "go_left": "move_left",
        }

    # todo getter & setter for is_corner & last_action

    # todo setter for action_selector

    def think(self, precept: list) -> str:
        """

        takes a list with 3 parameters inside:
            [0] := agent row
            [1] := agent column
            [2] := environment state

        states -> 0 = clean, 1 = dirty

        return action for environment

        actions -> `suck` | `move_down` | `move_up` | `move_right` | `move_left`
        """

        if precept[2]:

            return self._action_selector.get("clean_this_tile")

        elif self._is_corner:

            if (precept[0] == 0) & (precept[1] == 0):

                if (precept[0] == 0) & (precept[1] == 0) & (self._last_action == ""):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_right"
                    return self._action_selector.get("go_right")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_right"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_right"
                    return self._action_selector.get("go_right")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_right"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == self._ACTIVE_ENV[1] - 1):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

                elif (precept[0] == self._ACTIVE_ENV[0]) & (precept[1] == self._ACTIVE_ENV[1] - 1):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

            elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == 0):

                if (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == 0) & (self._last_action == ""):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_right"
                    return self._action_selector.get("go_right")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_right"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_right"
                    return self._action_selector.get("go_right")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_right"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == self._ACTIVE_ENV[1] - 1):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

                elif (precept[0] == 0) & (precept[1] == self._ACTIVE_ENV[1] - 1):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

            elif (precept[0] == 0) & (precept[1] == self._ACTIVE_ENV[1] - 1):

                if (precept[0] == 0) & (precept[1] == self._ACTIVE_ENV[1] - 1) & (self._last_action == ""):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_left"
                    return self._action_selector.get("go_right")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_left"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_left"
                    return self._action_selector.get("go_left")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_left"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] == 0) & (precept[1] == 0):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == 0):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

            elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == self._ACTIVE_ENV[1] - 1):

                if (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == self._ACTIVE_ENV[1] - 1) & (self._last_action == ""):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_up"):
                    self._last_action = "go_left"
                    return self._action_selector.get("go_left")

                elif (precept[0] == 0) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_left"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] < self._ACTIVE_ENV[0]) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_down"
                    return self._action_selector.get("go_down")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_down"):
                    self._last_action = "go_left"
                    return self._action_selector.get("go_left")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] < self._ACTIVE_ENV[1]) & (self._last_action == "go_left"):
                    self._last_action = "go_up"
                    return self._action_selector.get("go_up")

                elif (precept[0] == 0) & (precept[1] == 0):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

                elif (precept[0] == self._ACTIVE_ENV[0] - 1) & (precept[1] == 0):
                    set_clean_flag()
                    return self._action_selector.get("clean_this_tile")

        else:

            if (precept[0] <= floor(self._ACTIVE_ENV[0]/2)) & (precept[0] - 1 >= 0):
                return self._action_selector.get("go_up")

            elif (precept[0] > floor(self._ACTIVE_ENV[0]/2)) & (precept[0] + 1 < self._ACTIVE_ENV[0]):
                return self._action_selector.get("go_down")

            elif (precept[1] <= floor(self._ACTIVE_ENV[1]/2)) & (precept[1] - 1 >= 0):
                return self._action_selector.get("go_left")

            elif (precept[1] > floor(self._ACTIVE_ENV[1]/2)) & (precept[1] + 1 < self._ACTIVE_ENV[1]):
                return self._action_selector.get("go_right")

            else:
                self._is_corner = True
                return self._action_selector.get("clean_this_tile")

# endregion
