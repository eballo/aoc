
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def count_houses(directions):
    # Initialize Santa's position
    x = 0
    y = 0

    # Dictionary to store houses and their present counts
    houses = {(x, y): 1}

    # Iterate through each direction
    # print(directions)
    for direction in directions:
        # print(direction)
        # Update Santa's position based on the direction
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1

        # Increment the present count for the current house
        houses[(x, y)] = houses.get((x, y), 0) + 1

    # Return the number of houses that received at least one present
    return len(houses)


def count_houses_with_robo_santa(directions):
    # Initialize Santa's and Robo-Santa's positions
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0

    # Set to store houses visited by Santa and Robo-Santa
    santa_houses = {(santa_x, santa_y)}
    robo_houses = {(robo_x, robo_y)}

    # Iterate through each direction
    for i, direction in enumerate(directions):
        # Decide whether it's Santa's turn or Robo-Santa's turn
        # Santa and Robo are splitting the work, and that means that
        # Santa will do the pair ones and Robo the odd ones
        if i % 2 == 0:
            # Update Santa's position based on the direction
            if direction == '^':
                santa_y += 1
            elif direction == 'v':
                santa_y -= 1
            elif direction == '>':
                santa_x += 1
            elif direction == '<':
                santa_x -= 1
            # Add Santa's new position to the set of visited houses
            santa_houses.add((santa_x, santa_y))
        else:
            # Update Robo-Santa's position based on the direction
            if direction == '^':
                robo_y += 1
            elif direction == 'v':
                robo_y -= 1
            elif direction == '>':
                robo_x += 1
            elif direction == '<':
                robo_x -= 1
            # Add Robo-Santa's new position to the set of visited houses
            robo_houses.add((robo_x, robo_y))

    # Merge the sets of visited houses and count the total number
    all_houses = santa_houses.union(robo_houses)

    # Return the number of houses that received at least one present
    return len(all_houses)


def part_one(file: str):
    raw_values = load_file(file)

    # Because is all in one line we just select the first row to get all the values
    value = count_houses(raw_values[0])
    print(f"Houses that received at least one present: {value}")


def part_two(file: str):
    raw_values = load_file(file)

    # Because is all in one line we just select the first row to get all the values
    value = count_houses_with_robo_santa(raw_values[0])
    print(f"Houses that received at least one present: {value}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
