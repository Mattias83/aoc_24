# Rules
# This word search allows words to be horizontal, vertical, diagonal,
# written backwards, or even overlapping other words. It's a little
# unusual, though, as you don't merely need to find one instance of
# XMAS - you need to find all of them.

# Test data, should contain 18 'xmas'
pz_test: list[str] = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

pz: list[list[str]] = [
    [column for column in row]
    for row in open("day4/puzzle_input.txt", "r").read().splitlines()
]

directions: list[tuple[int, int]] = [  # tuple (row, col)
    (-1, 0),  # up
    (-1, -1),  # up, left
    (-1, 1),  # up, right
    (1, 0),  # down
    (1, -1),  # down, left
    (1, 1),  # down, right
    (0, -1),  # left
    (0, 1),  # right
]


ROWS: int = len(pz)
COLS: int = len(pz[0])  # all rows are equal length


def find_xmas(row: int, col: int, dir_row: int, dir_col: int) -> bool:
    # Return False if end_row or end_col is outside  grid
    end_row: int = row + 3 * dir_row
    end_col: int = col + 3 * dir_col
    if not (0 <= end_row < ROWS and 0 <= end_col < COLS):
        return False

    # Check if direction from X equals expected letter in 'XMAS'
    exptected: list[str] = ["M", "A", "S"]
    for i, letter in enumerate(exptected, start=1):
        if pz[row + i * dir_row][col + i * dir_col] != letter:
            return False

    return True


def count_xmas_in_directions(row: int, col: int) -> int:
    """
    Counts all 'XMAS' that starts at given position in all directions
    """
    return sum(
        1
        for dir_row, dir_col in directions
        if find_xmas(row, col, dir_row, dir_col)
    )


word_count: int = sum(
    count_xmas_in_directions(row, col)
    for row in range(ROWS)
    for col in range(COLS)
    if pz[row][col] == "X"
)


print(f"Total occurrences of 'XMAS' {word_count} times.")
