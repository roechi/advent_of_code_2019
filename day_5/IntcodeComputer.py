class IntcodeComputer:

    def __init__(self, memory: [int]) -> None:
        self.initial_memory = memory

    def run_program(self, parameters: [int] = None, input: int = None) -> [int]:
        memory = self.initial_memory.copy()

        if parameters:
            for i in range(len(parameters)):
                memory[i + 1] = parameters[i]

        instruction_pointer = 0
        steps_to_next_instruction = 0
        while instruction_pointer < len(memory) - 1:
            instruction_pointer += steps_to_next_instruction
            if instruction_pointer + steps_to_next_instruction < len(memory) and memory[instruction_pointer] != 99:
                command = Instruction(instruction_pointer, memory, input)
                steps_to_next_instruction = command.execute_on(memory)

        return memory


class Instruction:
    def __init__(self, pointer: int, memory: [int], input: int = None) -> None:
        raw_opcode = memory[pointer]
        self.op_code = int(str(memory[pointer])[-2:])
        self.input = input
        if self.op_code == 3:
            self.param_1 = memory[pointer + 1]
        if self.op_code in [1, 2, 4]:
            mode = Instruction.get_parameter_modes(raw_opcode, 0)
            if mode == 0:
                self.param_1 = memory[memory[pointer + 1]]
            elif mode == 1:
                self.param_1 = memory[pointer + 1]
        if self.op_code in [1, 2]:
            mode = Instruction.get_parameter_modes(raw_opcode, 1)
            if mode == 0:
                self.param_2 = memory[memory[pointer + 2]]
            elif mode == 1:
                self.param_2 = memory[pointer + 2]
        if self.op_code in [1, 2]:
            self.param_3 = memory[pointer + 3]

    @staticmethod
    def get_parameter_modes(op_code, requested_param_position):
        modes = list(map(lambda x: int(x), str(op_code)[::-1][2:]))
        if requested_param_position >= len(modes):
            return 0
        else:
            return modes[requested_param_position]

    def execute_on(self, codes: [int]) -> [int]:

        if self.op_code == 1:
            result = self.param_1 + self.param_2
            codes[self.param_3] = result
            steps_to_next_instruction = 4
        elif self.op_code == 2:
            result = self.param_1 * self.param_2
            codes[self.param_3] = result
            steps_to_next_instruction = 4
        elif self.op_code == 3:
            result = self.input
            codes[self.param_1] = result
            steps_to_next_instruction = 2
        elif self.op_code == 4:
            print(self.param_1)
            steps_to_next_instruction = 2
        elif self.op_code == 99:
            steps_to_next_instruction = 0
        else:
            raise Exception('Received invalid opcode: ' + str(self.op_code))

        return steps_to_next_instruction
