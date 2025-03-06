from stats import count_words, count_chars, sort_char_count
import sys

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return
    book_location = args[1]
    text_content = get_book_text(book_location)
    total_words = count_words(text_content)

    char_count = count_chars(text_content)

    sorted_dict = sort_char_count(char_count)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_location}...
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------
        """)

    for k,v in sorted_dict.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")

main()

