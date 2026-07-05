def word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def character_occurances(book_text):
    char_dictionary = {}
    lower_case = book_text.lower()
    for char in lower_case:
        if char in char_dictionary:
            char_dictionary[char] +=1
        else:
            char_dictionary[char] = 1
    return char_dictionary

def sort_dictionary (dictionary):
    sorted_list=[]
    for entry in dictionary:
        mapped_dictionary = {}
        mapped_dictionary["char"] = entry
        mapped_dictionary["num"] = dictionary[entry]
        sorted_list.append(mapped_dictionary)
        sorted_list.sort(key=helper,reverse = True)
    return sorted_list

def helper(input):
    return input["num"]


