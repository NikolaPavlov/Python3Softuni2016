import math


a = input()
b = input()
c = input()


def calc_area_of_triangele(a, b, c):
    p = (float(a) + float(b) + float(c)) / 2
    area = math.sqrt(p * (p - float(a)) * (p - float(b)) * (p - float(c)))
    return '{:.2f}'.format(area)

try:
    print(calc_area_of_triangele(a, b, c))
except:
    print('Invalid input mf!!!')
