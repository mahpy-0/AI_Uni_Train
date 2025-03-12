from static_info import (
    FULL_CLEAN_FLAG,
    ENV,
    rows,
    columns
)
from Agent import agent
from Environment import environment


if __name__ == "__main__":

    print(f"rows: {rows}, columns: {columns}")

    for row in range(rows):
        for column in range(columns):
            print(ENV[row][column], end= "\t")
        print()

    precept = environment("start")
    action = agent(precept)

    if action == "suck":
        print("cleaning")

    while not FULL_CLEAN_FLAG:
        precept = environment(action)
        action = agent(precept)
        if action == "suck":
            print("cleaning")

    for row in range(rows):
        for column in range(columns):
            print(ENV[row][column], end= "\t")
        print()

    print("done")