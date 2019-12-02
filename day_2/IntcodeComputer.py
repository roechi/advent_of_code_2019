class IntcodeComputer:

    def __init__(self, memory: [int]) -> None:
        self.initial_memory = memory

    def run_program(self, parameters: [int] = None) -> [int]:
        memory = self.initial_memory.copy()

        if parameters:
            for i in range(len(parameters)):
                memory[i + 1] = parameters[i]

        for i in range(len(memory))[::4]:
            if memory[i] != 99 and i + 4 < len(memory):
                command = Instruction(memory[i:i + 4])
                command.execute_on(memory)

        return memory


class Instruction:
    def __init__(self, instruction_snippet: [int]) -> None:
        assert len(instruction_snippet) == 4
        self.op_code = instruction_snippet[0]
        self.param_1 = instruction_snippet[1]
        self.param_2 = instruction_snippet[2]
        self.param_3 = instruction_snippet[3]

    def execute_on(self, codes: [int]) -> [int]:

        if self.op_code == 1:
            result = codes[self.param_1] + codes[self.param_2]
        elif self.op_code == 2:
            result = codes[self.param_1] * codes[self.param_2]
        else:
            raise Exception('Received invalid opcode: ' + str(self.op_code))

        codes[self.param_3] = result
        return codes
