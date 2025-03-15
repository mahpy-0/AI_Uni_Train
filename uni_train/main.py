import random
from My_module import Environment, Agent


rows = random.randint(1, 10)
cols = random.randint(1, 10)

print(f"space size: {rows}x{cols}")

env = Environment(rows, cols)
agent = Agent(env)

while not env.is_clean():
    agent.action()

print(f"All rooms are clean! Total steps taken: {agent.steps}")
print(f"Path followed: {agent.path}")
