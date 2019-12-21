from day_21.SpringBot import SpringDroid


def test_run_spring_script_part_1():
    # !A || (!C && D)
    print('Part 1')
    sd = SpringDroid()
    sd.run_spring_script([
        'NOT A J\n',
        'NOT C T\n',
        'AND D T\n',
        'OR T J\n',
        'WALK\n'])

def test_run_spring_script_part_2():
    # !A || (!C && D && E) || (!C && D && H)) || (!B && !E)
    print('Part 2')
    sd = SpringDroid()
    sd.run_spring_script([
        'NOT A J\n',
        'NOT C T\n',
        'AND D T\n',
        'AND E T\n',
        'OR T J\n',
        'NOT C T\n',
        'AND D T\n',
        'AND H T\n',
        'OR T J\n',
        'NOT B T\n',
        'NOT T T\n',
        'OR E T\n',
        'NOT T T\n',
        'OR T J\n',
        'RUN\n'])
