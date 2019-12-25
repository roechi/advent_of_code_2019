from functools import reduce

from day_13.IntcodeComputer import IntcodeComputer


class SantaRescue:
    def __init__(self) -> None:
        t = open('resources/input_25.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))

        self.computer = IntcodeComputer(program)

    def run(self, command: str):
        encoded = SantaRescue.encode(command)

        mem, out, exit_code = self.computer.run_program(input=encoded, reset_memory=False,
                                                        reset_pointer=False, reset_relative_pointer=False)
        decoded = SantaRescue.decode(out)
        print(decoded)



    @staticmethod
    def decode(code: str):
        return reduce(lambda x, y: x + y, map(lambda x: str(chr(x)), code))

    @staticmethod
    def encode(code: str):
        return list(map(lambda x: ord(x), code))
