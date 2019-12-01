"""
Calculate the fuel cost based on weight.

>>> fuel_calculation(0)
-2
>>> fuel_calculation(12)
2
>>> fuel_calculation(14)
2
>>> fuel_calculation(1969)
654
>>> fuel_calculation(100756)
33583

>>> additional_fuel_amount(2)
0
>>> additional_fuel_amount(654)
312
>>> additional_fuel_amount(33583)
16763



"""

from math import floor

def main():
    f = open("input/1.txt", "r")
    lines = f.readlines()
    weights = map(lambda x: int(x), lines)

    fuel_amounts = list(map(fuel_calculation, weights))

    naive_fuel_sum = sum(fuel_amounts)
    print(naive_fuel_sum)

    additional_fuel_amounts = map(additional_fuel_amount, fuel_amounts)
    print(naive_fuel_sum + sum(additional_fuel_amounts))

def fuel_calculation(weight):
    return floor(weight/3) - 2

def additional_fuel_amount(fuel_amount):
    additional_fuel = fuel_calculation(fuel_amount)
    if additional_fuel <= 0:
        return 0
    else:
        return additional_fuel + additional_fuel_amount(additional_fuel)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
