def main():
    # Load puzzle_input.txt into a list of lines.
    with open("puzzle_input.txt", "r") as pz:
        lines = pz.read().splitlines()

    # Reads in left_list & right_list and sorts them.
    left_list, right_list = map(
        lambda lst: sorted(map(int, lst)),
        zip(*[line.split("   ") for line in lines]),
    )

    # Calculate differnce and adds them togheter.
    total_difference = sum(
        abs(left - right) for left, right in zip(left_list, right_list)
    )

    print(total_difference)


if __name__ == "__main__":
    main()
