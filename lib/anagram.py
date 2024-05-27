# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word_letters = self.sort_letters(word)

    def sort_letters(self, word):
        return sorted(word)

    def match(self, word_list):
        return [word for word in word_list if self.sort_letters(word) == self.word_letters]

print(Anagram("listen").match(['enlists', 'google', 'inlets', 'banana']))