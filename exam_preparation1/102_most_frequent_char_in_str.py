input_string = input()
input_txt = ''.join(list(input_string))


def most_freq_char(input_txt):
    if input_txt.isspace():
        return 'Invalid Input!!!'
    else:
        return max(set(input_txt), key=input_string.count)

print(most_freq_char(input_txt))
