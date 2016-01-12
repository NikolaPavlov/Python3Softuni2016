input_name = input()

titles_foreign = ['van', 'von']
titles_bg = ['доктор', 'др.', 'д-р.' 'професор', 'проф.']
split_input_name = input_name.split()
answers = ''

for name in split_input_name:
    if name in titles_bg:
        continue
    if name in titles_foreign:
        continue
    answers += (name[0] + '.')

print(answers)
