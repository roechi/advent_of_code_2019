class IntcodeComputer:

    def __init__(self, memory: [int]) -> None:
        self.initial_memory = memory

    def run_program(self, parameters: [int] = None, input: int = None) -> [int]:
        memory = self.initial_memory.copy()

        if parameters:
            for i in range(len(parameters)):
                memory[i + 1] = parameters[i]

        instruction_pointer = 0

        while instruction_pointer < len(memory) - 1 and memory[instruction_pointer] != 99:
                instruction_pointer = self.execute(memory, instruction_pointer, input)

        return memory

    def execute(self, memory: [int], pointer: int, input: int = None) -> int:
        raw_op_code_with_modes = memory[pointer]
        op_code = int(str(memory[pointer])[-2:])

        if op_code == 1:
            param_1 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            memory[param_3] = param_1 + param_2
            return pointer + 4
        elif op_code == 2:
            param_1 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            memory[param_3] = param_1 * param_2
            return pointer + 4
        elif op_code == 3:
            memory[memory[pointer + 1]] = input
            return pointer + 2
        elif op_code == 4:
            param = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 1)
            print(param)
            return pointer + 2
        elif op_code == 5:
            if IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 1) != 0:
                pointer = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 2)
            else:
                pointer += 3
            return pointer
        elif op_code == 6:
            if IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 1) == 0:
                pointer = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 2)
            else:
                pointer += 3
            return pointer
        elif op_code == 7:
            param_1 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            if param_1 < param_2:
                memory[param_3] = 1
            else:
                memory[param_3] = 0
            return pointer + 4
        elif op_code == 8:
            param_1 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 1)
            param_2 = IntcodeComputer.get_param(memory, pointer, raw_op_code_with_modes, 2)
            param_3 = memory[pointer + 3]
            if param_1 == param_2:
                memory[param_3] = 1
            else:
                memory[param_3] = 0
            return pointer + 4
        elif op_code == 99:
            return pointer
        else:
            raise Exception('Received invalid opcode: ' + str(op_code))

    @staticmethod
    def get_param(memory, pointer, raw_op_code_with_modes, num_of_param):
        mode = IntcodeComputer.get_parameter_modes(raw_op_code_with_modes, num_of_param - 1)
        if mode == 0:
            param = memory[memory[pointer + num_of_param]]
        else:
            param = memory[pointer + num_of_param]
        return param

    @staticmethod
    def get_parameter_modes(op_code, requested_param_position):
        modes = list(map(lambda x: int(x), str(op_code)[::-1][2:]))
        if requested_param_position >= len(modes):
            return 0
        else:
            return modes[requested_param_position]

