try:
    exchange_file = input()
    amounts_file = input()

    exchange_dict = dict()
    with open(exchange_file, encoding='utf-8') as f:
        for line in f:
            exchange_dict[line.strip().split()[0]] = line.strip().split()[1]

    with open(amounts_file, encoding='utf-8') as f:
        for line in f:
            currency_quantity = line.strip().split()[0]
            currency_type = line.strip().split()[1]
            course = exchange_dict[currency_type]
            answer = float(currency_quantity) / float(course)
            print('{:.2f}'.format(answer))
except:
    print('error in input nakovvica mf!')
