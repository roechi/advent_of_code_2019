from unittest import TestCase

from day_1.fuel_calc import calculate_fuel, calculate_fuel_for_many, calculate_fuel_recursively, \
    calculate_fuel_for_many_recursively


class TestCalculate_fuel(TestCase):
    def test_calculate_fuel(self):

        expected_values = [
            (12, 2),
            (14, 2),
            (1969, 654),
            (100756, 33583)
        ]

        for tup in expected_values:
            fuel = calculate_fuel(tup[0])
            assert fuel == tup[1]

    def test_calculate_fuel_for_many(self):
        input_values = [12, 14, 1969, 100756]

        expected = 34241

        result = calculate_fuel_for_many(input_values)
        assert result == expected

    def test_calculate_fuel_for_all_modules(self):
        t = open('../resources/input_1.txt')
        lines = t.readlines()
        t.close()
        lines = list(map(lambda line: int(line.strip()), lines))

        result = calculate_fuel_for_many(lines)
        print('The overall required amount of fuel is: ' + str(result))

    def test_calculate_fuel_while_accounting_for_additional_weight_caused_by_fuel(self):
        expected_values = [(1969, 966), (100756, 50346)]

        for tup in expected_values:
            fuel = calculate_fuel_recursively(tup[0])
            assert fuel == tup[1]

    def test_calculate_all_fuel_recursively(self):
        t = open('../resources/input_1.txt')
        lines = t.readlines()
        t.close()
        lines = list(map(lambda line: int(line.strip()), lines))

        result = calculate_fuel_for_many_recursively(lines)
        print('The overall required amount of fuel is: ' + str(result))