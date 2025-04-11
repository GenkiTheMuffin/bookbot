import sys

from stats import count_chars, get_num_words, split_to_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content


def main():
    content = get_book_text(f"{path}")
    word_count = get_num_words(content)
    char_count = count_chars(content)
    zoz = split_to_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in zoz:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['count']}")
    print("============= END ===============")


main()
