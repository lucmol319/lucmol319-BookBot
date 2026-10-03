def word_count(text):
    words = text.split()
    return len(words)

# Add a function that accepts the book's text and returns a dict[str, int]
# containing the count of every character, including spaces and symbols.
# Convert each character to lowercase with .lower().
def character_count(text):
    char_dict = {}
    for char in text.lower():
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

# It should accept a tuple[str, int] like ("b", 4868).
# It should return the count value from the tuple.
def sort_on(dict_item: tuple[str, int]) -> int:
    return dict_item[1]

def chars_dict_to_sorted_list(chars_dict):
    # Convert the dictionary to a list of tuples
    char_items = list(chars_dict.items())
    # Sort the list by the count (second element of each tuple)
    char_items = sorted(char_items, key=sort_on, reverse=True)
    return char_items