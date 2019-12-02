def run_program(codes: [int], adjusted_codes: [int] = None) -> [int]:
    if adjusted_codes:
        for i in range(len(adjusted_codes)):
            codes[i + 1] = adjusted_codes[i]

    for i in range(len(codes))[::4]:
        if codes[i] != 99 and i + 4 < len(codes):
            command = Instruction(codes[i:i + 4])
            command.execute_on(codes)

    return codes


class Instruction:
    def __init__(self, command_segment: [int]) -> None:
        assert len(command_segment) == 4
        self.op_code = command_segment[0]
        self.param_1 = command_segment[1]
        self.param_2 = command_segment[2]
        self.param_3 = command_segment[3]

    def execute_on(self, codes: [int]) -> [int]:

        if self.op_code == 1:
            result = codes[self.param_1] + codes[self.param_2]
        elif self.op_code == 2:
            result = codes[self.param_1] * codes[self.param_2]
        else:
            raise Exception('Received invalid opcode: ' + str(self.op_code))

        codes[self.param_3] = result
        return codes
