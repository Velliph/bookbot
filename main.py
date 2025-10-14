def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
from stats import count_words

def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()