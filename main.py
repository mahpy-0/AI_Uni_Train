import random
# from .Agent import agent
# from .Environment import environment

rows = random.randint(1, 10)
columns = random.randint(1, 10)

tiles = []
for row in range(rows):
    row_numbers = []
    for column in range(columns):
        row_numbers.append(random.randint(0, 1))
    tiles.append(row_numbers)
