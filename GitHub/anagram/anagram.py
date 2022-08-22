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
            dictionary_excerpt = []
            write_dictionary_excerpt(s, dictionary, dictionary_excerpt)
            find_anagrams(s, '', len(s), anagrams, dictionary_excerpt)
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


def write_dictionary_excerpt(s, dictionary, dictionary_excerpt):
    """
    This function is to excerpt the dictionary list. Only words with the same formation of letters
    of the word input by user will be appended to the new dictionary_excerpt list.
    :param s: str, the word input by user
    :param dictionary: the list made by the file of dictionary
    :param dictionary_excerpt: a list that includes words from dictionary, of which
                               the formation of letters is same with the word input by user
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
                dictionary_excerpt.append(word)


def find_anagrams(s, current_a, len_s, anagrams, dictionary_excerpt):
    """
    This function finds all anagram(s).
    :param s: str, the word input by user
    :param current_a: str, possible anagram to check
    :param len_s: int, the length of the word input by user
    :param anagrams: a list of all anagram(s) found
    :param dictionary_excerpt: a list that includes words from dictionary, of which
                               the formation of letters is same with the word input by user
    :return: this function does not return anything
    """
    if len(current_a) == len_s:
        if current_a in dictionary_excerpt:
            anagrams.append(current_a)
            print('Found:', current_a)
            print('Searching...')
    else:
        for i in range(len(s)):
            # skip checking for possible anagrams starting with characters that have been checked
            if s[i] in s[:i]:
                pass
            else:
                # choose
                current_a += s[i]
                # explore
                if not has_prefix(current_a, dictionary_excerpt):
                    pass
                else:
                    find_anagrams(s[:i] + s[i+1:], current_a, len_s, anagrams, dictionary_excerpt)
                # un-choose
                current_a = current_a[:len(current_a)-1]


def has_prefix(sub_s, dictionary_excerpt):
    """
    This function is to check if there's any word which starts with sub_s in dictionary_excerpt list.
    :param sub_s: str, the word input by user
    :param dictionary_excerpt: a list that includes words from dictionary, of which
                               the formation of letters is same with the word input by user
    :return: boolean, if there's word which starts with sub_s in dictionary_excerpt list
    """
    for word in dictionary_excerpt:
        if word.startswith(sub_s):
            break
    return word.startswith(sub_s)


if __name__ == '__main__':
    main()
