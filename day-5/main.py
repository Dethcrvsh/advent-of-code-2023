from typing import List, Tuple
from pprint import pprint
import math


INPUT_FILE: str = "input"


def get_maps(lines: List[str]) -> List[List[Tuple[int, int, int]]]:
    maps: List[List[Tuple[int, int, int]]] = []

    for line in lines:
        if not line:
            continue

        if line[-1] == ":":
            maps.append([])
            continue

        maps[-1].append(tuple(int(n) for n in line.split()))

    return maps


def get_dest(seed: int, garden_map: List[Tuple[int, int, int]]) -> int:
    for dest, source, span in garden_map:
        if source <= seed < source + span:
            return dest + seed - source
    return seed 


def get_seed_location(seed: int, maps: List[List[Tuple[int, int, int]]]) -> int:
    dest: int = seed

    for garden_map in maps:
        dest = get_dest(dest, garden_map)

    return dest


def solve_puzzle_1() -> int:
    lines: List[str] = open(INPUT_FILE, "r").read().splitlines()

    seeds: List[int] = [int(num) for num in lines[0].split(": ")[1].split()]
    maps = get_maps(lines[1:])

    seed_location: List[int] = [get_seed_location(seed, maps) for seed in seeds]

    return min(seed_location)


def solve_puzzle_2() -> int | float:
    lines: List[str] = open(INPUT_FILE, "r").read().splitlines()

    seeds: List[int] = [int(num) for num in lines[0].split(": ")[1].split()]
    maps = get_maps(lines[1:])

    min_location = math.inf

    # Brute force go brrr
    for seed, span in zip(seeds[::2], seeds[1::2]):
        for i in range(span):
            location = get_seed_location(seed + i, maps)

            if location < min_location:
                min_location = location

        print(f"Finished seed {seed}")

    return min_location


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 5   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

