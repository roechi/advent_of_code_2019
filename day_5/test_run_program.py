from unittest import TestCase

from nose.tools import assert_equal

from day_5.IntcodeComputer import IntcodeComputer


class TestRun_program(TestCase):
    def test_run_program(self):
        inputs = [
            ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
            ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
            ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])
        ]

        for input_tuple in inputs:
            computer = IntcodeComputer(input_tuple[0])
            result = computer.run_program()
            assert_equal(result, input_tuple[1])

    def test_result_for_first_part(self):
        t = open('../resources/input_2.txt')
        lines = t.readlines()
        t.close()
        inputs = list(map(lambda x: int(x), lines[0].split(sep=',')))

        computer = IntcodeComputer(inputs)
        result = computer.run_program(parameters=[12,2])
        print('The value is: ' + str(result[0]))

    def test_result_for_second_part(self):
        expected_value = 19690720

        t = open('../resources/input_2.txt')
        lines = t.readlines()
        t.close()
        original_inputs = list(map(lambda x: int(x), lines[0].split(sep=',')))

        result = 0
        computer = IntcodeComputer(original_inputs)
        for i in range(100):
            for j in range(100):

                result = computer.run_program(parameters=[i, j])
                if result[0] == expected_value:
                    print('noun: ' + str(i) + ' verb: ' + str(j))
                    print('result is: ' + str(100 * i + j))
                    break
            if result[0] == expected_value:
                break

    def test_opcode_3(self):
        inputs = [3, 2, 0]
        expected_outputs = [3, 2, 99]

        computer = IntcodeComputer(inputs)
        outputs = computer.run_program(input=99)

        assert_equal(outputs, expected_outputs)

    def test_opcode_4(self):
        inputs = [4, 2, 99]

        computer = IntcodeComputer(inputs)
        computer.run_program()

    def test_result_for_part_one_day_5(self):
        t = open('../resources/input_5.txt')
        lines = t.readlines()
        t.close()
        original_inputs = list(map(lambda x: int(x), lines[0].split(sep=',')))

        computer = IntcodeComputer(original_inputs)
        computer.run_program(input=1)