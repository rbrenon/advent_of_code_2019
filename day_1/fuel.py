

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    module_masses = [int(module) for module in raw_input]
    # module_masses = [100756]
    part_1(module_masses)
    part_2(module_masses)


def part_1(module_masses):
    total_mass = 0
    for mass in module_masses:
        total_mass += mass // 3 - 2
    print(total_mass)


def part_2(module_masses):
    total_mass = 0
    for mass in module_masses:
        fuel_mass = mass // 3 - 2
        total_mass += fuel_mass
        while fuel_mass >= 6:
            fuel_mass = fuel_mass // 3 - 2
            total_mass += fuel_mass
    print(total_mass)


if __name__ == "__main__":
    main()

# 3161883 - p1: too high
# 4739256 - p2: too low
# 4739336 - p2: too low