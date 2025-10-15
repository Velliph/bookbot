# A module for text statistics

#Counts the total number of words in the text
def count_words(text):
    return len(text.split())

#Counts the occurrences of each character in the text, ignoring spaces and case
def count_characters(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char == ' ':
            continue
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

#Sorts characters by their frequency in descending order
def sort_characters(char_dict):
    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})

    def get_num(d):
        return d["num"]

    char_list.sort(key=get_num, reverse=True)
    return char_list

#Prints the sorted character statistics in the A: # format
def print_character_stats(text):
    sorted_chars = sort_characters(count_characters(text))
    for entry in sorted_chars:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")