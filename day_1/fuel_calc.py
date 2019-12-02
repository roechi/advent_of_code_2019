from functools import reduce
from math import floor


def calculate_fuel(weight: int) -> int:
    return floor(weight / 3) - 2


def calculate_fuel_for_many(weights: [int]) -> int:
    fuel_results = list(map(calculate_fuel, weights))
    return reduce(lambda l, r: l + r, fuel_results, 0)


def calculate_fuel_recursively(weight: int) -> int:
    fuel = calculate_fuel(weight)
    return 0 if fuel <= 0 else fuel + calculate_fuel_recursively(fuel)

def calculate_fuel_for_many_recursively(weights: [int]) -> int:
    fuel_results = list(map(calculate_fuel_recursively, weights))
    return reduce(lambda l, r: l + r, fuel_results, 0)
