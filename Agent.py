from math import floor
from .main import (
    DIMENSIONS,
    set_clean_flag
)

is_corner = False
last_action = ""


def agent(precept: list) -> str:
    """
    return `action` for environment\n
    take a list with 3 parameter inside:\n
    precet[0] -> row\n
    precet[1] -> column\n
    precet[2] -> state\n
    state =: 0 -> clean, 1 -> dirty"""
    if precept[2]:
        # ? if dirty then clean
        # * ENV[precept[0]][precept[1]] = 0
        return "suck"
    elif is_corner:
        if precept[0] == 0 & precept[1] == 0:
            if (precept[0] == 0) & (precept[1] == 0) & (last_action == ""):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_right"
                return "go_right"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_right"
                return "go_right"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1):
                set_clean_flag()
                return "suck"

            elif (precept[0] == DIMENSIONS[0]) & (precept[1] == DIMENSIONS[1] - 1):
                set_clean_flag()
                return "suck"
        elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0):

            if (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0) & (last_action == ""):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_right"
                return "go_right"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_right"
                return "go_right"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_right"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1):
                set_clean_flag()
                return "suck"

            elif (precept[0] == 0) & (precept[1] == DIMENSIONS[1] - 1):
                set_clean_flag()
                return "suck"
        elif (precept[0] == 0) & (precept[1] == DIMENSIONS[1] - 1):

            if (precept[0] == 0) & (precept[1] == DIMENSIONS[1] - 1) & (last_action == ""):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_left"
                return "go_left"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_left"
                return "go_left"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] == 0) & (precept[1] == 0):
                set_clean_flag()
                return "suck"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0):
                set_clean_flag()
                return "suck"
        elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1):

            if (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == DIMENSIONS[1] - 1) & (last_action == ""):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_up"):
                last_action = "go_left"
                return "go_left"

            elif (precept[0] == 0) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] < DIMENSIONS[0]) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_down"
                return "go_down"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_down"):
                last_action = "go_left"
                return "go_left"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] < DIMENSIONS[1]) & (last_action == "go_left"):
                last_action = "go_up"
                return "go_up"

            elif (precept[0] == 0) & (precept[1] == 0):
                set_clean_flag()
                return "suck"

            elif (precept[0] == DIMENSIONS[0] - 1) & (precept[1] == 0):
                set_clean_flag()
                return "suck"
    else:

        if (precept[0] <= floor(DIMENSIONS[0]/2)) & (precept[0] - 1 >= 0):
            return "go_up"
        
        elif (precept[0] > floor(DIMENSIONS[0]/2)) & (precept[0] + 1 < DIMENSIONS[0]):
            return "go_down"
        
        elif (precept[1] <= floor(DIMENSIONS[1]/2)) & (precept[1] - 1 >= 0):
            return "go_left"
        
        elif (precept[1] > floor(DIMENSIONS[1]/2)) & (precept[1] + 1 < DIMENSIONS[1]):
            return "go_right"
        
        else:
            is_corner = True
            return "suck"
