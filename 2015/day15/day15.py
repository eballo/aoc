import itertools
from typing import List
import json


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def parse_ingredients(raw_values: List[str]) -> dict[str, dict[str, int]]:
    ingredients = {}
    for ingredient in raw_values:
        ingredient, properties = ingredient.split(": ")
        properties = properties.split(",")
        ingredients[ingredient] = {}
        for element_property in properties:
            property_name, quantity = element_property.strip().split(" ")
            ingredients[ingredient][property_name] = int(quantity)

    return ingredients


def calculate_score(amounts: dict, ingredients: dict) -> int:
    capacity, durability, flavor, texture, calories, score = 0, 0, 0, 0, 0, 0

    for (ingredient, amount) in amounts.items():
        capacity += amount * ingredients[ingredient]['capacity']
        durability += amount * ingredients[ingredient]['durability']
        flavor += amount * ingredients[ingredient]['flavor']
        texture += amount * ingredients[ingredient]['texture']
        calories += amount * ingredients[ingredient]['calories']

    # Properties must not be negative
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)

    score = capacity * durability * flavor * texture
    return score


def find_best_score(ingredients):
    best_score = 0
    ingredient_names = list(ingredients.keys())

    for amounts in itertools.product(range(101), repeat=len(ingredient_names)):
        if sum(amounts) == 100:
            amounts_dict = dict(zip(ingredient_names, amounts))
            score = calculate_score(amounts_dict, ingredients)
            if score > 0:
                print(f"amounts: {amounts_dict}, score: {score}")
            best_score = max(best_score, score)

    return best_score


def part_one(file: str):
    raw_values = load_file(file)
    ingredients = parse_ingredients(raw_values)
    print(json.dumps(ingredients, indent=2))
    score = find_best_score(ingredients)

    print(f"what is the total score of the highest-scoring cookie you can make? {score}")


def part_two(file: str):
    raw_values = load_file(file)
    ingredients = parse_ingredients(raw_values)
    print(json.dumps(ingredients, indent=2))


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
