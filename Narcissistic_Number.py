import math


def narcissistic(value):
    value_array = [int(x) for x in str(value)]
    power = len(value_array)
    value_sum = 0
    for i in value_array:
        value_sum = value_sum + (math.pow(i, power))

    if value == value_sum:
        return True
    else:
        return False


print(narcissistic(153))
