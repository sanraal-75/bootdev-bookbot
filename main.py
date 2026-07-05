from stats import word_count, character_occurances, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = (sys.argv)[1]
    
    book_text = get_book_text(book)
    book_word_count = word_count(book_text)
    pretty_list = sort_dictionary(character_occurances(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for entry in pretty_list:
        if entry["char"].isalpha() == True:
            print (f"{entry["char"]}: {entry["num"]}")


main()
