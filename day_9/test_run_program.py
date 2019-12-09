from unittest import TestCase

from nose.tools import assert_equal

from day_7.AmplificationCircuit import AmplificationCircuit
from day_9.IntcodeComputer import IntcodeComputer


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
            result = computer.run_program()[0]
            assert_equal(result, input_tuple[1])

    def test_result_for_first_part(self):
        t = open('../resources/input_2.txt')
        lines = t.readlines()
        t.close()
        inputs = list(map(lambda x: int(x), lines[0].split(sep=',')))

        computer = IntcodeComputer(inputs)
        result = computer.run_program(parameters=[12, 2])[0]
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

                result = computer.run_program(parameters=[i, j])[0]
                if result[0] == expected_value:
                    print('noun: ' + str(i) + ' verb: ' + str(j))
                    print('result is: ' + str(100 * i + j))
                    break
            if result[0] == expected_value:
                break

    def test_opcode_3(self):
        inputs = [3, 2, 0]
        expected_memory = [3, 2, 99]

        computer = IntcodeComputer(inputs)
        outputs = computer.run_program(input=[99])[0]

        assert_equal(outputs, expected_memory)

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
        computer.run_program(input=[1])

    def test_compare(self):
        ### manual testing of various programs, check printed output to verify

        inputs = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
            1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
            999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        computer = IntcodeComputer(inputs)
        computer.run_program(input=[100])

    def test_result_for_part_two_day_five(self):
        t = open('../resources/input_5.txt')
        lines = t.readlines()
        t.close()
        original_inputs = list(map(lambda x: int(x), lines[0].split(sep=',')))
        computer = IntcodeComputer(original_inputs)
        computer.run_program(input=[5])

    def test_thruster_config_1(self):
        phase_sequence = [4, 3, 2, 1, 0]
        expected_result = 43210
        program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]

        circuit = AmplificationCircuit(5, program)
        signal = circuit.amplify(phase_sequence)

        assert_equal(signal, expected_result)

    def test_thruster_config_2(self):
        phase_sequence = [0, 1, 2, 3, 4]
        expected_result = 54321
        program = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
                   101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]

        circuit = AmplificationCircuit(5, program)
        signal = circuit.amplify(phase_sequence)

        assert_equal(signal, expected_result)

    def test_thruster_config_3(self):
        phase_sequence = [1, 0, 4, 3, 2]
        expected_result = 65210
        program = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
                   1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]

        circuit = AmplificationCircuit(5, program)
        signal = circuit.amplify(phase_sequence)

        assert_equal(signal, expected_result)

    def test_thruster_config_4(self):
        phase_sequence = [9, 8, 7, 6, 5]
        expected_result = 139629729
        program = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                   27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]

        circuit = AmplificationCircuit(5, program)
        signal = circuit.amplify_with_feedback(phase_sequence)

        assert_equal(signal, expected_result)

    def test_thruster_config_5(self):
        phase_sequence = [9, 7, 8, 5, 6]
        expected_result = 18216
        program = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                   -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                   53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]

        circuit = AmplificationCircuit(5, program)
        signal = circuit.amplify_with_feedback(phase_sequence)

        assert_equal(signal, expected_result)

    def test_result_part_one_day_seven(self):
        t = open('../resources/input_7.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))

        circuit = AmplificationCircuit(5, program)
        best_setting, best_signal = circuit.find_best_phase_settings()
        print('The highest possible signal is: ' + str(best_signal))

    def test_result_part_two_day_seven(self):
        t = open('../resources/input_7.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))

        circuit = AmplificationCircuit(5, program)
        best_setting, best_signal = circuit.find_best_phase_settings_feedback()
        print('The highest possible signal with feedback is: ' + str(best_signal))

    def test_result_part_one_day_nine(self):
        t = open('../resources/input_9.txt')
        lines = t.readlines()
        t.close()
        original_inputs = list(map(lambda x: int(x), lines[0].split(sep=',')))
        computer = IntcodeComputer(original_inputs)

        output = computer.run_program(input=[1])[1]
        print('Result: {}'.format(output))
        assert_equal(output, [3409270027])

    def test_result_part_two_day_nine(self):
        t = open('../resources/input_9.txt')
        lines = t.readlines()
        t.close()
        original_inputs = list(map(lambda x: int(x), lines[0].split(sep=',')))
        computer = IntcodeComputer(original_inputs)

        output = computer.run_program(input=[2])[1]
        print('Resulting coordinates of the distress signal: {}'.format(output))

    def test_opcode_9_and_relative(self):
        program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        computer = IntcodeComputer(program)
        print(computer.run_program()[1])

    def test_opcode_9_and_relative_2(self):
        program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        computer = IntcodeComputer(program)
        print(computer.run_program()[1])

    def test_opcode_9_and_relative_3(self):
        program = [104, 1125899906842624, 99]
        computer = IntcodeComputer(program)
        print(computer.run_program()[1])

