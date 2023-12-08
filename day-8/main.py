from __future__ import annotations
from dataclasses import dataclass
import re
import math


INPUT_FILE: str = "input"

START_NODE: str = "AAA"
END_NODE: str = "ZZZ"

START_NODES_2: str = ".*A"
END_NODES_2: str = ".*Z"


@dataclass
class Node:
    name: str
    left: str
    right: str


def get_network(lines: list[str]) -> dict[str, Node]:
    return {
        name: Node(name, left, right) for node_line in lines[2:] for name, left, right in [re.sub("[=,()]", "", node_line).split()]
    }


def get_start_nodes(network: dict[str, Node], con: str) -> list[str]:
    return [name for name in network.keys() if re.search(con, name)]


def get_steps_to_goal(instructions: str, network: dict[str, Node], start_node: str, end_node_con: str):
    steps: int = 0
    # Get the starting nodes
    current_node: str = start_node

    while True:
        instruction: str = instructions[steps % len(instructions)]
        steps += 1
        
        # Get the next nodes according to the left/right instruction
        current_node = network[current_node].left if instruction == "L" else network[current_node].right

        # Quit if all current nodes match the end condition
        if re.search(end_node_con, current_node):
            return steps


def solve_puzzle_1() -> int:
    lines: list[str] = open(INPUT_FILE).read().splitlines()

    instructions: str = lines[0]
    network: dict[str, Node] = get_network(lines)

    return get_steps_to_goal(instructions, network, START_NODE, END_NODE)


def solve_puzzle_2() -> int:
    lines: list[str] = open(INPUT_FILE).read().splitlines()

    instructions: str = lines[0]
    network: dict[str, Node] = get_network(lines)
    
    # Calculate the steps for each of the starting nodes
    steps: list[int] = [
        get_steps_to_goal(instructions, network, start_node, END_NODES_2) for start_node in get_start_nodes(network, START_NODES_2)
    ]

    # Find their least common multiple
    return math.lcm(*steps)


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 8   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

