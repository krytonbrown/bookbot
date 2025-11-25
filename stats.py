def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lc_words = text.lower()
    chars = {}
    for char in lc_words:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_characters(char_dict):
    char_list = []
    sorted_list = []
    for value in char_dict:
        if value.isalpha() == False:
            pass
        else:
            char_list.append({"char": value, "num": char_dict[value]})
            char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list