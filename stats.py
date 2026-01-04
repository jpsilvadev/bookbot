def count_words(text):
    return len(text.split())


def get_chars(text):
    text = text.lower()
    chars = {}

    for char in text:
        if not char.isalpha():
            continue
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars


def sort_on(items):
    return items["num"]


def sort_char_count(chars):
    char_count = []
    for char, count in chars.items():
        char_count.append({"char": char, "num": count})
    char_count.sort(key=sort_on, reverse=True)
    return char_count
