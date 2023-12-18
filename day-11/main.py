from itertools import combinations


INPUT_FILE: str = "input"


def get_distance(
    galaxy1: tuple[int, int],
    galaxy2: tuple[int, int],
    empty_rows: list[int],
    empty_columns: list[int],
    expansion: int,
) -> int:

    x_range: range = range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0]))
    y_range: range = range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1]))

    empty_rows_count: int = len(set(y_range).intersection(empty_rows))
    empty_columns_count: int = len(set(x_range).intersection(empty_columns))

    return (
        abs((galaxy1[0] - galaxy2[0])) + empty_columns_count * (expansion - 1) + 
        abs((galaxy1[1] - galaxy2[1])) + empty_rows_count * (expansion - 1)
    )
    

def get_empty_rows(space: list[str]) -> list[int]:
    return [y for y, line in enumerate(space) if all(char == "." for char in line)]


def get_empty_columns(space: list[str]) -> list[int]:
    return [x for x, _ in enumerate(space[0]) if all(space[y][x] == "." for y, _ in enumerate(space))]


def get_galaxies(space: list[str]) -> list[tuple[int, int]]:
    return [
        (x, y) for y, line in enumerate(space) for x, char in enumerate(line) if not char == "."
    ]


def get_closest_distances(expansion: int) -> int:
    space: list[str] = open(INPUT_FILE).read().splitlines()
    galaxies: list[tuple[int, int]] = get_galaxies(space)

    empty_rows: list[int] = get_empty_rows(space)
    empty_columns: list[int] = get_empty_columns(space)

    distance: int = 0

    for galaxy1, galaxy2 in combinations(galaxies, 2):
        distance += get_distance(galaxy1, galaxy2, empty_rows, empty_columns, expansion)
    
    return distance


def solve_puzzle_1() -> int:
    return get_closest_distances(2)


def solve_puzzle_2() -> int:
    return get_closest_distances(1000000)


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 11   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")
