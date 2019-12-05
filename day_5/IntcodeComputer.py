class IntcodeComputer:

    def __init__(self, memory: [int]) -> None:
        self.initial_memory = memory

    def run_program(self, parameters: [int] = None) -> [int]:
        memory = self.initial_memory.copy()

        if parameters:
            for i in range(len(parameters)):
                memory[i + 1] = parameters[i]

        instruction_pointer = 0
        steps_to_next_instruction = 0
        while instruction_pointer < len(memory) -1:
            instruction_pointer += steps_to_next_instruction
            if instruction_pointer + steps_to_next_instruction < len(memory) and memory[instruction_pointer] != 99:
                command = Instruction(memory[instruction_pointer:instruction_pointer + 4])
                steps_to_next_instruction = command.execute_on(memory)

        return memory


class Instruction:
    def __init__(self, instruction_snippet: [int]) -> None:
        assert len(instruction_snippet) >= 1
        self.op_code = instruction_snippet[0]
        if self.op_code in [1, 2, 3]:
            self.param_1 = instruction_snippet[1]
            self.param_2 = instruction_snippet[2]
        if self.op_code in [1, 2]:
            self.param_3 = instruction_snippet[3]

    def execute_on(self, codes: [int]) -> [int]:

        if self.op_code == 1:
            result = codes[self.param_1] + codes[self.param_2]
            codes[self.param_3] = result
            steps_to_next_instruction = 4
        elif self.op_code == 2:
            result = codes[self.param_1] * codes[self.param_2]
            codes[self.param_3] = result
            steps_to_next_instruction = 4
        elif self.op_code == 3:
            result = codes[self.param_1]
            codes[self.param_2] = result
            steps_to_next_instruction = 3
        elif self.op_code == 4:
            print(codes[self.param_1])
            steps_to_next_instruction = 2
        elif self.op_code == 99:
            steps_to_next_instruction = 0
        else:
            raise Exception('Received invalid opcode: ' + str(self.op_code))

        return steps_to_next_instruction
