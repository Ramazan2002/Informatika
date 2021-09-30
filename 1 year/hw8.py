from bs4 import BeautifulSoup
data = []
tatarstan = []
with open('page.html', 'r', encoding='utf-8') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    data = list(tuple(ad.h5.text.split(', ') + [ad.findChild('div', class_='mobile-number').text])
            for ad in soup.find_all('div', class_='apartament'))
    base1 = (line.replace('\n', '').split(';') for line in open('8_ABC.csv', 'r', encoding='utf-8'))
    base2 = (line.replace('\n', '').split(';') for line in open('9_ABC.csv', 'r', encoding='utf-8'))
    base1 = (line for line in base1 if 'Республика Татарстан' in line[-1])
    base2 = (line for line in base2 if 'Республика Татарстан' in line[-1])
    for line in base1:
        tatarstan += [ad for ad in data if ((int(ad[-1][4:7]) == int(line[0])) and
                    (int(ad[-1][9:]) >= int(line[1])) and (int(ad[-1][9:]) <= int(line[2])))]
    for line in base2:
        tatarstan += [ad for ad in data if ((int(ad[-1][4:7]) == int(line[0])) and
                    (int(ad[-1][9:]) >= int(line[1])) and (int(ad[-1][9:]) <= int(line[2])))]
    result = (ad for ad in tatarstan if (int(ad[2].partition('/')[0]) >= 3 and
              int(ad[2].partition('/')[0]) <= 15 and float(ad[1].partition(' ')[0])>=45 and
              float(ad[1].partition(' ')[0])<=65) and ad[0] == '3-комн. кв.')
with open('result.txt', 'w', encoding='utf-8') as f:
    for e in result:
        print(', '.join(e), file=f)