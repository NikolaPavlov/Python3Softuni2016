# filename_exchange_rates = input()  # exchange.txt
# filename_amounts = input()  # amounts.txt
filename_exchange_rates = 'exchange.txt'
filename_amounts = 'amounts.txt'

dict_rates = {}
with open(filename_exchange_rates, 'r', encoding='utf-8') as f:
    for line in f:
        splited_line = line.split()
        currency_name = splited_line[0]
        currency_change_value = splited_line[1]
        dict_rates[currency_name] = currency_change_value

dict_amounts = {}
test_answers = []
with open(filename_amounts, 'r', encoding='utf-8') as f:
    for line in f:
        splited_line = line.split()
        currency_name = splited_line[1]
        currency = splited_line[0]
        currency_value_in_bgn = currency * dict_rates[currency_name]
        test_answers.append(currency_value_in_bgn)

print(dict_rates)
print(dict_amounts)
print(test_answers)
