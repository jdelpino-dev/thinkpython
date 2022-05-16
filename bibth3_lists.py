#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Library with usefull list functions
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# List Library (by José Delpino)


def print_string_list(strings: list, string_label: str,
                      with_sublist=False,
                      sub_lists=[],
                      sub_label=""):
    print("\n")
    n_strings = len(strings)
    if n_strings == 1:
        prompt = (f"The {string_label} is "
                  f"{strings[0].upper()}\n")
        more_than_one = False
    else:
        prompt = (f"The {n_strings} {string_label}(s) are:\n")
        more_than_one = True
    print(prompt)
    if more_than_one:
        n = 1
        for string in strings:
            print(f"[{n}] ", string)
            n += 1
            if with_sublist:
                sub_list = sub_lists[n-1]
                print_string_list(sub_list, sub_label)
        print("\n")


def print_list(the_list: list, item_label: str,
               with_sublist=False,
               sub_lists=[],
               sub_label=""):
    print("\n")
    n_items = len(the_list)
    if n_items == 1:
        prompt = (f"The {item_label} is "
                  f"{the_list[0]}\n")
        more_than_one = False
    else:
        prompt = (f"The {n_items} {item_label}(s) are:\n")
        more_than_one = True
    print(prompt)
    if more_than_one:
        n = 1
        for item in the_list:
            print(f"[{n}] ", item)
            n += 1
            if with_sublist:
                sub_list = sub_lists[n-1]
                print_list(sub_list, sub_label)
        print("\n")


def reduce_llist(llist: list) -> list:
        new_list = []
        for item in llist:
            new_list.extend(item)
        return new_list
