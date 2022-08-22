"""
File: anagram.py
Name: Luna
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 23

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program requires user to input any word and help to find all anagram(s).
    """
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    dictionary = []
    read_dictionary(FILE, dictionary)

    while True:
        s = input('Find anagrams for: ')

        start = time.time()

        if s == EXIT:
            break
        else:
            print('Searching...')
            anagrams = []
            find_anagrams(s, dictionary, anagrams)
        print(f"{len(anagrams)} anagram(s): {anagrams}")

        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(file, dictionary):
    """
    This function reads the file of dictionary and make a list accordingly.
    :param file: str, the filepath of dictionary
    :param dictionary: a list made by the file of dictionary
    :return: this function does not return anything
    """
    with open(file, 'r') as f:
        for line in f:
            word = line.strip()
            dictionary.append(word)


def find_anagrams(s, dictionary, anagrams):
    """
    This function finds all anagram(s).
    :param s: str, the word input by user
    :param dictionary: the list made by the file of dictionary
    :param anagrams: a list of all anagram(s) found
    :return: this function does not return anything
    """
    for word in dictionary:
        if len(word) == len(s):
            letters_word = []
            letters_s = []
            for ch in word:
                letters_word.append(ch)
            for ch in s:
                letters_s.append(ch)
            if sorted(letters_word) == sorted(letters_s):
                anagrams.append(word)
                print('Found:', word)
                print('Searching...')


if __name__ == '__main__':
    main()
