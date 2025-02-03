def main():
    file_path = "books/frankenstein.txt"

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    count_words(file_contents)
    count_chars(file_contents)
    return report(file_contents, file_path)


def count_words(file):
    words = file.split()
    return len(words)

def count_chars(file):
    chars = {}

    for character in file.lower():
        if character in chars.keys():
            chars[character] += 1
        else:
            chars[character] = 1

    return chars

def report(file, filepath):
    chars = count_chars(file)
    letters = {}

    for char, count in chars.items():
        if char.isalpha():
            letters[char] = count

    letters = sorted(letters.items(), key=lambda x:x[1], reverse=1)

    print(f"--- Begin report of {filepath} ---")

    for i in letters:
        print(f"The '{i[0]}' character was found {i[1]} times")

    print("--- End Report ---")

main()