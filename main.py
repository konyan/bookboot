def main():
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        count = wordCount(contents)
        char_dict = count_char(contents)
        printReport(char_dict,
                   count)


def wordCount(contents):
    wordsArray = contents.split()
    return len(wordsArray)

def count_char(contents):
    lower_contents = contents.lower()
    char_counts = {}
    for char in lower_contents:
        if char in char_counts:
            char_counts[char] += 1
        else: 
            char_counts[char] = 1


    return char_counts


def printReport(dictChar, count):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count} words found in the document')

    for char,count in dictChar.items():
        if char.isalnum():
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()
