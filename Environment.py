from .main import (
    ENV,
    AGENT_LOC
)


def environment(action: str) -> list:
    """
    take a action\n
    action =: suck | go_right | go_left | go_up | go_down
    """
    if action == "suck":
        ENV[AGENT_LOC[0]][AGENT_LOC[1]] = 0
        return [
            AGENT_LOC[0],
            AGENT_LOC[1],
            ENV[AGENT_LOC[0]][AGENT_LOC[1]]
        ]

    elif action == "go_down":
        AGENT_LOC[0] += 1
        return [
            AGENT_LOC[0],
            AGENT_LOC[1],
            ENV[AGENT_LOC[0]][AGENT_LOC[1]]
        ]

    elif action == "go_up":
        AGENT_LOC[0] -= 1
        return [
            AGENT_LOC[0],
            AGENT_LOC[1],
            ENV[AGENT_LOC[0]][AGENT_LOC[1]]
        ]

    elif action == "go_right":
        AGENT_LOC[1] += 1
        return [
            AGENT_LOC[0],
            AGENT_LOC[1],
            ENV[AGENT_LOC[0]][AGENT_LOC[1]]
        ]
    
    elif action == "go_left":
        AGENT_LOC[1] -= 1
        return [
            AGENT_LOC[0],
            AGENT_LOC[1],
            ENV[AGENT_LOC[0]][AGENT_LOC[1]]
        ]
