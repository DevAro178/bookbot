import sys
from stats import get_word_count,get_char_frequency,sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    try:
        filepath=sys.argv[1]
        content=get_book_text(filepath)
        num_words=get_word_count(content)
        dict_list=get_char_frequency(content)
        sorted_char_list=sort_char_dict(dict_list)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_char_list:
            if item["char"].isalpha():    
                print(f"{item["char"]}: {item["num"]}")
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()