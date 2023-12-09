INPUT_FILE: str = "input"


def get_next_num(sequence: list[int]) -> int:
    if all(num == 0 for num in sequence):
        return 0

    return sequence[-1] + get_next_num([j - i for i, j in zip(sequence, sequence[1:])])


def solve_puzzle_1() -> int:
    sequences: list[list[int]]  = list(map(lambda x: list(map(int, x.split())), open(INPUT_FILE).read().splitlines()))

    return sum(map(get_next_num, sequences))


def solve_puzzle_2() -> int:
    sequences: list[list[int]]  = list(map(lambda x: list(map(int, x.split())), open(INPUT_FILE).read().splitlines()))

    return sum(map(get_next_num, [seq[::-1] for seq in sequences]))


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 9   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

