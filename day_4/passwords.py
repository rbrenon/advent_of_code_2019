# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#
# 273025-767253


def main():
    possible_pwd = list(range(273025, 767254))
    part_one(possible_pwd)
    # part_two(possible_pwd)


def part_one(possible_pwd: list) -> None:
    valid_pwd = 0
    valid_pwd_list = []
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
            valid_pwd_list.append(pwd)

    print(f"Part 1 Valid Passwords: {valid_pwd}")  # 910
    part_two(valid_pwd_list)


def part_two(possible_pwd: list) -> None:
    valid_pwd_2 = 0
    valid_pwd_2_list = []
    for pwd in possible_pwd:
        unique_numbs = set(str(pwd))
        occurrences = {}
        for numb in unique_numbs:
            occurrences[int(numb)] = str(pwd).count(numb)
        if 2 in occurrences.values():
            valid_pwd_2_list.append(pwd)
            valid_pwd_2 += 1

    print(
        f"Part 2 Valid Passwords: {valid_pwd_2}"
    )  # 251, 475 - too low; 1603 - too high; 598 - correct


if __name__ == "__main__":
    main()
