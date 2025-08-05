def word_count(text):
    return len(text.split())

def count_char(text):
    char_count_dict = {}
    for char in text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_dict_list(char_count_dict):
    list = []
    def sort_on(items):
        return items["num"]

    for char in char_count_dict:
        list.append( {
            "char": char,
            "num": char_count_dict[char]
        })
    list.sort(reverse=True, key=sort_on)
    return list