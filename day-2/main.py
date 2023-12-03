from typing import List, Dict


INPUT_FILE: str = "input"
COLORS: List[str] = ["red", "green", "blue"]
POSSIBLE_GAMES: Dict[str, int] = {"red": 12, "green": 13, "blue": 14}


def is_game_valid(game: Dict[str, int]) -> bool:
    for color, count in game.items():
        if POSSIBLE_GAMES[color] < count:
            return False
    return True


def get_parsed_games(lines: List[str]) -> List[List[Dict[str, int]]]:
    games = [line.split(": ")[1].strip() for line in lines]
    games = [game.split("; ") for game in games]
    games = [[game_round.replace(",", "").split() for game_round in game] for game in games]
    
    games = [
            [{game_round[i+1]: int(game_round[i]) for i in range(0, len(game_round), 2)} for game_round in game]
            for game in games
    ]

    return games


def get_valid_games(games: List[Dict[str, int]]) -> List[int]:
    """Get the numbers of the valid games"""
    valid_games: List[int] = []

    for game_num, game in enumerate(games):
        for color, count in game.items():
            if POSSIBLE_GAMES[color] < count:
                break
        # Never thought I would actually find a use for this syntax
        else:
            valid_games.append(game_num + 1)

    return valid_games


def get_min_games(games: List[List[Dict[str, int]]]) -> List[Dict[str, int]]:
    """Get the minimum possible amount of cubes for each game"""
    games_min: List[Dict[str, int]] = []

    for game_num, game in enumerate(games):
        games_min.append({color: 0 for color in COLORS})

        for game_round in game:
            for color, count in game_round.items():
                if games_min[game_num][color] < count:
                    games_min[game_num][color] = count

    return games_min


def solve_puzzle_1() -> int:
    lines: List[str] = open(INPUT_FILE, "r").readlines()

    games = get_parsed_games(lines)
    games_min: List[Dict[str, int]] = get_min_games(games)
    valid_games: List[int] = [i+1 for i, game in enumerate(games_min) if is_game_valid(game)]

    return sum(valid_games)


def solve_puzzle_2() -> int:
    lines: List[str] = open(INPUT_FILE, "r").readlines()

    games = get_parsed_games(lines)
    games_min: List[Dict[str, int]] = get_min_games(games)
    
    return sum([game["red"] * game["blue"] * game["green"] for game in games_min])
    

if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 2   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

