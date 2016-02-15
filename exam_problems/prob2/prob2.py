import sys


ERROR_MSG = 'INVALID INPUT'
DIRECTIONS = ['left', 'right', 'up', 'down']

try:
    # input_file = input()
    input_file = 'steps.txt'
    current_cordinates = {'x': 0, 'y': 0}
    with open(input_file, encoding='utf-8') as f:
        for line in f:
            splited_line = line.strip().split()
            #  validation start -------------------
            if len(splited_line) == 0:
                continue

            if len(splited_line) != 2:
                sys.exit(ERROR_MSG)

            direction = splited_line[0]
            value_of_move = float(splited_line[1])

            if direction not in DIRECTIONS:
                sys.exit(ERROR_MSG)

            #  check if value_of_move is number
                # pass

            #  validation end -------------------
            if direction == 'left':
                current_cordinates['x'] -= value_of_move
            elif direction == 'right':
                current_cordinates['x'] += value_of_move
            elif direction == 'up':
                current_cordinates['y'] += value_of_move
            elif direction == 'down':
                current_cordinates['y'] -= value_of_move

    formated_x = '{:.3f}'.format(current_cordinates['x'])
    formated_y = '{:.3f}'.format(current_cordinates['y'])
    print('X ' + formated_x)
    print('Y ' + formated_y)
except:
    print(ERROR_MSG)
