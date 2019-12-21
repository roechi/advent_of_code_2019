from functools import reduce

from day_13.IntcodeComputer import IntcodeComputer

class SpringDroid:

    def __init__(self) -> None:
        t = open('../resources/input_21.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))
        self.computer = IntcodeComputer(program)

    def run_spring_script(self, spring_script: [str]):
        mem, out, exit_code = self.computer.run_program()

        print(SpringDroid.decode(out))
        for line in spring_script:
            int_code = SpringDroid.encode(line)
            mem, out, exit_code = self.computer.run_program(input=int_code, reset_memory=False, reset_pointer=False, reset_relative_pointer=False)
        if exit_code == 1:
            print(SpringDroid.decode(out))
        else:
            print('{}{}'.format(SpringDroid.decode(out[:-1]), out[-1]))

    @staticmethod
    def decode(code: str):
        return reduce(lambda x, y: x + y, map(lambda x: str(chr(x)), code))

    @staticmethod
    def encode(code: str):
        return list(map(lambda x: ord(x), code))


