def word_count(string_to_count):
    split_string = string_to_count.split()
    counted_words = 0
    for word in split_string:
        counted_words += 1
    return f"Found {counted_words} total words"

def each_character_count(string_to_count):
    character_counts_dictionary = {}
    for character in string_to_count:
        if character.lower() in character_counts_dictionary:
            character_counts_dictionary[character.lower()] += 1
        else:
            character_counts_dictionary[character.lower()] = 1
    return dict(sorted(character_counts_dictionary.items()))

def print_check(string_to_print):
    return string_to_print.read()

def dictionary_to_list_of_dictionaries(dictionary_to_convert):
    converted_dictionary_list = []
    for key in dictionary_to_convert:
        if key.isalpha():
            converted_dictionary_list.append({"character_name": key, "character_count": dictionary_to_convert[key]})
    return converted_dictionary_list

def sort_alpha_by_highest_count(list_to_sort):
    return list_to_sort["character_count"]
