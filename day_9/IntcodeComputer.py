class IntcodeComputer:

    def __init__(self, program: [int]) -> None:
        self.initial_memory = program.copy()
        self.initial_memory.extend(0 for i in range(100 * len(program)))
        self.memory = program.copy()
        self.memory.extend(0 for i in range(100 * len(program)))
        self.instruction_pointer = 0
        self.relative_pointer = 0

    def reset(self):
        self.memory = self.initial_memory.copy()
        self.instruction_pointer = 0
        self.relative_pointer = 0

    def run_program(self, parameters: [int] = None, input: [int] = None, reset_memory: bool = True,
                    reset_pointer: bool = True, reset_relative_pointer: bool = True) -> [int]:
        if reset_memory:
            self.memory = self.initial_memory.copy()
        if reset_pointer:
            self.instruction_pointer = 0
        if reset_relative_pointer:
            self.relative_pointer = 0

        exit_code = 1
        output = []
        if parameters:
            for i in range(len(parameters)):
                self.memory[i + 1] = parameters[i]

        try:
            while self.instruction_pointer < len(self.memory) - 1 and self.memory[self.instruction_pointer] != 99:
                self.instruction_pointer = self.execute(self.memory, self.instruction_pointer, input, output)
        except AwaitingInput:
            pass

        if self.memory[self.instruction_pointer] == 99:
            exit_code = 0

        return self.memory, output, exit_code

    def execute(self, memory: [int], pointer: int, input: [int] = None, output: [int] = None) -> int:
        raw_op_code_with_modes = memory[pointer]
        op_code = int(str(memory[pointer])[-2:])

        if op_code == 1:
            relative_shift = 0
            if str(raw_op_code_with_modes)[0] == '2' and len(str(raw_op_code_with_modes)) > 4:
                relative_shift = self.relative_pointer

            param_1 = self.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = self.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            memory[param_3 + relative_shift] = param_1 + param_2
            return pointer + 4
        elif op_code == 2:
            relative_shift = 0
            if str(raw_op_code_with_modes)[0] == '2' and len(str(raw_op_code_with_modes)) > 4:
                relative_shift = self.relative_pointer

            param_1 = self.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = self.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            memory[param_3 + relative_shift] = param_1 * param_2
            return pointer + 4
        elif op_code == 3:
            relative_shift = 0
            if str(raw_op_code_with_modes)[0] == '2' and len(str(raw_op_code_with_modes)) > 2:
                relative_shift = self.relative_pointer

            if not input:
                raise AwaitingInput
            param = input.pop(0)
            memory[memory[pointer + 1] + relative_shift] = param
            return pointer + 2
        elif op_code == 4:
            param = self.get_param(memory, pointer, raw_op_code_with_modes, 1)
            output.append(param)
            return pointer + 2
        elif op_code == 5:
            if self.get_param(memory, pointer, raw_op_code_with_modes, 1) != 0:
                pointer = self.get_param(memory, pointer, raw_op_code_with_modes, 2)
            else:
                pointer += 3
            return pointer
        elif op_code == 6:
            if self.get_param(memory, pointer, raw_op_code_with_modes, 1) == 0:
                pointer = self.get_param(memory, pointer, raw_op_code_with_modes, 2)
            else:
                pointer += 3
            return pointer
        elif op_code == 7:
            relative_shift = 0
            if str(raw_op_code_with_modes)[0] == '2' and len(str(raw_op_code_with_modes)) > 4:
                relative_shift = self.relative_pointer

            param_1 = self.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = self.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            if param_1 < param_2:
                memory[param_3 + relative_shift] = 1
            else:
                memory[param_3 + relative_shift] = 0
            return pointer + 4
        elif op_code == 8:
            relative_shift = 0
            if str(raw_op_code_with_modes)[0] == '2' and len(str(raw_op_code_with_modes)) > 4:
                relative_shift = self.relative_pointer

            param_1 = self.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = self.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            if param_1 == param_2:
                memory[param_3 + relative_shift] = 1
            else:
                memory[param_3 + relative_shift] = 0
            return pointer + 4
        elif op_code == 9:
            param_1 = self.get_param(memory, pointer, raw_op_code_with_modes, 1)
            self.relative_pointer += param_1
            return pointer + 2
        elif op_code == 99:
            return pointer
        else:
            raise Exception('Received invalid opcode: ' + str(op_code))

    def get_param(self, memory, pointer, raw_op_code_with_modes, num_of_param):
        mode = IntcodeComputer.get_parameter_modes(raw_op_code_with_modes, num_of_param - 1)
        if mode == 0:
            param = memory[memory[pointer + num_of_param]]
        elif mode == 1:
            param = memory[pointer + num_of_param]
        elif mode == 2:
            param = memory[memory[pointer + num_of_param] + self.relative_pointer]
        else:
            raise Exception('Received invalid param mode: {}'.format(mode))
        return param

    @staticmethod
    def get_parameter_modes(op_code, requested_param_position):
        modes = list(map(lambda x: int(x), str(op_code)[::-1][2:]))
        if requested_param_position >= len(modes):
            return 0
        else:
            return modes[requested_param_position]


class AwaitingInput(Exception):
    pass
