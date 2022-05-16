#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Library with usefull dictionary functions
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Dictionary Library (by José Delpino)

from os import system
from bibth3_strings import make_plain, no_space_nor_punctuation
from bibth3_lists import print_string_list, reduce_llist
from random import randint, choice


def make_ddicts(filepath, key_gen, items_gen, value_adder, method=None):
    the_file = open(filepath)
    ddicts = {}
    for line in the_file:
        line = make_plain(line)
        the_key = key_gen(line)
        items = items_gen(the_key, line)
        subkey, value = items[0], items[1]
        if method is None:
            add_to_ddicts(ddicts, the_key, subkey, value, value_adder,
                          method="as_an_element")
        else:
            add_to_ddicts(ddicts, the_key, subkey, value, value_adder,
                          method)
    return ddicts


def add_to_ddicts(ddicts, the_key, sub_key, value, value_adder, method):
    if the_key in ddicts:
        sub_dict = ddicts[the_key]
        value_adder(sub_dict, sub_key, value, method)
    else:
        ddicts[the_key] = {}
        sub_dict = ddicts[the_key]
        value_adder(sub_dict, sub_key, value, method)


def make_dict(filepath, key_gen, element_adder):
    the_file = open(filepath)
    the_dict = {}
    for line in the_file:
        line = make_plain(line)
        the_key = key_gen(line)
        element_adder(the_dict, the_key, line)
    return the_dict


def make_simple_dict(filepath):
    return make_dict(filepath,
                     key_gen=lambda l: l,
                     element_adder=lambda d, k, l: d.setdefault(k))


def add_to_dictlist(the_dict, the_key, item, method):
    if method == "as_the_iterable":
        if type(item) is list:
            item = item[:]
        the_dict[the_key] = item
    elif method == "as_an_element":
        if the_dict.setdefault(the_key, [item]) != [item]:
            the_dict[the_key].append(item)


def invert_dict_imprv(the_dict, item_gen, element_adder):
    inv_dict = dict()
    for key in the_dict:
        value = the_dict[key]
        new_items = item_gen(key, value)
        new_key, new_value = new_items[0], new_items[1]
        element_adder(inv_dict, new_key, new_value)
    return inv_dict


def filter_the_dict(the_dict, function):
    newdict = dict()
    for key in the_dict:
        value = the_dict[key]
        if function(key, value):
            newdict[key] = value
    return newdict


def filter_ddicts(ddicts, the_filter, sub_filter, value_adder, method=None):
    newdict = dict()
    for key in ddicts:
        subdic = ddicts[key]
        if the_filter(key, subdic):
            for sub_key in subdic:
                value = subdic[sub_key]
                if sub_filter(sub_key, value, ddicts):
                    if method is None:
                        method == "as_the_iterable"
                    add_to_ddicts(newdict, key, sub_key, value,
                                  value_adder, method)

    return newdict


def size_ddicts(ddicts: dict) -> tuple:
    n_keys, n_sub_keys, n_items = 0, 0, 0
    n_keys = len(ddicts)
    for key in ddicts:
        subdict = ddicts[key]
        n_sub_keys += len(subdict)
        for sub_key in subdict:
            items = subdict[sub_key]
            n_items += len(items)
    return (n_keys, n_sub_keys, n_items)


def size_dict_list(the_dict: dict) -> tuple:
    n_keys, n_items = 0, 0
    n_keys = len(the_dict)
    for key in the_dict:
        items_list = the_dict[key]
        n_items += len(items_list)
    return (n_keys, n_items)


def find_the_n_longest(ddicts: dict, n: int) -> list:
    """Find the n longest str-subkeys in a ddict of lenghts
    and strings.
    """
    max_lenght = max(ddicts.keys())
    longest_list = list(ddicts[max_lenght].keys())
    longest_list.sort()
    n_longest = len(longest_list)
    another_lenght = max_lenght - 1
    while n_longest < n:
        needed = n - n_longest
        another_list = list(ddicts[another_lenght].keys())
        another_list.sort()
        found = len(another_list)
        if found >= needed:
            longest_list.extend(another_list[:needed])
            n_longest += needed
        else:
            longest_list.extend(another_list)
            n_longest += found
        another_lenght -= 1
    return longest_list


