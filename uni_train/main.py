import random
from My_module import Environment, Agent


rows = random.randint(1, 10)
cols = random.randint(1, 10)

print(f"space size: {rows}x{cols}")

env = Environment(rows, cols)
agent = Agent(env)

while not env.is_clean():
    agent.action()

print(f"All the rooms are clean. Total steps: {agent.steps}")
print(f"Path agent took: {agent.path}")
