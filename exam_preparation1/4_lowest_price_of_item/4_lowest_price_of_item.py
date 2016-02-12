article = input()
input_file = input()


lowest_price = 9999999999999
lowest_price_city = ''
with open(input_file, encoding='utf-8') as f:
    for line in f:
        splited_line = line.strip().split(',')
        article_name = splited_line[0].strip('"')
        article_city = splited_line[2]
        article_price = float(splited_line[4])
        if article_name == article:
            if article_price < lowest_price:
                lowest_price = article_price
                lowest_price_city = article_city

print(lowest_price_city.strip('"'))
