# from static_info import (
#     FULL_CLEAN_FLAG,
#     ENV,
#     rows,
#     columns
# )
# from Agent import agent
# from Environment import environment


# if __name__ == "__main__":

    # print(f"rows: {rows}, columns: {columns}")

    # for row in range(rows):
    #     for column in range(columns):
    #         print(ENV[row][column], end= "\t")
    #     print()

    # precept = environment("start")
    # action = agent(precept)

    # if action == "suck":
    #     print("cleaning")

    # while not FULL_CLEAN_FLAG:
    #     precept = environment(action)
    #     action = agent(precept)
    #     if action == "suck":
    #         print("cleaning")

    # for row in range(rows):
    #     for column in range(columns):
    #         print(ENV[row][column], end= "\t")
    #     print()

# print("done")


from Environment import Environment
from Agent import Agent
from static_info import FULL_CLEAN_FLAG


if __name__ == "__main__":

    environment = Environment()

    environment.create_ENV()
    environment.start_agent_loc()

    agent = Agent(environment.get_ENV())

    rows = environment.get_rows()
    columns = environment.get_columns()

    print(f"rows: {rows}, columns: {columns}")

    environment.print_state()

    precept = environment.think("start")
    action = agent.think(precept)

    while not FULL_CLEAN_FLAG:

        if action == "suck":
            print("cleaning")
        
        precept = environment.think(action)
        action = agent.think(precept)
    
    environment.print_state()

    print("done")