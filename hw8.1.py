import requests
from bs4 import BeautifulSoup
data = []

base1 = (line.replace('\n', '').split(';') for line in open('8_ABC.csv', 'r', encoding='utf-8'))
base2 = (line.replace('\n', '').split(';') for line in open('9_ABC.csv', 'r', encoding='utf-8'))
base1 = (line for line in base1 if 'Республика Татарстан' in line[-1])
base2 = (line for line in base2 if 'Республика Татарстан' in line[-1])
for i in range(1,10): # i - кол-во страниц
    link = f'https://kazan.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={i}&region=4777&room1=1&room2=1'
    page = requests.get(link).text
    soup = BeautifulSoup(page, 'lxml')
    results = soup.find_all("article", class_ = '_93444fe79c--container--2pFUD _93444fe79c--cont--1Ddh2')

    for ad in results:
        y = [''.join(ad.findChild('div', class_ = '_93444fe79c--labels--1J6M3').text.split(', ')[2]),
             ''.join(ad.findChild('span', class_ = '_93444fe79c--color_primary_100--O6-gZ _9'
             '3444fe79c--lineHeight_28px--3QLml _93444fe79c--fontWeight_bold--t3Ars '
             '_93444fe79c--fontSize_22px--3UVPd _93444fe79c--display_block--1eYsq _9'
             '3444fe79c--text--2_SER').text.split(', ')[-1]).partition('/')[0],
             ad.findChild('span', class_ = '_93444fe79c--color_black_100--A_xYw _9344'
             '4fe79c--lineHeight_28px--3QLml _93444fe79c--fontWeight_bold--t3Ars _9344'
             '4fe79c--fontSize_22px--3UVPd _93444fe79c--display_block--1eYsq _93444fe7'
             '9c--text--2_SER').text.replace('\xa0₽', ''),
             ad.findChild('p', class_ = '_93444fe79c--color_gray60_100--3VLtJ _93444fe'
             '79c--lineHeight_20px--2dV2a _93444fe79c--fontWeight_normal--2G6_P _93444f'
             'e79c--fontSize_14px--10R7l _93444fe79c--display_block--1eYsq _93444fe79c-'
             '-text--2_SER').text.replace('\xa0₽/м²', ''),
             ad.findChild('span', class_ = '_93444fe79c--text--2P6bT').text]
        if x := ad.findChild('div', class_='_93444fe79c--label--1VdtZ _93444fe79c--success--39_XW'):
            y.append(x.text)
        if not y[1].isdigit():
             y[1] = ''.join(ad.findChild('div', class_='_93444fe79c--subtitle--iGb0_')
                            .findChild('span').text.split(', ')[2].partition('/')[0])
        y[1] = int(y[1])
        y[2] = int(y[2].replace(' ',''))
        y[3] = int(y[3].replace(' ', ''))
        y[4] = y[4].replace('-', '').replace(' ','')
        data.append(tuple(y))
print(data)
data = filter(lambda x: (x[2]<=6_000_000) and (x[3]>120_000) and
             ((x[0] != 'р-н Ново-Савиновский') and (x[0] != 'р-н Вахитовский'))
             and (x[1] > 15) and (x[-1] == 'Застройщик') and ((int(line[0])==int(x[4][2:5]))
             and (int(line[1]) < int(x[4][5:10])*100) and (int(line[2]) > int(x[4][5:10])*100)
             for line in base1), data)
print(list(data))
