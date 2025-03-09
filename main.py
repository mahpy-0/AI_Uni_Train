import random
from .Agent import agent
from .Environment import environment

rows = random.randint(1, 10)
columns = random.randint(1, 10)

agent_row = random.randint(0, rows - 1)
agent_column = random.randint(0, columns - 1)

tiles = []
for row in range(rows):
    row_numbers = []
    for column in range(columns):
        row_numbers.append(random.randint(0, 1))
    tiles.append(row_numbers)


DIMENSIONS = (rows, columns)
ENV = tiles
FULL_CLEAN_FLAG = False
AGENT_LOC = (agent_row, agent_column)

def set_clean_flag():
    FULL_CLEAN_FLAG = True

if __name__ == "__main__":
    pass