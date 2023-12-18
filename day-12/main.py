from itertools import product
from pprint import pprint


INPUT_FILE: str = "input"


def get_possible_springs(row: str) -> list[str]:
    possible_springs: list[str] = []
    permutations = [''.join(p) for p in product('X#', repeat=row.count('?'))]

    for perm in permutations:
        possible_springs.append("")

        for char in row:
            if char == "?":
                possible_springs[-1] += perm[0]
                perm = perm[1:]
            else:
                possible_springs[-1] += char

    return possible_springs


def get_spring_count(row: str) -> list[int]:
    spring_count: list[int] = []
    current_count: int = 0

    for char in row + ".":
        if char == "#":
            current_count += 1
        elif current_count > 0:
            spring_count.append(current_count)
            current_count = 0

    return spring_count


def solve_puzzle_1() -> int:
    # Brute force go brrrr
    lines: list[list[str]] = [line.split() for line in open(INPUT_FILE).read().splitlines()]

    springs: list[str] = [line[0] for line in lines]
    groups: list[list[int]] = [list(map(int, line[1].split(","))) for line in lines]

    possible_springs: list[list[str]] = list(map(get_possible_springs, springs))
    spring_count: list[list[list[int]]] = [list(map(get_spring_count, row)) for row in possible_springs]

    possibility_count = [row.count(group) for row, group in zip(spring_count, groups)]

    return sum(possibility_count)


def solve_puzzle_2() -> int:
    return 0


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 12   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")
