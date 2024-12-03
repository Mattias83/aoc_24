import re


pz = open("day3/puzzle_input.txt", "r").read()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, pz)
print(sum((int(match[0]) * int(match[1])) for match in matches))
