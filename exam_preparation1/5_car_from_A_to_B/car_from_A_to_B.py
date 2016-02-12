# TODO: WTF!!!
ERROR_MSG = 'INVALID INPUT'
# input_file = input()
# input_file = 'input_file.txt'
input_file = 'input_file2.txt'


total_time = 0
with open(input_file, encoding='utf-8') as f:
    for line in f:
        splited_line = line.strip().split(',')
        # print(splited_line)
        try:
            start_km = int(splited_line[0])
            end_km = int(splited_line[1])
            speed = float(splited_line[2])
            distance = float(end_km - start_km)
            print('distance: ' + str(distance))
            print('speed: ' + str(speed))
            time = distance / speed
            print('time:' + str(time))
            total_time += float(time)
            print('------------------------------')
        except:
            print(ERROR_MSG)
print(total_time)
