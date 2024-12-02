"""
The unusual data (your puzzle input) consists of many reports, one 
report per line. Each report is a list of numbers called levels that 
are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
 - Any two adjacent levels differ by at least one and at most three.
 - In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

"""

reports: list[list[int]] = [
    [int(val) for val in row.split(" ")]
    for row in open("puzzle_input.txt", "r").read().splitlines()
]


# test puzzle input
reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def is_safe(report: list[int]) -> bool:
    # Calc difference between adjecent numbers
    differences = [b - a for a, b in zip(report, report[1:])]

    # Check if differences are within allowed range (between 1,2 or 3)
    if any(abs(diff) > 3 or diff == 0 for diff in differences):
        return False

    # check if all differences are increasing or all decreasing
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    return is_increasing or is_decreasing


safe_reports = sum(is_safe(report) for report in reports)
print(safe_reports)
