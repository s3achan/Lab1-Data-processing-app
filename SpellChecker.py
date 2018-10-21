#!/usr/bin/python
import os
import sys
import string 
from autocorrect import spell

# Strip words of any punctuations 
punctuation = '.,:;?!-()"\''

# Logic - check each word if it exists in dictionary or not
# If it doesn't -- attempt to correct it 


# list to store all the dictioary 
dictionary = []

# count the number of misspelled words
a = 1

if __name__ == '__main__':
    if len(sys.argv) == 3:
        # read the text file to check 
        checkFile = open(sys.argv[1]).read()
        # read the word file to check for words and
        # store the words in the dictionary
        # convert everything to lower case to simplify correction
        with open(sys.argv[2]) as f:
            for line in f:
                line = line.strip()
                dictionary.append(line.lower())

        # Loop through the file to check and strip of punctuations
        # and check if the word isn't in dictioary and if it isn't
        # return the correct spelling 
        for word in checkFile.split():
            word = word.strip(punctuation).lower()
            if word not in dictionary:
                print (str(a)+":"+word + " --> [ "+ spell(word))+ " ]"
                a = a +1 
    else:
        print "Usage: python spellcheck.py <text file> <wordfile>"





