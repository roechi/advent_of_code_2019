from day_13.IntcodeComputer import IntcodeComputer


class Arcade:
    def __init__(self, game: [int]) -> None:
        self.computer = IntcodeComputer(game)
        self.parameters = [2]
        self.screen = [[' ' for x in range(24)] for y in range(42)]

    def run(self, input: int = None):
        if self.parameters:
            param = list()
            param.append(self.parameters.pop())
        else:
            param = None
        if input is not None:
            inp = [input]
        else:
            inp = None

        hi_score = 0
        exit_code = 1

        while exit_code != 0:
            mem, out, exit_code = self.computer.run_program(parameters=[2], input=inp,
                                                            reset_memory=False, reset_pointer=False,
                                                            reset_relative_pointer=False)

            p = 0
            ball_x, bally = 0, 0
            pad_x, pad_y = 0, 0
            while p + 3 <= len(out):
                c = '~'
                if out[p + 2] == 0:
                    c = ' '
                elif out[p + 2] == 1:
                    c = '#'
                elif out[p + 2] == 2:
                    c = 'X'
                elif out[p + 2] == 3:
                    c = '-'
                    pad_x = out[p]
                    pad_y = out[p + 1]
                elif out[p + 2] == 4:
                    c = 'O'
                    ball_x = out[p]
                    ball_y = out[p + 1]
                else:
                    c = out[p + 2]

                x = out[p]
                y = out[p + 1]
                if x == -1 and y == 0:
                    hi_score = out[p + 2]
                else:
                    self.screen[x][y] = c
                p += 3

            if ball_x > pad_x:
                inp = [1]
            elif ball_x < pad_x:
                inp = [-1]
            else:
                inp = [0]
            print('Highscore: {}'.format(hi_score))
            self.print_screen(self.screen)

    def print_screen(self, screen):
        for y in range(len(screen[0])):
            line = ''
            for x in range(len(screen)):
                line += screen[x][y]
            print(line)
