import sys
import days.day1
import days.day2

def main(argv):
    problem_no = int(argv[0])

    if problem_no == 1:
        f = open("input/1.txt", "r")
        input = days.day1.parse_input(f)
        results = days.day1.solve(input)
    elif problem_no == 2:
        f = open("input/2.txt", "r")
        input = days.day2.parse_input(f)
        results = days.day2.solve(input)
    else:
        raise "Unknown problem"



    print(f"Problem 1: {results[0]}")
    print(f"Problem 2: {results[1]}")



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(sys.argv[1:])
