text = 'Wazzzzzuuuup bro haw ware youuuozw Zupppawazup ooo www zuuuppzup ' \
       'wupaz wupaz zoooo wzauuuuuppp ppppuz waz zaw upppzwaa uu zwa zwa'
words = 'wazup'
text1 = list(map(str.lower, filter(lambda x: len(x) > 5, text.split())))
text_str = ' '.join(text1)
for y in words:
    text1 = list(filter(lambda x:y in x, text1))
print(' '.join(text1))