import re


pz = open("day3/puzzle_input.txt", "r").read()

# RegEx pattern to find correct mul(digits, digits)
pattern: str = r"mul\((\d{1,3}),(\d{1,3})\)"
dont_and_do_blocks: list[str] = re.split(r"(don't\(\)|do\(\))", pz)


total: int = 0
count_block: bool = True


for block in dont_and_do_blocks:
    if block == "don't()":
        count_block = False
    elif block == "do()":
        count_block = True
    elif count_block:
        matches = re.findall(pattern, block)
        for match in matches:
            number1, number2 = map(int, match)
            total += number1 * number2

print(total)
