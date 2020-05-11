from util import Queue
import string

f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

alphabet = list(string.ascii_lowercase)
words_set = set()
for word in words:
    words_set.add(word.lower())

def get_neighbours(word):
    # create an empty list to hold neighbors
    neighbors = []
    # turn our word in to a letter list
    string_word = list(word)
    # loop over each index of the string word
    for i in range(len(string_word)):
        # for each letter...
        # swap letter with each letter in alphabet (for loop)
        for letter in alphabet:
            # make a temp word to work on
            temp_word = list(string_word)
            # set temp word at index to letter
            temp_word[i] = letter
            # join the temp word together to make a new word
            new_word = "".join(temp_word)
            # check if new word is not starting word
            # and new word is in word set
            if new_word != word and new_word in words_set:
                # append new word to the neighbors list
                neighbors.append(new_word)
    # return neighbors list
    return neighbors

def word_ladder(start_word, end_word):
    # create a queue to hold the vertex ids
    q = Queue()
    # enqueue the start vertex id
    q.enqueue( [start_word] )
    # create an empty visited set
    visited = set()
    # while the queue is not empty
    while q.size() > 0:
        # set vert to the dequeued element
        path = q.dequeue()
        word = path[-1]
        if word not in visited:
            if word == end_word:
                return path
            visited.add(word)
            for neighbour in get_neighbours(word):
                path_copy = list(path)
                path_copy.append(neighbour)
                q.enqueue(path_copy)
    return None

print(word_ladder("hit", "cog"))