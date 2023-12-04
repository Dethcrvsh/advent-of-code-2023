import collections
from typing import List, Tuple
import re


INPUT_FILE: str = "input"
NUMBERS_RE: str = "[0-9]+"
SYMBOL_RE: str = "[^0-9.]"


def is_symbol(char: str) -> bool:
    """Check if a character is a symbol"""
    return not char.isdigit() and not char == "."


def is_out_of_bounds(x: int, y: int, schematic: List[str]) -> bool:
    """Check if coordinates are out of bounds in schematic"""
    return not 0 <= x < len(schematic[0]) or not 0 <= y < len(schematic)


def is_number_valid(x: int, y: int, row_len: int, schematic: List[str]) -> bool:
    """Check if a row subsection has an adjacent symbol"""
    row_search_len: int = 2 + row_len
    column_search_len: int = 3

    for i in range(row_search_len * column_search_len):
        check_x: int = i // column_search_len + x - 1
        check_y: int = i % column_search_len + y - 1

        if is_out_of_bounds(check_x, check_y, schematic):
            continue
        
        char: str = schematic[check_y][check_x]
        
        if is_symbol(char):
            return True 

    return False


def expand_number(x: int, y: int, direction: int, schematic: List[str]) -> int:
    """Expand the bounds of a number in a given direction"""
    bound: int = x
    current_char: str = schematic[y][x]

    while True:
        new_bound: int = bound + direction

        if is_out_of_bounds(new_bound, y, schematic):
            break

        current_char = schematic[y][new_bound]

        if not current_char.isdigit():
            break

        bound = new_bound

    return bound

def get_number_at(x: int, y: int, schematic: List[str]) -> int:
    """Given a coordinate, get the number that resides there"""
    left_bound: int = expand_number(x, y, -1, schematic)
    right_bound: int = expand_number(x, y, 1, schematic)

    return int(schematic[y][left_bound:right_bound+1])


def get_surrounding_numbers(x: int, y: int, schematic: List[str]) -> List[int]:
    surrounding_numbers: List[int] = []

    for i, row in enumerate(schematic[y-1:y+2]):
        number_matches: List[re.Match] = list(re.finditer(NUMBERS_RE, row[x-1:x+2]))

        surrounding_numbers += [get_number_at(n.span()[0] + x-1, y+i-1, schematic) for n in number_matches]
        
    return surrounding_numbers


def solve_puzzle_1() -> int:
    file = open(INPUT_FILE, "r")
    # Remove newline from the lines
    schematic: List[str] = [line.strip() for line in file.readlines()]

    valid_numbers: List[int] = []

    for y, row in enumerate(schematic):
        # Get all numbers in the row
        number_matches: List[re.Match] = list(re.finditer(NUMBERS_RE, row))

        for num in number_matches:
            span: Tuple[int, int] = num.span()

            # Save the numbers if the have an adjacent symbol
            if is_number_valid(span[0], y, span[1] - span[0], schematic):
                valid_numbers.append(int(num.group()))

    return sum(valid_numbers)


def solve_puzzle_2() -> int:
    file = open(INPUT_FILE, "r")
    # Remove newline from the lines
    schematic: List[str] = [line.strip() for line in file.readlines()]

    ratio_sum: int = 0

    for y, row in enumerate(schematic):
        # Get all numbers in the row
        symbol_matches: List[re.Match] = list(re.finditer(SYMBOL_RE, row))

        for symbol in symbol_matches:
            span: Tuple[int, int] = symbol.span()

            surrounding_numbers: List[int] = get_surrounding_numbers(span[0], y, schematic)
            ratio_sum += surrounding_numbers[0] * surrounding_numbers[1] if len(surrounding_numbers) == 2 else 0

    return ratio_sum


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 3   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

