with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    num_of_words = len(words)
    print(num_of_words)

    lower_case = file_contents.lower()

    dictionary = {}

    for letter in lower_case:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    del dictionary[" "]

    print(dictionary)
