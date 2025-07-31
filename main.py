from stats import word_count, each_character_count, print_check, sort_alpha_by_highest_count, dictionary_to_list_of_dictionaries
import sys

def get_book_text(book_filepath):
    file_contents = book_filepath.read()
    return file_contents

def main():
 # old        get_book_text(frankenbook)
 # updated    print(get_book_text(frankenbook))
 # old        word_count(get_book_text(frankenbook))
 # updated
 #   print(word_count(get_book_text(txtfile_string)))
 #   print(each_character_count(txtfile_string))
    txtfile_string = get_book_text(txtfile)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count(txtfile_string))
    print("--------- Character Count -------")
    #print(each_character_count(get_book_text(txtfile_string)))
    full_character_list = dictionary_to_list_of_dictionaries(each_character_count(txtfile_string))
    full_character_list.sort(reverse=True, key=sort_alpha_by_highest_count)
    for item in full_character_list:
        print(f"{item["character_name"]}: {item["character_count"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

with open(sys.argv[1]) as txtfile:

    main()
