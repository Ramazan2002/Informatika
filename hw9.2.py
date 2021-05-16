from bs4 import BeautifulSoup
from multiprocessing import Pool, Manager
from functools import partial
from time import time



def for_bases(tatarstan, data, line):
    tatarstan += [ad for ad in data if ((int(ad[-1][4:7]) == int(line[0])) and
                 (int(ad[-1][9:]) >= int(line[1])) and (int(ad[-1][9:]) <= int(line[2])))]

if __name__ == "__main__":
    z = time()
    with open('page.html', 'r', encoding='utf-8') as f:
        data = Manager().list()
        tatarstan = Manager().list()
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')
        data = list(tuple(ad.h5.text.split(', ') + [ad.findChild('div', class_='mobile-number').text])
                    for ad in soup.find_all('div', class_='apartament'))
        base1 = (line.replace('\n', '').split(';') for line in open('8_ABC.csv', 'r', encoding='utf-8'))
        base2 = (line.replace('\n', '').split(';') for line in open('9_ABC.csv', 'r', encoding='utf-8'))
        base1 = (line for line in base1 if 'Республика Татарстан' in line[-1])
        base2 = (line for line in base2 if 'Республика Татарстан' in line[-1])
        pool1 = Pool(1)
        pool2 = Pool(1)
        x = partial(for_bases, tatarstan, data)
        pool1.map(x, base1)
        pool2.map(x, base2)
        result = (ad for ad in tatarstan if (int(ad[2].partition('/')[0]) >= 3 and
                  int(ad[2].partition('/')[0]) <= 15 and float(
                  ad[1].partition(' ')[0]) >= 45 and
                  float(ad[1].partition(' ')[0]) <= 65) and ad[0] == '3-комн. кв.')
        with open('result1.txt', 'w', encoding='utf-8') as f:
            for e in result:
                print(', '.join(e), file=f)
        y = time()
        print(y - z)
        pool1.close()
        pool2.close()
        pool1.join()
        pool2.join()