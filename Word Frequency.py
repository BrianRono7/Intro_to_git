# input = input("Please enter a sentence:")
# words = input.lower().split()
# dictionary = {}
# for word in words:
#     dictionary[word] = dictionary.get(word, 0) + 1

# for key, value in dictionary.items():
#     print(key, value)

def word_frequency(sentence):
    words = sentence.lower().split()
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

input = input("Please enter a sentence:")
print(word_frequency(input))


# 2. Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
# 3. Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