def search_by_key(ddicts, key_label, type_func):
    """Initiates a continuous loop that allows
    the user to search a ddict by key, printing
    all the subkeys it contains.
    """
    key_label = key_label.lower()
    keys = sorted(ddicts.keys())
    while True:
        print(f"{key_label.capitalize()}: ", keys)
        key = input(f"Which {key_label}? ")
        if key != "":
            key = type_func(key)
            print_dict(ddicts[key])
            print("\n")
        else:
            break
    system('clear')


def search_by_sub_key(ddicts, sub_key_label, type_func, items_label):
    """Initiates a continuous loop that allows
    the user to search a ddict by sub_key, printing
    all the subkey's items.
    """
    sub_key_label = sub_key_label.lower()
    items_label = items_label.lower()
    while True:
        sub_key_name = input("Which word? ")
        sub_key_name = sub_key_name.lower()
        sub_key = type_func(sub_key_name)
        if sub_key_name != "":
            sub_key_name = sub_key_name.upper()
            lenght = len(sub_key)
            sub_dict = ddicts[lenght]
            if sub_key in sub_dict:
                items = sub_dict[sub_key]
                print(f"The {sub_key_label} {sub_key_name}"
                      f"is in the dictionary. Its {items_label} are:")
                print(items)
                print("\n")
            else:
                print(f'"Sorry, {sub_key_name}" ' +
                      'is not in the dictionary.')
                print("Try with another word...")
                print("\n")
        else:
            break
    system('clear')


def add_dict_of_dicts(the_dict, the_key, sub_key, element=None):
    if the_key in the_dict:
        sub_dict = the_dict[the_key]
        if sub_key in sub_dict:
            pass
        else:
            sub_dict[sub_key] = element
    else:
        the_dict[the_key] = {sub_key: element}


def make_dict_dicts(file_name, key_generator):
    words = open(file_name)
    letters_dict = {}
    for word in words:
        word = make_plain(word)
        key_str = key_generator(word)
        add_dict_of_dicts(letters_dict, key_str, word)
    return letters_dict


def make_lenghts_dict(file_name):
    words = open(file_name)
    lenghts_dict = {}
    for word in words:
        word = make_plain(word)
        lenght = len(word)
        add_dict_of_dicts(lenghts_dict, lenght, word)
    return lenghts_dict


def make_lenghts_dict_alph(file_name, by_letter=1):
    """by_letter: 1 or 2
    """
    words = open(file_name)
    dicc_of_lenghts = {}
    for word in words:
        word = make_plain(word)
        lenght = len(word)
        if by_letter < lenght:
            letter = word[by_letter]
            if lenght not in dicc_of_lenghts:
                alpha_dicc = {letter: {word: None}}
                dicc_of_lenghts[lenght] = alpha_dicc
            else:
                alpha_dicc = dicc_of_lenghts[lenght]
                if letter not in alpha_dicc:
                    dicc_of_lenghts[lenght][letter] = {word: None}
                else:
                    dicc_of_lenghts[lenght][letter][word] = None
    return dicc_of_lenghts


