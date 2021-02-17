with open ('db2.txt','r', encoding = 'utf-8') as f:
    text = f.read().splitlines()
    text = set(text)
    text = list(text)
    russian_numbers = []
    for i in range(len(text)):
        text[i] = text[i].split('\t')
    for user in text:
        number = user[2]
        if not number.startswith('+'):
            number = '+' + number
        if number.startswith('+7 ') or number.startswith('8 '):
            russian_numbers.append(number)
        number = number.replace(' ', '')
        number = number.replace('(', '')
        number = number.replace(')', '')
        number = number.replace('-', '')
        user[2] = number
    same_ips = []
    #print(text)
    #print(russian_numbers)
    print(same_ips)
