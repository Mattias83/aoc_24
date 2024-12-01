def main():
    with open("puzzle_input.txt", "r") as pz:
        lines = pz.read().splitlines()

        # Using zip to unpack the columns in puzzle_input to left_list
        # and right_list
        left_list, right_list = map(
            lambda lst: list(map(int, lst)),
            zip(*[line.split("   ") for line in lines]),
        )

        # Multiply left_list value with number of instances in
        # rightlist and adds the result.
        total = sum(left * right_list.count(left) for left in left_list)
        print(total)


if __name__ == "__main__":
    main()
