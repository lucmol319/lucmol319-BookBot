import sys
from stats import chars_dict_to_sorted_list, word_count, character_count

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_text, sorted_chars, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")

    # Use str.isalpha() to skip non-alphabetic characters.
    # Print each alphabetic character and its count
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}") # e: 44538
    print("============= END ===============")

def main():
    # python3 main.py where there's no sys.argv[1]
    # Expecting exit code: 1
    # Expecting stdout to contain all of:
    # # Usage: python3 main.py <path_to_book>
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    char_dict = character_count(book_text)

    # Sort the characters by count in descending order
    sorted_chars = chars_dict_to_sorted_list(char_dict)
    print_report(book_text, sorted_chars, book_path)

if __name__=="__main__":
    main()