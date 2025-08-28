import sys
from stats import count_words, count_chars, sort_char_count_dict


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_char_count = sort_char_count_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for k, v in sorted_char_count.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    main()
