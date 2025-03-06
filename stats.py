def count_words(contents):
    sum = 0
    for word in contents.split():
        sum += 1
    return sum

def count_chars(contents):
    char_dict = {}

    for char in contents:
        if char.lower() in char_dict.keys():
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_char_count(char_dict):
    sorted_dict = {}
    sorted_value_list = list(char_dict.values())
    sorted_value_list.sort(reverse=True)

    for value in sorted_value_list:
        for k,v in char_dict.items():
            if value == v:
                sorted_dict[k] = value
    return sorted_dict