def invert_dict_original(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if inverse.setdefault(val, [key]) != [key]:
            inverse[val].append(key)
    return inverse


def print_dict_of_dicts(dict_of_dicts):
    for key in dict_of_dicts:
        print(key, ":")
        sub_dict = dict_of_dicts[key]
        for sub_key in sub_dict:
            element = sub_dict[sub_key]
            if element is None:
                print_element = ""
            else:
                print_element = ":" + str(element)
            print(sub_key, print_element)
        print("\n")


def print_dict(the_dict):
    for key in the_dict:
        element = the_dict[key]
        print(key, ":", element)


def print_dict2(the_dict: dict, key_label: str,
                with_items=False,
                sub_label=""):
    print("\n")
    n_keys = len(the_dict)
    keys_list = list(the_dict.keys())
    keys_list.sort()
    if n_keys == 1:
        prompt = (f"The {key_label} is "
                  f"{keys_list[0].upper()}\n")
        more_than_one = False
    else:
        prompt = (f"The {n_keys} {key_label}(s) are:\n")
        more_than_one = True
    print(prompt)
    if more_than_one:
        n = 1
        for key in keys_list:
            print(f"[{n}] ", key)
            n += 1
            if with_items:
                items = the_dict[key]
                if type(items) == dict:
                    print_dict2(items, sub_label)
                elif type(items) == list:
                    print_string_list(items, sub_label)
                elif type(items) == tuple:
                    print_string_list(list(items), sub_label)
                else:
                    print(sub_label, " : ", items)
        print("\n")


def make_proplist(hist: dict) -> list:
    prop_list = []
    for key in hist:
        to_add = [key] * hist[key]
        prop_list.extend(to_add)
    return prop_list


def make_proplist2(hist: dict) -> list:
    prop_list = []
    for key in hist:
        to_add = [key] * hist[key]
        lenght = len(prop_list)
        if lenght == 0:
            prop_list.extend(to_add)
        else:
            for item in to_add:
                prop_list.insert(randint(0, lenght-1), item)
    return prop_list


def make_proplist3(hist: dict) -> list:
    pairs = zip(map(str, hist.keys()), hist.values())
    prop_items = map(lambda x: [x[0]] * x[1], pairs)
    prop_list = reduce_llist(prop_items)
    return prop_list


def choose_from_hist(hist: dict, keys_list: list):
    """Takes a histogram dict and a list of its keys that include them
    as many times as their frequencies in the dictionary. The function
    returns a random value from the histogram, chosen frmo the list with
    probability in proportion to frequency. The type of value returned
    depends of the kinds of values stored on the dict.
    """
    lenght = len(keys_list)
    picked_key = keys_list[randint(0, lenght-1)]
    return picked_key


def print_randomprop_keys(the_dict: dict, n: int,
                          prop_list: list, message: str):
    print(f"The {n} random word(s) from {message} are:\n")
    for i in range(1, n+1):
        random_key = choose_from_hist(the_dict, prop_list)
        freq = the_dict[random_key]
        tab = " " * (25-len(random_key))
        print(f"[{i}] {random_key} –>{tab}-> "
              f"FREQ = {freq}")
    print("\n")


def print_randomprop_keys2(the_dict: dict, n: int, message: str):
    prop_list = make_proplist(the_dict)
    print(f"The {n} random word(s) from {message} are:\n")
    for i in range(1, n+1):
        random_key = choose_from_hist(the_dict, prop_list)
        freq = the_dict[random_key]
        tab = " " * (25-len(random_key))
        print(f"[{i}] {random_key} –>{tab}-> "
              f"FREQ = {freq}")
    print("\n")


def print_random_keys(the_dict: dict, n: int, message: str):
    print(f"The {n} random word(s) from {message} are:\n")
    for i in range(1, n+1):
        random_key = choice(the_dict)
        print(f"[{i}] {random_key}")
    print("\n")


def make_book_hist(filepath):
    the_file = open(filepath)
    hist = {}
    for line in the_file:
        if line[0] == "#":
            continue
        line = make_plain(line)
        line = line.split()
        i = 0
        while i < len(line):
            line[i] = no_space_nor_punctuation(line[i])
            i += 1
        for word in line:
            hist[word] = hist.get(word, 0) + 1
    return hist


def make_words_dict(filepath):
    return make_ddicts(filepath,
                       key_gen=lambda l: len(l),
                       items_gen=lambda k, l: (l, None),
                       value_adder=add_to_dictlist,
                       method="as_the_iterable")


def not_in_target(source: dict, target: dict) -> list:
    not_there = list()
    for word in source:
        lenght = len(word)
        if lenght in target:
            if word not in target[lenght]:
                not_there.append(word)
    not_there.sort()
    return not_there


def calc_total_words(hist: dict) -> int:
    values_list = hist.values()
    return sum(values_list)


def most_common(hist):
    t = list(hist.items())
    t.sort(key=lambda p: p[1], reverse=True)
    return t
