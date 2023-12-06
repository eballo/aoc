from collections import defaultdict


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


class Card:
    def __init__(self, card_number, winning_numbers, numbers_you_have):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.numbers_you_have = numbers_you_have
        self.is_worth = 0

    def __str__(self):
        return f"Card Number: {self.card_number}\nWinning Numbers: {self.winning_numbers}\nNumbers You Have: {self.numbers_you_have}\nIs Worth: {self.is_worth}\nCard matches: {self.get_matches()}\n"

    def get_matches(self) -> list[int]:
        return [x for x in self.winning_numbers if x in self.numbers_you_have]

    def add_is_worth(self, value: int) -> None:
        self.is_worth = value


def get_cards(raw_lines: list[str]) -> list[Card]:
    cards = []
    for line in raw_lines:
        raw_card_number = line.split(":")[0].strip()
        raw_winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
        raw_numbers_you_have = line.split(":")[1].split("|")[1].strip().split(" ")

        card_number_list = [x for x in raw_card_number if x.isdigit()]
        winning_numbers = [x for x in raw_winning_numbers if x.isdigit()]
        numbers_you_have = [x for x in raw_numbers_you_have if x.isdigit()]

        card_number = int(''.join(map(str, card_number_list)))

        cards.append(Card(card_number, winning_numbers, numbers_you_have))
    return cards


def part_one(file: str):
    raw_lines = load_file(file)

    cards = get_cards(raw_lines)

    worth_points = 0
    for card in cards:
        total = len(card.get_matches())
        if total == 0:
            card.add_is_worth(0)
        elif total == 1:
            card.add_is_worth(1)
        else:
            card.add_is_worth(2**(total-1))
        worth_points += card.is_worth
        print(card)

    print(f"Total Worth Points: {worth_points}")


def part_two(file: str):
    raw_lines = load_file(file)

    cards = get_cards(raw_lines)

    worth_points = 0
    cards_dict = defaultdict(int)

    for card in cards:
        cards_dict[card.card_number] += 1  # original card
        total_matches = len(card.get_matches())
        # print(f"Card Number: {card.card_number} - Total Matches: {total_matches}")
        for num in range(card.card_number + 1, card.card_number + 1 + total_matches):
            # print(f"Number: {num}")
            cards_dict[num] += cards_dict[card.card_number]

    print(cards_dict)

    print(f"total: {sum(cards_dict.values())}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
