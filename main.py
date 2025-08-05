def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def render_report(path, word_count, character_counts):

    render = f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------

"""
    for char in character_counts:
        if char["char"].isalpha():
            render += f"{char["char"]}: {char["num"]}\n"
    render += "============= END ==============="
    return render

from stats import word_count, count_char, sort_dict_list

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num = word_count(text)
    chars = count_char(text)
    print(render_report(path, num, sort_dict_list( chars) ))
main()

