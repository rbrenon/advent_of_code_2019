
def part_one(infile: list[str]):
    routes = [
        el.split(",") for el in infile
    ]  # list of lists [['R75', 'D30'], ['U62', 'R66']]

    # print(routes[0], routes[1])
    wire_0, _ = get_coords(routes[0])
    wire_1, _ = get_coords(routes[1])

    intersecting_coords = list(set(wire_0).intersection(set(wire_1)))

    manhattan_distance = []

    for intersecting_coord in intersecting_coords:
        manhattan_distance.append(abs(intersecting_coord[0]) + abs(intersecting_coord[1]))

    print(f"Shortest Manhattan Distance = {sorted(manhattan_distance)[1]}")



def part_two(infile: list[str]):
    routes = [
        el.split(",") for el in infile
    ]  # list of lists [['R75', 'D30'], ['U62', 'R66']]

    # print(routes[0], routes[1])
    wire_0, wire_0_steps = get_coords(routes[0])
    wire_1, wire_1_steps = get_coords(routes[1])

    intersecting_coords = list(set(wire_0).intersection(set(wire_1)))

    print(intersecting_coords)
    total_distance_traversed = []
    for intersecting_coord in intersecting_coords:
        print(f"w0 steps {wire_0_steps[intersecting_coord]} + w1 steps {wire_1_steps[intersecting_coord]} = total steps {abs(wire_0_steps[intersecting_coord] + abs(wire_1_steps[intersecting_coord]))}")
        total_distance_traversed.append(abs(wire_0_steps[intersecting_coord]) + abs(wire_1_steps[intersecting_coord]))

    print(f"Shortest distance traversed = {sorted(total_distance_traversed)}")


def get_coords(route: list):
    computed_route = [(0, 0)]
    steps = 0
    steps_to_computed_route = {(0, 0): steps}
    for coord in route:  # R75: str
        # print(coord)
        direction = coord[0]  # R
        distance = int(coord[1:])  # 75: int
        match direction:
            case "R":
                x = computed_route[-1][0]
                y = computed_route[-1][1]
                for x_point in range(1, distance + 1):
                    computed_route.append((x+x_point, y))
                    steps += 1
                    try:
                        steps_to_computed_route[(x+x_point, y)]
                    except:
                        steps_to_computed_route[(x+x_point, y)] = steps
                    # print(f"{coord}: {x+x_point}, {y}")
            case "U":
                x = computed_route[-1][0]
                y = computed_route[-1][1]
                for y_point in range(1, distance + 1):
                    computed_route.append((x, y+y_point))
                    steps += 1
                    try:
                        steps_to_computed_route[(x, y+y_point)]
                    except:
                        steps_to_computed_route[(x, y+y_point)] = steps
                    # print(f"{coord}: {x}, {y + y_point}")
            case "D":
                x = computed_route[-1][0]
                y = computed_route[-1][1]
                for y_point in range(1, distance + 1):
                    computed_route.append((x, y-y_point))
                    steps += 1
                    try:
                        steps_to_computed_route[(x, y-y_point)]
                    except:
                        steps_to_computed_route[(x, y-y_point)] = steps
                    # print(f"{coord}: {x}, {y - y_point}")
            case "L":
                x = computed_route[-1][0]
                y = computed_route[-1][1]
                for x_point in range(1, distance + 1):
                    computed_route.append((x-x_point, y))
                    steps += 1
                    try:
                        steps_to_computed_route[(x-x_point, y)]
                    except:
                        steps_to_computed_route[(x-x_point, y)] = steps
                    # print(f"{coord}: (x{x},y{y}) {x - x_point}, {y}")

    # print(computed_route)
    return computed_route, steps_to_computed_route


if __name__ == "__main__":
    with open("input.txt") as file:
        raw_input = file.read().splitlines()
    # part_one(raw_input)
    part_two(raw_input)     # 93528, 93536 - too low; 118599 - too high; 93654 - correct
