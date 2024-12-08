# Looking for the instructions, you flip over the word search to find
# that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in
# which you're supposed to find two MAS in the shape of an X.
# One way to achieve that is like this:
# M.S
# .A.
# M.S

# Test puzzle, should find 9 X-MAS.
test_puzzle_input: list[str] = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    "..........",
]

# Puzzle input data
puzzle_input: list[str] = [
    row for row in open("day4/puzzle_input.txt", "r").read().splitlines()
]


def check_pattern(grid: list[str], y: int, x: int) -> bool:
    """Function to find X-MAS pattern"""
    height = len(grid)
    width = len(grid[0])

    # Check grid boundaries
    if y - 1 < 0 or y + 1 >= height or x - 1 < 0 or x + 1 >= width:
        return False

    # Define patterns to find X-MAS
    patterns = [
        (("M", "S"), ("M", "S")),  # mas mas
        (("S", "M"), ("S", "M")),  # sam sam
        (("M", "S"), ("S", "M")),  # mas sam
        (("S", "M"), ("M", "S")),  # sam mas
    ]

    # Check patterns
    for (top_left, bottom_right), (bottom_left, top_right) in patterns:
        if (
            grid[y - 1][x - 1] == top_left
            and grid[y + 1][x + 1] == bottom_right
            and grid[y + 1][x - 1] == bottom_left
            and grid[y - 1][x + 1] == top_right
        ):
            return True

    return False


count: int = 0
PUZZLE: list[str] = puzzle_input

for y, row in enumerate(PUZZLE):
    for x, col in enumerate(row):
        if col == "A":
            if check_pattern(PUZZLE, y, x):
                count += 1

print(count)
