"""
File: boggle.py
Name: Luna
----------------------------------------
This programme finds all words for Boggle game.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	The programme requires users to input a total of 16 letters (case-insensitive) by a fixed format:4 rows,
	4 letters for each row, split by space. And the programme finds all possible words spelled by the letters input.
	"""
	dictionary = []
	read_dictionary(FILE, dictionary)

	boggle = {}
	for i in range(4):
		letters = input(str(i + 1)+' row of letters: ')
		# check format
		if len(letters) == 7:
			if letters[0].isalpha() and letters[2].isalpha() and letters[4].isalpha() and letters[6].isalpha() and \
					letters[1] == ' ' and letters[3] == ' ' and letters[5] == ' ':
				boggle[i + 1] = letters.lower().split(' ')
			else:
				print('Illegal input')
				break
		else:
			print('Illegal input')
			break

	start = time.time()

	dictionary_excerpt = []
	write_dictionary_excerpt(boggle, dictionary, dictionary_excerpt)

	words_found = []
	for i in range(4):
		for j in range(4):
			find_words(boggle, '', words_found, dictionary_excerpt, i + 1, j)

	print('There are ', len(words_found), 'words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(boggle, current_word, words_found, dictionary_excerpt, row, index):
	"""
	This function finds all words spelled by letters in boggle.
	:param boggle: a dictionary which stores all letters input by user
	:param current_word: str, possible word to check
	:param words_found: a list of all word(s) found
	:param dictionary_excerpt: a list of excerpted words from dictionary
	:param row: int, row in boggle
	:param index: int, index in a row of boggle
	:return: this function does not return anything
	"""
	if len(current_word) >= 4:
		if current_word in dictionary_excerpt and current_word not in words_found:
			words_found.append(current_word)
			print(f'Found "{current_word}"')
		if 1 <= row <= 4 and 0 <= index <= 3:
			if boggle[row][index] is not '#':
				# choose
				current_word += boggle[row][index]
				temp = boggle[row][index]
				boggle[row][index] = '#'
				# explore
				if not has_prefix(current_word, dictionary_excerpt):
					pass
				else:
					find_words(boggle, current_word, words_found, dictionary_excerpt, row - 1, index - 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row - 1, index)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row - 1, index + 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row, index - 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row, index + 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row + 1, index - 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row + 1, index)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row + 1, index + 1)
				# un-choose
				current_word = current_word[:len(current_word) - 1]
				boggle[row][index] = temp
	else:
		if 1 <= row <= 4 and 0 <= index <= 3:
			if boggle[row][index] is not '#':
				# choose
				current_word += boggle[row][index]
				temp = boggle[row][index]
				boggle[row][index] = '#'
				# explore
				if not has_prefix(current_word, dictionary_excerpt):
					pass
				else:
					find_words(boggle, current_word, words_found, dictionary_excerpt, row - 1, index - 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row - 1, index)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row - 1, index + 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row, index - 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row, index + 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row + 1, index - 1)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row + 1, index)
					find_words(boggle, current_word, words_found, dictionary_excerpt, row + 1, index + 1)
				# un-choose
				current_word = current_word[:len(current_word) - 1]
				boggle[row][index] = temp


def write_dictionary_excerpt(boggle, dictionary, dictionary_excerpt):
	"""
	This function is to excerpt the dictionary list.
	Only words spelled by only letters stored in boggle will be appended to the dictionary_excerpt list.
	:param boggle: a dictionary which stores all letters input by user
	:param dictionary: a list made by the file of dictionary
	:param dictionary_excerpt: a list of excerpted words from dictionary
	:return: this function does not return anything
	"""
	letters_boggle = []
	for key in boggle:
		letters = boggle[key]
		for letter in letters:
			letters_boggle.append(letter)
	for word in dictionary:
		if 4 <= len(word) <= 16 and all_in_boggle(word, letters_boggle):
			dictionary_excerpt.append(word)


def all_in_boggle(s, letters_boggle):
	"""
	This function is to check if a word is spelled by only letters in boggle.
	:param s: (str) a word to check
	:param letters_boggle: a list of all letters in boggle
	:return: (bool) If the word is spelled by only letters in boggle
	"""
	for ch in s:
		if ch not in letters_boggle:
			return False
	return True


def read_dictionary(file, dictionary):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:param file: str, the filepath of dictionary
	:param dictionary: a list made by the file of dictionary
	:return: this function does not return anything
	"""
	with open(file, 'r') as f:
		for line in f:
			word = line.strip()
			dictionary.append(word)


def has_prefix(sub_s, dictionary_excerpt):
	"""
	This function is to check if there's any word which starts with sub_s in dictionary_excerpt list.
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary_excerpt: a list of words excerpted from dictionary based on letters in Boggle.
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_excerpt:
		if word.startswith(sub_s):
			break
	return word.startswith(sub_s)


if __name__ == '__main__':
	main()
