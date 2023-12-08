from itertools import groupby
from functools import reduce, cmp_to_key


INPUT_FILE: str = "input"
# Sorted from weakest to strongest
CARD_STRENGTH: str = "23456789JTQKA"
CARD_STRENGTH_2: str = "J23456789TQKA"

def is_five_of_a_kind(card: str) -> bool:
    return len(set(card)) == 1


def is_four_of_a_kind(card: str) -> bool:
    return any([len(list(group)) == 4 for _, group in groupby(sorted(card))])


def is_full_house(card: str) -> bool:
    return all([l == 2 or l == 3 for _, group in groupby(sorted(card)) for l in [len(list(group))]])


def is_three_of_a_kind(card: str) -> bool:
    res: list[bool] = [len(list(group)) == 3 for _, group in groupby(sorted(card))]
    return any(res) and len(res) == 3


def is_two_pair(card: str) -> bool:
    res: list[bool] = [len(list(group)) == 2 for _, group in groupby(sorted(card))]
    return any(res) and len(res) == 3


def is_one_pair(card: str) -> bool:
    res: list[bool] = [len(list(group)) == 2 for _, group in groupby(sorted(card))]
    return any(res) and len(res) == 4


def is_high_card(card: str) -> bool:
    return len(set(card)) == len(card)


# Hands sorted from weakest to strongest
HANDS = [is_high_card, is_one_pair, is_two_pair, is_three_of_a_kind, is_full_house, is_four_of_a_kind, is_five_of_a_kind]


def get_highest_card(hand: tuple[str, int]) -> tuple[str, int]:
    # Cards to try replacing joker with
    cards = "".join(set(filter(lambda x: not x == "J", hand[0])))
    possible_hands: list[tuple[str, int]] = [(hand[0].replace("J", card), hand[1]) for card in cards]

    possible_hands = sorted(possible_hands, key=cmp_to_key(compare))

    # This do be stupid
    if hand[0] == "JJJJJ":
        return ("AAAAA", hand[1])

    return possible_hands[-1]


def compare2(hand1: tuple[str, int], hand2: tuple[str, int]):
    hand1_point: int = list(map(lambda f: f(get_highest_card(hand1)[0]), HANDS)).index(True)
    hand2_point: int = list(map(lambda f: f(get_highest_card(hand2)[0]), HANDS)).index(True)

    if hand1_point < hand2_point:
        return -1
    if hand1_point > hand2_point:
        return 1

    if hand1[0] == hand2[0]:
        return 0

    # Find the first differing cards in the two hands
    card1, card2 = [(a, b) for a, b in zip(hand1[0], hand2[0]) if a != b][0]

    return -1 if CARD_STRENGTH_2.index(card1) < CARD_STRENGTH_2.index(card2) else 1


def compare(hand1: tuple[str, int], hand2: tuple[str, int]):
    hand1_point: int = list(map(lambda f: f(hand1[0]), HANDS)).index(True)
    hand2_point: int = list(map(lambda f: f(hand2[0]), HANDS)).index(True)

    if hand1_point < hand2_point:
        return -1
    if hand1_point > hand2_point:
        return 1

    if hand1[0] == hand2[0]:
        return 0

    # Find the first differing cards in the two hands
    card1, card2 = [(a, b) for a, b in zip(hand1[0], hand2[0]) if a != b][0]

    return -1 if CARD_STRENGTH.index(card1) < CARD_STRENGTH.index(card2) else 1


def solve_puzzle_1():
    hands: list[tuple[str, int]]  = [(t[0], int(t[1])) for line in open(INPUT_FILE, "r").read().splitlines() for t in [line.split()]]

    hands = sorted(hands, key=cmp_to_key(compare))

    return sum([(i + 1) * score for i, (_, score) in enumerate(hands)])


def solve_puzzle_2() -> int:
    hands: list[tuple[str, int]]  = [(t[0], int(t[1])) for line in open(INPUT_FILE, "r").read().splitlines() for t in [line.split()]]

    hands = sorted(hands, key=cmp_to_key(compare2))

    return sum([(i + 1) * score for i, (_, score) in enumerate(hands)])


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 7   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

