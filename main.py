#importing sys to handle command line arguments
import sys
# Importing functions from stats.py    
from stats import count_words
from stats import count_characters
from stats import sort_characters
from stats import print_character_stats

# A module for reading book text files
def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
        
# The main function to run the book analysis and print a report to console
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {filepath}")
    print(" ------------ Word Count ------------ ")
    print(f"Found {num_words} total words")
    print(" ------------ Character Count ------------ ")
    print_character_stats(text)
    

main()