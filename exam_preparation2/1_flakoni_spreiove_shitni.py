import math


AREA_COVERAGE = 1.76
ERROR_MSG = 'INVALID INPUT'

width = input()
height = input()


try:
    w = float(width)
    h = float(height)
    area = w * h
    number_of_cans = math.ceil(area / AREA_COVERAGE)
    print(number_of_cans)
except:
    print(ERROR_MSG)
