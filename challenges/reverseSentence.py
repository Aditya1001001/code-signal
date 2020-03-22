"""Reverse the order of words in a given string sentence. You can assume that
sentence does not have any leading, trailing or repeating spaces.

Example-
For sentence = "Man bites dog", the output should be
reverseSentence(sentence) = "dog bites Man" """

def reverseSentence(sentence):
    return " ".join(sentence.split()[::-1])