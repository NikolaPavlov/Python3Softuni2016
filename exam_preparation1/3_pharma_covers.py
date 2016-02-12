ERROR_MSG = 'INVALID INPUT'
w = input()
h = input()
d = input()
input_file = input()


def check_dimensions(list1, list2):
    if (list1[0] > list2[0] and list1[1] > list2[1] and list1[2] > list2[2]):
        return True


try:
    width = float(w)
    heigh = float(h)
    depth = float(d)

    box_dimensions = [width, heigh, depth]
    box_dimensions_sorted = sorted(box_dimensions)

    with open(input_file, encoding='utf-8') as f:
        for line in f:
            splited_line = line.strip().split(',')
            pharma_name = splited_line[0]
            pharma_dimensions = [float(splited_line[1]),
                                 float(splited_line[2]),
                                 float(splited_line[3])]
            pharma_dimensions_sorted = sorted(pharma_dimensions)
            if check_dimensions(box_dimensions_sorted, pharma_dimensions_sorted):
                print(pharma_name)
except:
    print(ERROR_MSG)
