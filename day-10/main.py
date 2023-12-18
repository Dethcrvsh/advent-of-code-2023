INPUT_FILE: str = "input"


def add_padding(maze: list[str]) -> list[str]:
    maze = ["." * (len(maze[0]))] + maze + ["." * (len(maze[0]))]
    maze = ["." + line + "." for line in maze]

    return maze


def get_next_pipe(maze: list[str], pipe: tuple[int, int]) -> list[tuple[int, int]]:
    next_pipes: list[tuple[int, int]]

    match maze[pipe[1]][pipe[0]]:
        case "|":
            next_pipes = [(0, -1), (0, 1)]
        case "-":
            next_pipes = [(-1, 0), (1, 0)]
        case "L":
            next_pipes = [(1, 0), (0, -1)]
        case "J":
            next_pipes = [(-1, 0), (0, -1)]
        case "7":
            next_pipes = [(-1, 0), (0, 1)]
        case "F":
            next_pipes = [(1, 0), (0, 1)]
        case "S":
            next_pipes = [
                (x, y) for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)) if pipe in get_next_pipe(maze, (x + pipe[0], y + pipe[1]))
            ]
        case _:
            return []

    return [(x + pipe[0], y + pipe[1]) for x, y in next_pipes]


def get_start(maze: list[str]) -> tuple[int, int]:
    for y, line in enumerate(maze):
        for x, pipe in enumerate(line):
            if pipe == "S":
                return (x, y)
    return (-1, -1)


def get_loop(maze: list[str]) -> list[tuple[int, int]]:
    start_pipe: tuple[int, int] = get_start(maze)
    loop: list[tuple[int, int]] = [start_pipe]

    current_pipe: tuple[int, int] = start_pipe
    last_pipe: tuple[int, int] = (-1, -1)

    while True:
        next_pipes: list[tuple[int, int]] = get_next_pipe(maze, current_pipe)

        # Make sure not to back track
        for pipe in next_pipes:
            if not pipe == last_pipe:
                last_pipe = current_pipe
                current_pipe = pipe
                break
        
        if current_pipe == start_pipe:
            break

        loop.append(current_pipe)

    return loop


def print_maze(maze: list[str], loop: list[tuple[int, int]]):
    print("\033[2J")

    was_in_loop = False

    for y, line in enumerate(maze):
        maze_line: str = ""
        for x, pipe in enumerate(line):
            maze_line += f"\033[1;33m{pipe}\033[1;0m" if (x, y) in loop else pipe
        print(maze_line)


def flood(maze: list[str], loop: list[tuple[int, int]]):
    flooded_tiles: list[tuple[int, int]] = []

    for y, line in enumerate(maze):
        inside_loop: bool = False
        tiles: list[tuple[int, int]] = []

        for x, pipe in enumerate(line):
            next_pipes: list[tuple[int, int]] = get_next_pipe(maze, (x, y))
            if (x, y) in loop and (x - 1, y) not in next_pipes and (x + 1, y) not in next_pipes:
                inside_loop = not inside_loop

            # Check whether the pipe is inside the loop and not on its border
            if inside_loop and (x, y) not in loop:
                flooded_tiles.append((x, y))

    return flooded_tiles


def solve_puzzle_1() -> int:
    maze: list[str] = open(INPUT_FILE).read().splitlines()
    # Add padding around the maze because bounds checking is cringe
    maze = add_padding(maze)

    return len(get_loop(maze)) // 2


def solve_puzzle_2() -> int:
    maze: list[str] = open(INPUT_FILE).read().splitlines()
    # Add padding around the maze because bounds checking is cringe
    maze = add_padding(maze)

    loop: list[tuple[int, int]] = get_loop(maze)

    print(flood(maze, loop))

    return len(flood(maze, loop))


if __name__ == "__main__":
    print("⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆   Advent of Code - Day 10   ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆\n")
    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")

