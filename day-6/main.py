from functools import reduce


INPUT_FILE: str = "input"


def get_possible_distances(time: int, distance: int) -> list[int]:
    distances: list[int] = []

    for waiting_time in range(time):
        speed: int = waiting_time
        result: int = (time - waiting_time) * speed

        if result > distance:
            distances.append(result)

    return distances


def solve_puzzle_1() -> int:
    lines : list[str] = open(INPUT_FILE, "r").read().splitlines()

    times, distances = ([int(num) for num in line.split(":")[1].split()] for line in lines)

    possible_distances: list[list[int]] = [
        get_possible_distances(time, distance) for time, distance in zip(times, distances)
    ]
    
    return reduce(lambda x, y: x * y, map(len, possible_distances))


def solve_puzzle_2() -> int:
    lines : list[str] = open(INPUT_FILE, "r").read().splitlines()

    time, distance = (int(reduce(lambda x, y: x + y, [num for num in line.split(":")[1].split()])) for line in lines)

    possible_distances: list[int] = get_possible_distances(time, distance)
    
    return len(possible_distances)


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 6   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

