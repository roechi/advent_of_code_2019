def has_exact_amount_of_digits(number_to_check: int, digits_count: int) -> bool:
    return len(str(number_to_check)) == digits_count


def has_only_increasing_digits(number_to_check: int) -> bool:
    s = str(number_to_check)
    for i in range(len(s)):
        if i < len(s) - 1:
            if int(s[i]) > int(s[i + 1]):
                return False

    return True


def has_at_least_one_pair_of_adjacent_equal_digits(number_to_check: int) -> bool:
    s = str(number_to_check)

    for i in range(len(s)):
        if i < len(s) - 2:
            if i == 0:
                if int(s[i]) == int(s[i + 1]) and int(s[i]) != int(s[i + 2]):
                    return True
            else:
                if int(s[i-1]) != int(s[i]) and int(s[i]) == int(s[i + 1]) and int(s[i]) != int(s[i + 2]):
                    return True
        elif i < len(s) - 1:
            if i == 0:
                if int(s[i]) == int(s[i + 1]):
                    return True
            else:
                if int(s[i-1]) != int(s[i]) and int(s[i]) == int(s[i + 1]):
                    return True

    return False


def has_adjacent_equal_digits(number_to_check: int) -> bool:
    s = str(number_to_check)

    for i in range(len(s)):
        if i < len(s) - 1:
            if int(s[i]) == int(s[i + 1]):
                return True

    return False


def calculate_number_of_possibilities(range_start: int, range_end: int, digits: int):
    assert has_exact_amount_of_digits(range_start, digits)
    assert has_exact_amount_of_digits(range_end, digits)

    current = range_start

    possibilities = list()

    while current <= range_end:
        if has_only_increasing_digits(current) and has_adjacent_equal_digits(current):
            possibilities.append(current)
        current += 1

    return len(possibilities)


def calculate_number_of_possibilities_with_solitary_pair(range_start: int, range_end: int, digits: int):
    assert has_exact_amount_of_digits(range_start, digits)
    assert has_exact_amount_of_digits(range_end, digits)

    current = range_start

    possibilities = list()

    while current <= range_end:
        if has_only_increasing_digits(current) and has_at_least_one_pair_of_adjacent_equal_digits(current):
            possibilities.append(current)
        current += 1

    return len(possibilities)

