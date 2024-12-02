"""
The engineers are surprised by the low number of safe reports until 
they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor 
safety systems tolerate a single bad level in what would otherwise be 
a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level 
from an unsafe report would make it safe, the report instead counts as
safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

"""

# Test puzzle input

reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

reports: list[list[int]] = [
    [int(val) for val in row.split(" ")]
    for row in open("puzzle_input.txt", "r").read().splitlines()
]


def calculate_differences(report: list[int]) -> bool:
    """Generate a list of differences from a report"""
    return [b - a for a, b in zip(report, report[1:])]


def is_within_rules(differences: list[int]) -> bool:
    """Check if all differences follow the rules."""
    return all(1 <= abs(diff) <= 3 and diff != 0 for diff in differences)


def all_inc_or_all_dec(differences: list[int]) -> bool:
    """Check if the differences are either all increasing or all decreasing."""
    return all(diff > 0 for diff in differences) or all(
        diff < 0 for diff in differences
    )


def is_safe_with_dampener(report: list[int]) -> bool:
    """Check if a report is safe, considering the Problem Dampener."""
    differences = calculate_differences(report)

    # Check if the report is already safe
    if is_within_rules(differences) and all_inc_or_all_dec(differences):
        return True

    # Remove one element from report and try again
    for i in range(len(report)):
        # Create a new report without element with index
        new_report = report[:i] + report[i + 1 :]
        new_differences = calculate_differences(new_report)

        # Check if the new report is safe
        if is_within_rules(new_differences) and all_inc_or_all_dec(
            new_differences
        ):
            return True

    return False


# Count safe reports
safe_reports = sum(is_safe_with_dampener(report) for report in reports)

print(safe_reports)
