def count_words(text):
    return len(text.split())


def count_chars(text):
    text = text.lower()
    counter = {}
    for char in text:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    return counter


def sort_char_count_dict(counter):
    return dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
