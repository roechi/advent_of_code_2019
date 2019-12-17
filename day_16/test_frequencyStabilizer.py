from collections import deque
from functools import reduce
from unittest import TestCase

from nose.tools import assert_equal

from day_16.FrequencyStabilizer import FrequencyStabilizer


class TestFrequencyStabilizer(TestCase):
    def test_apply_phase(self):
        inp = [1, 2, 3, 4, 5, 6, 7, 8]


        fs = FrequencyStabilizer(inp)
        freq = fs.apply_phase(times=1)

        result = int(reduce(lambda x, y: str(x) + str(y), freq))
        assert_equal(result, 48226158)

        freq = fs.apply_phase(times=1)

        result = int(reduce(lambda x, y: str(x) + str(y), freq))
        assert_equal(result, 34040438)

        freq = fs.apply_phase(times=1)

        result = int(reduce(lambda x, y: str(x) + str(y), freq))
        assert_equal(result, 3415518)

        freq = fs.apply_phase(times=1)

        result = int(reduce(lambda x, y: str(x) + str(y), freq))
        assert_equal(result, 1029498)

    def test_apply_phase_large(self):
        inp = list(map(lambda x: int(x), '80871224585914546619083218645595'))

        fs = FrequencyStabilizer(inp)
        freq = fs.apply_phase(times=100)
        freq = freq[:8]
        result = int(reduce(lambda x, y: str(x) + str(y), freq))
        assert_equal(result, 24176176)

    def test_part_one(self):
        t = open('../resources/input_16.txt')
        lines = t.readlines()
        t.close()

        inpt_freq = list(map(lambda x: int(x), lines[0]))


        fs = FrequencyStabilizer(inpt_freq)
        freq = fs.apply_phase(times=100)
        freq = freq[:8]
        print('The first eight digits are: {}'.format(reduce(lambda n, m: str(n) + str(m), freq)))

    def test_part_two(self):
        t = open('../resources/input_16.txt')
        lines = t.readlines()
        t.close()
        num_str = lines[0]

        offset = int(num_str[:7])

        freq = [int(num) for _ in range(10000) for num in num_str][offset:]

        for _ in range(100):
            for i in range(2, len(freq) + 1):
                freq[-i] = (freq[-i + 1] + freq[-i]) % 10

        res = reduce(lambda x, y: str(x) + str(y), freq[:8])


        print('The first eight digits are: ' + res)

        assert_equal(res, '55078585')
