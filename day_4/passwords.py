# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#
# 273025-767253

from collections import Counter


def main():
    possible_pwd = list(range(273025, 767253))
    # part_one(possible_pwd)
    part_two(possible_pwd)


def part_one(possible_pwd: list) -> None:
    valid_pwd = 0
    for pwd in possible_pwd:
        if (
            int(str(pwd)[0])
            <= int(str(pwd)[1])
            <= int(str(pwd)[2])
            <= int(str(pwd)[3])
            <= int(str(pwd)[4])
            <= int(str(pwd)[5])
        ) and (
            (int(str(pwd)[0]) == int(str(pwd)[1]))
            or (int(str(pwd)[1]) == int(str(pwd)[2]))
            or (int(str(pwd)[2]) == int(str(pwd)[3]))
            or (int(str(pwd)[3]) == int(str(pwd)[4]))
            or (int(str(pwd)[4]) == int(str(pwd)[5]))
        ):
            valid_pwd += 1

    print(f'Part 1 Valid Passwords: {valid_pwd}')  # 910


def part_two(possible_pwd: list) -> None:
    valid_pwd = 0
    for pwd in possible_pwd:
        if (
                int(str(pwd)[0])
                <= int(str(pwd)[1])
                <= int(str(pwd)[2])
                <= int(str(pwd)[3])
                <= int(str(pwd)[4])
                <= int(str(pwd)[5])
        ) and (
                (int(str(pwd)[0]) == int(str(pwd)[1]) and int(str(pwd)[1]) < int(str(pwd)[2]))
                or (int(str(pwd)[1]) == int(str(pwd)[2]) and int(str(pwd)[2]) < int(str(pwd)[3]))
                or (int(str(pwd)[2]) == int(str(pwd)[3]) and int(str(pwd)[3]) < int(str(pwd)[4]))
                or (int(str(pwd)[3]) == int(str(pwd)[4]) and int(str(pwd)[4]) < int(str(pwd)[5]))
                or (int(str(pwd)[4]) == int(str(pwd)[5]))
        ):
            counter = Counter
            max_dupes = [char.count(char) for char in str(pwd)]
            print(max_dupes)
            # if max_dupes < 3:
            #     print(pwd)
            #     valid_pwd += 1

    print(f'Part 2 Valid Passwords: {valid_pwd}')  # 910


if __name__ == "__main__":
    main()

