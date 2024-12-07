# BEWARE OF SPOILERS
#
#
#
# anish goyal
# advent of code day 4

import sys

data = open("December/5/data.txt", 'r').read().strip()
lines = data.split("\n")


def part1():
    count = 0
    # horizontal
    for line in lines:
        count += line.count("XMAS")
        count += line.count("SAMX")

    # vertical
    for line in list(zip(*lines)):
        count += "".join(line).count("XMAS")
        count += "".join(line).count("SAMX")

    # NE/SW
    diagonals = []
    for i in range(3, len(lines)):
        current_diagonal = ""
        j = 0
        while i >= 0:
            current_diagonal += lines[i][j]
            j += 1
            i -= 1
        diagonals.append(current_diagonal)

    for j in range(1, len(lines[0]) - 3):
        current_diagonal = ""
        i = len(lines) - 1
        while j < len(lines):
            current_diagonal += lines[i][j]
            j += 1
            i -= 1
        diagonals.append(current_diagonal)

    # NW/SE
    for j in range(len(lines[0]) - 3):
        current_diagonal = ""
        i = 0
        while j < len(lines):
            current_diagonal += lines[i][j]
            j += 1
            i += 1
        diagonals.append(current_diagonal)

    for i in range(1, len(lines) - 3):
        j = 0
        current_diagonal = ""
        while i < len(lines):
            current_diagonal += lines[i][j]
            j += 1
            i += 1
        diagonals.append(current_diagonal)

    for diagonal in diagonals:
        count += diagonal.count("XMAS")
        count += diagonal.count("SAMX")

    return count


def part2():
    count = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            if lines[i][j] == "A":
                if (
                    lines[i - 1][j - 1] == "M"
                    and lines[i - 1][j + 1] == "S"
                    and lines[i + 1][j - 1] == "M"
                    and lines[i + 1][j + 1] == "S"
                ):
                    count += 1
                elif (
                    lines[i - 1][j - 1] == "S"
                    and lines[i - 1][j + 1] == "S"
                    and lines[i + 1][j - 1] == "M"
                    and lines[i + 1][j + 1] == "M"
                ):
                    count += 1
                elif (
                    lines[i - 1][j - 1] == "S"
                    and lines[i - 1][j + 1] == "M"
                    and lines[i + 1][j - 1] == "S"
                    and lines[i + 1][j + 1] == "M"
                ):
                    count += 1
                elif (
                    lines[i - 1][j - 1] == "M"
                    and lines[i - 1][j + 1] == "M"
                    and lines[i + 1][j - 1] == "S"
                    and lines[i + 1][j + 1] == "S"
                ):
                    count += 1

    return count


def main():
    # if len(sys.argv) != 2:
    #     print("Usage: python3 aoc_day4.py input.txt")
    #     sys.exit(1)

    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
