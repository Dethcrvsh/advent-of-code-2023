from typing import List


INPUT_FILE: str = "input"


def get_winning_numbers(scratch_card: List[List[str]]) -> int:
    numbers: List[str] = scratch_card[0]
    winning_numbers: List[str] = scratch_card[1]

    return sum([1 for win_num in winning_numbers if win_num and win_num in numbers])


def get_scratch_card_copies(scratch_cards: List[List[List[str]]]) -> List[int]:
    """Get a list of how many copies each scratch card has"""
    scratch_card_copies: List[int] = [1 for _ in range(len(scratch_cards))]

    for i, scratch_card in enumerate(scratch_cards):
        win_nums: int = get_winning_numbers(scratch_card)

        for j in range(1, win_nums + 1):
            if len(scratch_cards) < i+j:
                break
                
            scratch_card_copies[i+j] += scratch_card_copies[i]

    return scratch_card_copies


def solve_puzzle_1() -> int:
    file = open(INPUT_FILE, "r")
    lines = [line[line.index(":")+1:].strip() for line in file.readlines()]
    scratch_cards: List[List[List[str]]] = [[subline.split(" ") for subline in line.split("|")] for line in lines]

    final_score: int = 0

    for scratch_card in scratch_cards:
        score: int = 2**(get_winning_numbers(scratch_card) - 1)
        final_score += score if score >= 1 else 0

    return final_score


def solve_puzzle_2() -> int:
    file = open(INPUT_FILE, "r")
    lines = [line[line.index(":")+1:].strip() for line in file.readlines()]
    scratch_cards: List[List[List[str]]] = [[subline.split(" ") for subline in line.split("|")] for line in lines]

    scratch_card_copies: List[int] = get_scratch_card_copies(scratch_cards)

    return sum(scratch_card_copies)


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 4   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

