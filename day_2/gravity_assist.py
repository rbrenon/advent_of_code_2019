from itertools import product


def main() -> None:
    filenames = ['input.txt']#, 'testinput.txt']
    for filename in filenames:
        intcode = open_file(filename)
        # part_1(intcode)
        part_2(intcode)


def open_file(filename: str) -> list:
    with open(filename) as file:
        raw_input = file.read().split(",")

    intcode = [int(val) for val in raw_input]

    if filename == "input.txt":
        intcode[1] = 12
        intcode[2] = 2
    return intcode


def part_1(intcode: list) -> None:
    for index, code in enumerate(intcode):
        if not index % 4:
            opcode = code
            if opcode != 99:
                try:
                    # print(index, opcode)
                    first_val_index = intcode[index + 1]
                    first_val = intcode[first_val_index]
                    second_val_index = intcode[index + 2]
                    second_val = intcode[second_val_index]
                    output_index = intcode[index + 3]
                    if opcode == 1:
                        result = first_val + second_val
                    elif opcode == 2:
                        result = first_val * second_val
                except IndexError:
                    # print(index)
                    pass
            intcode[output_index] = result

    print(intcode[0])      # 5434663


def part_2(intcode) -> None:
    combos = list(product(range(100), range(100)))
    orig_intcode = intcode.copy()

    for combo in combos:
        intcode = orig_intcode.copy()
        intcode[1] = combo[0]
        intcode[2] = combo[1]

        for index, code in enumerate(intcode):
            if not index % 4:
                opcode = code
                if opcode != 99:
                    try:
                        # print(index, opcode)
                        first_val_index = intcode[index + 1]
                        first_val = intcode[first_val_index]
                        second_val_index = intcode[index + 2]
                        second_val = intcode[second_val_index]
                        output_index = intcode[index + 3]
                        if opcode == 1:
                            result = first_val + second_val
                        elif opcode == 2:
                            result = first_val * second_val
                    except IndexError:
                        # print(index)
                        pass
                intcode[output_index] = result

        if intcode[0] == 19690720:
            print(f"Combo: {combo}, 100 * {combo[0]} + {combo[1]} = {100*combo[0]+combo[1]}, Intcode: {intcode[0]}")
            # Combo: (45, 59), 100 * 45 + 59 = 4559, Intcode: 19690720


if __name__ == "__main__":
    main()


