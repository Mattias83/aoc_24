"""
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47

75 is correctly first because there are rules that put each other page
after it: 75|47, 75|61, 75|53, and 75|29.

47 is correctly second because 75 must be before it (75|47) and every
other page must be after it according to 47|61, 47|53, and 47|29.

61 is correctly in the middle because 75 and 47 are before it
(75|61 and 47|61) and 53 and 29 are after it (61|53 and 61|29).

53 is correctly fourth because it is before page number 29 (53|29).

29 is the only page left and so is correctly last.


The fifth update, 61,13,29, is also not in the correct order, since it breaks the rule 29|13.

"""

page_order_rules: set[tuple[int, int]] = set()
page_updates: list[list[int]] = []


# Reads puzzle input and splits data into a set of page order rules and
# a list with page updates
with open("day5/puzzle_input.txt", "r") as file:
    lines = file.read().strip().split("\n")
    for line in lines:
        if "|" in line:
            a, b = map(int, line.split("|"))
            page_order_rules.add((a, b))
        elif "," in line:
            page_updates.append(list(map(int, line.split(","))))


total: int = 0


for update in page_updates:
    is_valid: bool = True
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            # Break if in wrong order
            if (update[j], update[i]) in page_order_rules:
                is_valid = False
                break
        if not is_valid:
            continue

    if is_valid:
        # Get middle value from correct ordered page update
        middle = update[len(update) // 2]
        total += middle


print("Total:", total)
