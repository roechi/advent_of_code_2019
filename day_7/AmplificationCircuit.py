from day_7.IntcodeComputer import IntcodeComputer


class AmplificationCircuit:

    def __init__(self, num_amplifiers: int, program: [int]) -> None:
        self.num_amplifiers = num_amplifiers
        self.computers = list()
        for i in range(num_amplifiers):
            self.computers.append(IntcodeComputer(program))

    def find_best_phase_settings(self):
        permutations = AmplificationCircuit.get_permutations([0, 1, 2, 3, 4])
        current_best_signal = 0
        current_best_phase_setting = []

        for p in permutations:
            signal = self.amplify(p)

            if signal > current_best_signal:
                current_best_signal = signal
                current_best_phase_setting = p

        return current_best_phase_setting, current_best_signal

    def find_best_phase_settings_feedback(self):
        permutations = AmplificationCircuit.get_permutations([5, 6, 7, 8, 9])
        current_best_signal = 0
        current_best_phase_setting = []

        for p in permutations:
            for c in self.computers:
                c.reset()

            signal = self.amplify_with_feedback(p)

            if signal > current_best_signal:
                current_best_signal = signal
                current_best_phase_setting = p

        return current_best_phase_setting, current_best_signal

    def amplify(self, phase_sequence: [int]):
        signal = 0
        current_computer = 0
        for p in phase_sequence:
            memory, output, exit_code = self.computers[current_computer].run_program(input=[p, signal])
            self.last_exit_code = exit_code
            signal = output[0]
            current_computer += 1

        return signal

    def amplify_with_feedback(self, phase_sequence: [int]):
        phase_inputs = phase_sequence.copy()
        last_exit_codes = [1 for i in range(len(self.computers))]

        signal = 0
        current_computer = 0

        while last_exit_codes != [0 for i in range(len(self.computers))]:
            if last_exit_codes[current_computer]:
                if phase_inputs:
                    memory, output, exit_code = self.computers[current_computer].run_program(input=[phase_inputs.pop(0), signal], reset_memory=False, reset_pointer=False)
                else:
                    memory, output, exit_code = self.computers[current_computer].run_program(input=[signal], reset_memory=False, reset_pointer=False)
                if not exit_code:
                    print('Computer ' + str(current_computer) + ' has halted.')
                last_exit_codes[current_computer] = exit_code
                if output:
                    signal = output[0]
                    print('Output: ' + str(signal))
            current_computer += 1
            if current_computer >= len(self.computers):
                current_computer = 0

        return signal

    @staticmethod
    def get_permutations(lst):
        if len(lst) == 0:
            return []

        if len(lst) == 1:
            return [lst]

        l = []

        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i + 1:]
            for p in AmplificationCircuit.get_permutations(remLst):
                l.append([m] + p)
        return l
