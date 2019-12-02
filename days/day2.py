from itertools import product

def parse_input(f):
    return list(map(int, f.read().split(',')))

def solve(initial_program):
    prepared_program = apply_noun_verb(initial_program, 12, 2)
    test_program = run_program(prepared_program, 0)

    input_pair = search_for_output(initial_program, 19690720)


    return [get_output(test_program), format_answer2(input_pair)]

def get_output(program):
    return program[0]

def format_answer2(pair):
    return pair[0]*100 + pair[1]


def apply_noun_verb(initial_program, noun, verb):
    """ Applies noun verb to program

        >>> [1,2,3,4]
        [1,12,2,4]
        >>> [5,5,5,5]
        [5,12,2,5]
    """
    return initial_program[:1] + [noun,verb] + initial_program[3:]

def run_program(program, opcode_pos):
    """ Runs a supplide Intcode program.

        >>> run_program([1,0,0,0,99])
        [2,0,0,0,99]
    """

    opcode = program[opcode_pos]

    if opcode == 99:
        return program

    operand1 = program[program[opcode_pos + 1]]
    operand2 = program[program[opcode_pos + 2]]
    target   = program[opcode_pos + 3]

    new_program = list(program)

    if opcode == 1:
        new_program[target] = operand1 + operand2
    elif opcode == 2:
        new_program[target] = operand1 * operand2
    else:
        raise BaseException("Unknown opcode")

    return run_program(new_program, opcode_pos + 4)

def search_for_output(initial_program, desired_output):
    pairs = product(range(100), range(100))

    pair_program_gen = ([pair, apply_noun_verb(initial_program, *pair)] for pair in pairs)

    output_gen = ([pair, get_output(run_program(program, 0))] for pair, program in pair_program_gen)

    winner_pairs_gen = (pair for pair, output in output_gen if output == desired_output)

    return next(winner_pairs_gen)



