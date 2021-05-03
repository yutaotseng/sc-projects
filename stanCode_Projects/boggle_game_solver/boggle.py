"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variables
DICTIONARY = {}  # The dictionary that could be used to determine whether the word exist.
BOGGLE_DIC = {}  # The dictionary that contains coordinate(key) and its corresponding letter(value).
ANS_LST = []  # The list that stores all the ans.


def main():
	"""
	TODO:
	"""
	read_dictionary()
	enter_row()
	boggle()
	print(f'There are {len(ANS_LST)} words in total.')


def boggle():
	for key in BOGGLE_DIC:
		(x, y) = key
		ans_coordinate = [(x, y)]
		boggle_helper(x, y, BOGGLE_DIC[(x, y)], ans_coordinate)


def boggle_helper(x, y, ans, ans_coordinate):
	for i in range(-1, 2, 1):  # in order to find neighbor pixel
		for j in range(-1, 2, 1):  # in order to find neighbor pixel
			if 0 <= x + i < 4:
				if 0 <= y + j < 4:
					if (x + i, y + j) not in ans_coordinate:
						if ans in DICTIONARY and ans not in ANS_LST:
							ANS_LST.append(ans)
							print(f'Found: "{ans}"')
						# Choose
						ans_coordinate.append((x + i, y + j))
						ans += BOGGLE_DIC[(x + i, y + j)]
						# Explore
						if has_prefix(ans):
							boggle_helper(x + i, y + j, ans, ans_coordinate)
						# Un-choose
						ans_coordinate.pop()
						ans = ans[:len(ans) - 1]


def enter_row():
	global BOGGLE_DIC
	letter_lst = []
	while True:
		if len(letter_lst) == 4:
			break
		else:
			row = input(f'{len(letter_lst) + 1} row of letters: ')
			row = row.lower()
			row = row.split()
			if row_letter_check(row):
				letter_lst.append(row)
	# Convert list into dictionary
	for i in range(len(letter_lst)):
		for j in range(len(letter_lst[i])):
			BOGGLE_DIC[i, j] = letter_lst[i][j]


def row_letter_check(row):
	if not len(row) == 4:
		print('Illegal Format!!!')
		return False
	for letter in row:
		if not letter.isalpha() or not len(letter) == 1:
			print('Illegal Format!!!')
			return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			if len(line) > 4:
				DICTIONARY[(line.strip())] = 1
	return DICTIONARY


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in DICTIONARY:
		if word.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
