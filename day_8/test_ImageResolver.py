from nose.tools import assert_equal

from day_8.ImageResolver import ImageResolver


def test_decode():
    resolver = ImageResolver()
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
    resolver.decode(values, 3, 2)
    resolver.print_layers()

    layer_with_fewest_fours = resolver.layer_with_fewest_occurrences(4)
    assert_equal(layer_with_fewest_fours, [[7, 0], [8, 1], [9, 2]])


def test_render():
    resolver = ImageResolver()
    values = [0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0]
    resolver.decode(values, 2, 2)
    resolver.print_layers()

    rendered = resolver.render()
    resolver.print_layer_ASCII(rendered)

def test_solve_part_one():
    t = open('../resources/input_8.txt')
    lines = t.readlines()
    t.close()
    values = list(map(lambda s: int(s), lines[0]))

    resolver = ImageResolver()
    resolver.decode(values, 25, 6)

    layer = resolver.layer_with_fewest_occurrences(0)
    resolver.print_layer(layer)

    ones = resolver.count_digit_on_layer(1, layer)
    twos = resolver.count_digit_on_layer(2, layer)

    print('The solution is {} * {} = {}'.format(ones, twos, ones * twos))

def test_solve_part_two():
    t = open('../resources/input_8.txt')
    lines = t.readlines()
    t.close()
    values = list(map(lambda s: int(s), lines[0]))

    resolver = ImageResolver()
    resolver.decode(values, 25, 6)

    rendered = resolver.render()
    resolver.print_layer_ASCII(rendered)
