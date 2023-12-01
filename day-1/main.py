from typing import List, Tuple
import math


INPUT_FILE: str = "input1"
DIGITS: List[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_lines() -> List[str]:
    file = open(INPUT_FILE, "r")
    return file.readlines()


def is_digit(char: str) -> bool:
    return char.isdigit()


def get_digit(line: str, check, start: int, find_func) -> int:
    """Helper for get first and last digit"""
    save_index: int = start
    save_digit: str = ""

    for digit in DIGITS + [str(i) for i in range(1, 10)]:
        index: int = find_func(digit)

        if check(index, save_index):
            save_index = index
            save_digit = digit

    if not save_digit:
        return -1
    elif save_digit.isdigit():
        return int(save_digit)
    else:
        return DIGITS.index(save_digit) + 1


def get_first_digit(line: str) -> int:
    return get_digit(line, lambda i, s: 0 <= i < s, len(line), line.find)


def get_last_digit(line: str) -> int:
    return get_digit(line, lambda i, s: s < i, -1, line.rfind)


def solve_puzzle_1() -> int:
    value: int = 0

    for line in get_lines():
        digits: List[str] = list(filter(is_digit, line))

        value += int(digits[0] + digits[-1]) if digits else 0

    return value


def solve_puzzle_2() -> int:
    value: int = 0

    for line in get_lines():
        first_digit: int = get_first_digit(line)
        last_digit: int = get_last_digit(line)

        if first_digit == -1 or last_digit == -1:
            continue

        value += int(str(first_digit) + str(last_digit))

    return value


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 1   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")
