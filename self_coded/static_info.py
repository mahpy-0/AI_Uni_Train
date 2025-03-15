import random


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

# global is_corner
is_corner = False
# global last_action
last_action = ""

DIMENSIONS = (rows, columns)
ENV = tiles.copy()
FULL_CLEAN_FLAG = False
AGENT_LOC = [agent_row, agent_column]

def set_clean_flag():
    FULL_CLEAN_FLAG = True

