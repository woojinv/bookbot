def main():
    path = "books/frankenstein.txt"
    with open(f"./{path}") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        char_counts = count_chars(file_contents)

        print(f"--- Begin report of {path} ---")
        print(f"{num_words} found in the document")
        print()
        sorted_char_counts = dict(
            sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
        )
        for char, count in sorted_char_counts.items():
            if char.isalpha():
                print(f"the {char} character was found {count} times")

    print("--- End report ---")


def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_chars(file_contents):
    char_counts = {}
    for char in file_contents:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1

    return char_counts


main()
