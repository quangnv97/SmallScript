def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def makeBeauty(file_path):
	list_post = list()
	text = ""
	with open(file_path, 'r') as file:
		text = file.read()
		list_pos = findOccurrences(text,';')

	with open("output.txt", 'w') as file:
		for i in range(len(list_pos)):
			tmp = list_pos[i]+i+1
			text = text[:tmp] + "\n" + text[tmp:]
		file.write(text)
