from unittest import TestCase

from nose.tools import assert_equals

from day_4 import PasswordCracker


class TestPasswordCracker(TestCase):
    def test_has_exact_amount_of_digits(self):
        result = PasswordCracker.has_exact_amount_of_digits(123, 3)
        assert_equals(result, True)

        result = PasswordCracker.has_exact_amount_of_digits(12, 3)
        assert_equals(result, False)

        result = PasswordCracker.has_exact_amount_of_digits(12, 1)
        assert_equals(result, False)

    def test_has_only_increasing_digits(self):
        result = PasswordCracker.has_only_increasing_digits(123)
        assert_equals(result, True)

        result = PasswordCracker.has_only_increasing_digits(1223)
        assert_equals(result, True)

        result = PasswordCracker.has_only_increasing_digits(121)
        assert_equals(result, False)

    def test_has_at_least_one_pair_of_adjacent_equal_digits(self):
        result = PasswordCracker.has_adjacent_equal_digits(1223)
        assert_equals(result, True)

        result = PasswordCracker.has_adjacent_equal_digits(11223)
        assert_equals(result, True)

        result = PasswordCracker.has_adjacent_equal_digits(122223)
        assert_equals(result, True)

        result = PasswordCracker.has_adjacent_equal_digits(123)
        assert_equals(result, False)

    def test_result_of_part_one(self):
        start = 347312
        end = 805915
        digits = 6

        result = PasswordCracker.calculate_number_of_possibilities(start, end, digits)

        print('The amount of possibilities for the password is: ' + str(result))
