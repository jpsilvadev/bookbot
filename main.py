import sys
from stats import count_words, get_chars, sort_char_count


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1]
    book_text = get_book_text(book_filepath)
    word_count = count_words(book_text)
    chars = sort_char_count(get_chars(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count -------")
    for char_counts in chars:
        char = char_counts["char"]
        num = char_counts["num"]
        print(f"{char}: {num}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    main()
