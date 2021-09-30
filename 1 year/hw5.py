with open('war_and_piece.txt', 'r', encoding = 'utf-8') as f:
	k = 0
	t = 0 
	lst = []
	rus = set('ячсмитьбюфывапролджэйцукенгшщзхъё')
	for line in f.readlines():
		k += 1
		if 'Анна Павловна' in line:
			line = line.replace('Анна Павловна', 'Anna Pavlovna')
		if 'Princesse, ma parole' in line:
			print(k, 'строка')
		trash = line.strip().split()
		lst += trash
	lst = list(map(str.lower, lst))
	print('В тексте', len(lst), 'слов')
	lst = list(filter(rus.intersection, map(lambda x: ''.join(c for c in x if c.isalpha()), lst)))
	amount_words = sum(map(len, lst))
	average_len = int((amount_words / len(lst)) * 10000) / 10000
	print('Кол-во букв', amount_words)
	print('Средняя длина слова', average_len)
	most_top_word = {}
	most_top_letter = {}
	top_10_words = {}
	top_10_letters = {}
	for elem in lst:
		if elem not in most_top_word.keys():
			most_top_word[elem] = 1
		else:
			most_top_word[elem] += 1
		for letter in elem:
			if letter not in most_top_letter.keys():
				most_top_letter[letter] = 1
			else:
				most_top_letter[letter] += 1


	most_word = sorted(most_top_word, key = most_top_word.__getitem__, reverse = True)[:10]
	most_letter = sorted(most_top_letter, key = most_top_letter.__getitem__, reverse = True)[:10]
	for elem in most_word:
		for k, v in most_top_word.items():
			if k == elem:
				top_10_words[k] = v

	for elem in most_letter:
		for k, v in most_top_letter.items():
			if k == elem:
				top_10_letters[k] = v

	print(list(top_10_words.items()))
	print(list(top_10_letters.items()))
