from typing import List


def load_file(file: str) -> List[str]:
    with open(file, "r") as f:
        data = [x for x in f.read().split()]
    return data


def part_one(file: str) -> None:
    data = load_file(file)

    length_number = len(data[0])
    total_numbers = len(data)

    final_number_gama = []
    final_number_epsilon = []

    for column in range(0, length_number):
        total_ones = 0
        # print(f"column {column}")
        for row in range(0, total_numbers):
            # print(f" {data[row]} - {data[row][column]}")
            total_ones = total_ones + int(data[row][column])

        total_zeros = abs(total_ones - total_numbers)
        # print(f"total_ones: {total_ones}")
        # print(f"total_zeros: {total_zeros}")
        final_number_gama.append("0") if total_zeros > total_ones else final_number_gama.append("1")
        final_number_epsilon.append("1") if total_zeros > total_ones else final_number_epsilon.append("0")

    print(" ")
    # print(final_number)
    final_number_gamma_str = ''.join(final_number_gama)
    final_number_epsilon_str = ''.join(final_number_epsilon)
    print("-- Gamma --")
    print(f"Binary number {final_number_gamma_str}")
    print(f"Decimal number {int(final_number_gamma_str, 2)}")
    print("-- Epsilon --")
    print(f"Binary number {final_number_epsilon_str}")
    print(f"Decimal number {int(final_number_epsilon_str, 2)}")
    print("--")
    print(f"Final result {int(final_number_gamma_str, 2) * int(final_number_epsilon_str, 2)}")
    print("--")


def part_two(file: str) -> None:
    data = load_file(file)

    pos = 0
    final_number_oxygen = get_array_of_numbers(data, pos, True)
    final_number_co2 = get_array_of_numbers(data, pos, False)

    print(" ")
    final_number_oxygen_str = ''.join(final_number_oxygen)
    final_number_co2_str = ''.join(final_number_co2)
    print("-- Oxygen --")
    print(f"Binary number {final_number_oxygen_str}")
    print(f"Decimal number {int(final_number_oxygen_str, 2)}")
    print("-- CO2 --")
    print(f"Binary number {final_number_co2_str}")
    print(f"Decimal number {int(final_number_co2_str, 2)}")
    print("--")
    print(f"Final result {int(final_number_oxygen_str, 2) * int(final_number_co2_str, 2)}")
    print("--")


def get_array_of_numbers(data: List[str], pos: int, oxygen: bool):

    total_numbers = len(data)
    length_number = len(data[0])

    if total_numbers == 1:
        return data

    final_number_oxygen = []
    final_number_co2 = []

    array_number_with_ones = []
    array_number_with_zeros = []

    total_ones = 0
    # print(f"column {pos}")
    for row in range(0, total_numbers):
        if (int(data[row][pos])) == 1:
            array_number_with_ones.append(data[row])
        else:
            array_number_with_zeros.append(data[row])

        total_ones = total_ones + int(data[row][pos])

    total_zeros = abs(total_ones - total_numbers)
    # print(f"total_ones: {total_ones}")
    # print(f"total_zeros: {total_zeros}")
    if total_zeros > total_ones:
        final_number_oxygen = [*final_number_oxygen, *array_number_with_zeros]
        final_number_co2 = [*final_number_co2, *array_number_with_ones]
    elif total_zeros == total_ones:
        final_number_oxygen = [*final_number_oxygen, *array_number_with_ones]
        final_number_co2 = [*final_number_co2, *array_number_with_zeros]
    else:
        final_number_oxygen = [*final_number_oxygen, *array_number_with_ones]
        final_number_co2 = [*final_number_co2, *array_number_with_zeros]

    if pos < length_number:
        pos = pos + 1

    if oxygen:
        return get_array_of_numbers(final_number_oxygen, pos, True)
    else:
        return get_array_of_numbers(final_number_co2, pos, False)


if __name__ == '__main__':
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
