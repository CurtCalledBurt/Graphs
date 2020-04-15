# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

from os import path

f = open("projects/social/words.txt", 'r')
words = []
for word in f:
    words.append(word[:-1])
f.close()

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def transform(starting_word, ending_word, dictionary, path=None):
    # if path is None:
    #     path = []
    q = []
    q.append((starting_word, []))
    while len(q) > 0:
        # print(q)
        node = q.pop(0)
        # print(node)
        word = node[0]
        path = node[1].copy()
        # print(path)
        path.append(word)

        for i in range(len(word)):
            for char in range(ord('a'), ord('z') + 1):
                char_actual = chr(char)
                temp_word = word[:i] + char_actual + word[i+1:]
                if temp_word in dictionary:
                    dictionary.remove(temp_word)
                    q.append((temp_word, path))
            
        if word == ending_word:
            return path
    return None


dictionary = set()
with open("projects/social/words.txt", "r") as f:
    for word in f.readlines():
        dictionary.add(word[:-1])


print(transform('hit', 'cog', words))