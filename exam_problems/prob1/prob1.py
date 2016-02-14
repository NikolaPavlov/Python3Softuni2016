import sys
import math
import unittest


ERROR_MSG = 'INVALID INPUT'
FIRA = 0.098  # fira 9.8%
try:
    area = float(input())
    h = float(input())
    w = float(input())
    d = float(input())

    # area = 0.80
    # h = 1.23
    # w = 0.78
    # d = 0.50

    def calc_surface_of_rect_prism(h, w, d):
        if h <= 0 or w <= 0 or d <= 0:
            raise ValueError(ERROR_MSG)
        surface = 2 * (d*w + w*h + d*h)
        return surface

    if area <= 0 or h <= 0 or w <= 0 or d <= 0:
        sys.exit(ERROR_MSG)
    else:
        if __name__ == '__main__':
            surface_of_box = calc_surface_of_rect_prism(w, h, d)
            area_of_one_cover = area - (area * FIRA)
            print(math.ceil(surface_of_box / area_of_one_cover))
except:
    print(ERROR_MSG)


###############################################################################
class MyTest(unittest.TestCase):
    def test_calc_surface_or_rect_prism_1(self):
        self.assertAlmostEqual(calc_surface_of_rect_prism(1.23, 0.78, 0.50),
                               3.9288)

    def test_calc_surface_or_rect_prism_2(self):
        self.assertAlmostEqual(calc_surface_of_rect_prism(1.55, 0.78, 1.50),
                               9.408)

# unittest.main()
###############################################################################
