#bookbot - ebook statistics programme

import sys

from stats import count_words, count_characters, sort_characters

book_text = ""
book_path = ""

def check_usage():
    global book_path
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()    

def main():
    check_usage()
    #book_text = get_book_text(book_path)
    #print(book_text)
    #print(get_book_text(book_path))
    count = count_words(get_book_text(book_path))
    #cc = count_characters(get_book_text(book_path))
    #print(f"Found {count} total words")
    #print(cc)
    sort = sort_characters(count_characters(get_book_text(book_path)))
    #print(f"sorted list: {sort}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("-------- Character Count -------")
    for c in sort:
        n = c["num"]
        print(f"{c['char']}: {n}")
    print("============= END ===============")
main()
