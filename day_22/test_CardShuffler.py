from nose.tools import assert_equal

from day_22.CardShuffler import CardShuffler, CardShuffler2
from day_22.CardShufflerImproved import CardShufflerImproved


def test_deal_into_new_stack():
    cs = CardShuffler(10)
    cs.deal_into_new_stack()

    assert_equal([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], cs.deck)
    cs2 = CardShuffler2(10, 3)
    cs2.deal_into_new_stack()
    assert_equal(6, cs2.pos)


def test_cut():
    cs = CardShuffler(10)
    cs.cut(3)

    assert_equal([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], cs.deck)
    cs2 = CardShuffler2(10, 3)
    cs2.cut(3)
    assert_equal(0, cs2.pos)
    cs2.cut(3, inverse=True)
    assert_equal(3, cs2.pos)


def test_cut_negative():
    cs = CardShuffler(10)
    cs.cut(-4)

    assert_equal([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], cs.deck)

    cs2 = CardShuffler2(10, 3)
    cs2.cut(-4)
    assert_equal(7, cs2.pos)
    cs2.cut(-4, inverse=True)
    assert_equal(3, cs2.pos)


def test_deal_with_increment():
    cs = CardShuffler(10)
    cs.deal_with_increment(3)

    assert_equal([0, 7, 4, 1, 8, 5, 2, 9, 6, 3], cs.deck)

    cs2 = CardShuffler2(10, 3)
    cs2.deal_with_increment(3)
    assert_equal(9, cs2.pos)
    cs2.deal_with_increment(3, inverse=True)
    assert_equal(3, cs2.pos)


def test_multiple_operations_1():
    operations = ['deal with increment 7\n',
                  'deal into new stack\n',
                  'deal into new stack\n']

    cs = CardShuffler(10)
    cs.perform(operations)
    assert_equal([0, 3, 6, 9, 2, 5, 8, 1, 4, 7], cs.deck)

    cs2 = CardShuffler2(10, 3)
    cs2.perform(operations)
    assert_equal(1, cs2.pos)

    operations.reverse()
    cs2.perform(operations, inverse=True)
    assert_equal(3, cs2.pos)


def test_multiple_operations_2():
    operations = ['cut 6\n',
                  'deal with increment 7\n',
                  'deal into new stack\n']

    cs = CardShuffler(10)
    cs.perform(operations)
    assert_equal([3, 0, 7, 4, 1, 8, 5, 2, 9, 6], cs.deck)

    cs2 = CardShuffler2(10, 3)
    cs2.perform(operations)
    assert_equal(0, cs2.pos)

    operations.reverse()
    cs2.perform(operations, inverse=True)
    assert_equal(3, cs2.pos)


def test_multiple_operations_3():
    operations = ['deal with increment 7\n',
                  'deal with increment 9\n',
                  'cut -2\n']

    cs = CardShuffler(10)
    cs.perform(operations)

    assert_equal([6, 3, 0, 7, 4, 1, 8, 5, 2, 9], cs.deck)

    cs2 = CardShuffler2(10, 3)
    cs2.perform(operations)
    assert_equal(1, cs2.pos)

    operations.reverse()
    cs2.perform(operations, inverse=True)
    assert_equal(3, cs2.pos)


def test_multiple_operations_4():
    operations_old = ['deal into new stack\n',
                      'cut -2\n',
                      'deal with increment 7\n',
                      'cut 8\n',
                      'cut -4\n',
                      'deal with increment 7\n',
                      'cut 3\n',
                      'deal with increment 9\n',
                      'deal with increment 3\n',
                      'cut -1\n']

    operations = ['deal into new stack\n',
                  'cut -2\n',
                  'deal with increment 7\n',
                  'cut 8\n',
                  'cut -4\n',
                  'deal with increment 7\n',
                  'cut 3\n',
                  'deal with increment 9\n',
                  'deal with increment 3\n',
                  'cut -1\n']

    cs = CardShuffler(10)
    cs.perform(operations)

    assert_equal([9, 2, 5, 8, 1, 4, 7, 0, 3, 6], cs.deck)

    cs2 = CardShuffler2(10, 3)
    cs2.perform(operations)
    assert_equal(8, cs2.pos)

    operations.reverse()
    cs2.perform(operations, inverse=True)
    assert_equal(3, cs2.pos)


def test_solve_part_1():
    t = open('../resources/input_22.txt')
    lines = t.readlines()
    t.close()

    cs = CardShuffler(10007)
    cs.perform(lines)

    deck = cs.deck
    for i in range(len(deck)):
        if deck[i] == 2019:
            print('The position of card {} is {}.'.format(2019, i))

    cs2 = CardShuffler2(10007, 2019)
    cs2.perform(lines)
    assert_equal(7860, cs2.pos)

    cs3 = CardShuffler2(10007, 7860)

    lines.reverse()
    cs3.perform(lines, inverse=True)
    assert_equal(2019, cs3.pos)


def test_solve_part_1_with_tracking():
    t = open('../resources/input_22.txt')
    lines = t.readlines()
    t.close()

    cs = CardShuffler2(10007, 2019)
    cs.perform(lines)

    print('The position of card {} is {}.'.format(2019, cs.pos))


def test_solve_part_2():
    t = open('../resources/input_22.txt')
    lines = t.readlines()
    lines = list(map(lambda s: s.rstrip(), lines))
    t.close()
    n = 119315717514047

    coeffs = CardShufflerImproved.get_coeffs(n, lines, inverse=True)
    result = CardShufflerImproved.shuffle(n, 2020, coeffs, rounds=101741582076661)

    assert_equal(result, 61256063148970)
