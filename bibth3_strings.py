#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Library with useful string functions
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino and Allen Downey

import unicodedata
from string import whitespace, punctuation


def zfill(st, n):
    st = st.zfill(6)


def remove_accents(input_str):
    """Remueve los acentos de una string.
    No tengo ni idea de cómo funciona esta vaina.
    Tengo que estudiarla"""
    # Esta función no es de mi autoría. La tomé de un foro:
    # https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def make_plain(st, accents=False):
    st = st.strip()
    st = st.casefold()
    if accents:
        st = remove_accents(st)
    return st


def make_plain_with_accents(st):
    st = st.strip()
    st = st.casefold()
    return st


def no_whitespace(st):
    st = st.replace(" ", "")
    return st


def no_space_nor_punctuation(st):
    cleaning_st = (whitespace + punctuation +
                   en_sp_pr_chars7 + en_sp_pr_chars10)
    for ch in cleaning_st:
        st = st.replace(ch, "")
    return st


def make_words_it(file_name):
    words = open(file_name)
    for word in words:
        word = make_plain(word)
        yield word


def make_words_list(file_name):
    words = open(file_name)
    list_of_words = []
    for word in words:
        word = make_plain(word)
        list_of_words.append(word)
    return list_of_words


def make_words_dicc(file_name):
    words = open(file_name)
    dicc_of_words = {}
    pos = 0
    for word in words:
        word = make_plain(word)
        dicc_of_words[word] = pos
        pos += 1
    return dicc_of_words


def w_bigger_than(words, lenght):
    for word in words:
        if len(word) > lenght:
            print(word)


def first_letter(st):
    '''Doesn't work with the empty string.
    '''
    return st[0]


def middle_str(st):
    return st[1:-1]


def last_letter(st):
    '''Doesn't work with the empty string.
    '''
    return st[-1]


def middle_min_str(st):
    len_st = len(st)
    if len_st < 3:
        return st
    if len_st % 2 == 0:
        i = int((len/2)-1)
        j = int((len/2)+1)
        return st[i:j]
    else:
        i = int((len-1)/2)
        return st[i]


def second_letter(st):
    '''Doesn't work with the empty string.
    '''
    return st[1]


def is_palindrome_recursive(st):
    '''Recursively identifies palindrome strings words.
    The empty string '' is considered a palindrome, as well as any string
    with one character. This function doesn't work yet with every sentence that
    inlcudes punctuation marks'''
    len_st = len(st)
    # The first "if" –including its branches– is a guardian for
    # the special case of empty strings, which doesn't need any recursion,
    # and the base case of one-character strings, which ends the recursion.
    if len_st == 1:
        return True
    elif len_st == 0:
        return True
    # This second "if" make central logic of the function. It either stops
    # the recursion when it found that the word is not a palindrome or
    # keep going with the recursion if there is still a chance.
    if first_letter(st) != last_letter(st):
        return False
    return is_palindrome(middle_str(st))


def is_palindrome(st):
    """Checks if the string x or its representation
    as a string is a palindrome.

    x: it could be a sring or an integer
    """
    st = str(st)
    return st[::-1] == st


def has_palindrome(x, start, lenght):
    """Checks if the string x or its representation
    as a string has a palindrome inside.

    x: it could be a sring or an integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    x = str(x)
    x_lenght = len(x)
    if lenght < x_lenght:
        end = start + lenght
    else:
        start = 0
        end = lenght
    sub_x = str(x)[start:end]
    return sub_x[::-1] == sub_x


def make_palindrome(string, middle_st=""):
    """Make a palindrome from a string representation.
    It is able to produce odd-lengh palindromes
    if the middle_st is provided.

    i: string
    middle_st: string
    """
    return string[::-1] + middle_st + string


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


# String character blocks
en_chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
en_chars2 = "abcdefghijklmnopqrstuvwxyz"
en_sp_pr_chars1 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
en_sp_pr_chars2 = "abcdefghijklmnñopqrstuvwxyz"
en_sp_pr_chars3 = "ÁÇÉÍÓÚ"
en_sp_pr_chars4 = "áçéíóú"
en_sp_pr_chars3 = "ÄËÏÖÜ"
en_sp_pr_chars4 = "äëïöü"
en_sp_pr_chars5 = "ÀÁÂÃÄÅÆÇĀĂÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß"
en_sp_pr_chars6 = "àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿāă"
en_sp_pr_chars7 = "'\"¡!¿?,;:.×()/%&$#-_÷–·—#―‘’’‚‛“”„‟‥…‧«»"
en_sp_pr_chars8 = "ÖÀÄÒÎÈÁÞĂĀÉÛÊÇßÍØÃÆÝÂÜÔÌÕÓÅÑÚÙËÐÏ"
en_sp_pr_chars9 = "âêðïçøèõáñäíôùúåýëãöòîàüóæÿûìþéăā"
en_sp_pr_chars10 = '÷”„?,»/#–¿!’:¡&%(“‧×’·.‚‛)«‥—-#\'_―‘";$…‟'


# Character block colletions
en_letters = [en_chars1, en_chars2]
en_blocks = [en_chars1, en_chars2, en_sp_pr_chars10, en_sp_pr_chars10]
es_bloks = [en_sp_pr_chars1, en_sp_pr_chars2, en_sp_pr_chars8, en_sp_pr_chars9,
            en_sp_pr_chars10]


def rot_encoder(string, rotation, chr_bloks):
    encoded_string = ""
    for character in string:
        encoded_chr = character
        for chr_blok in chr_bloks:
            if character in chr_blok:
                # I use modular arithmetic to make the alphabetic rotation
                pos = chr_blok.index(character)
                mod_n = len(chr_blok)
                new_pos = (pos + rotation) % mod_n
                encoded_chr = chr_blok[new_pos]
                break
        encoded_string += encoded_chr
    return encoded_string


def rot_decoder(string, rotation, chr_bloks):
    decoded_string = ""
    for character in string:
        decoded_chr = character
        for chr_blok in chr_bloks:
            if character in chr_blok:
                # I use modular arithmetic to make the alphabetic rotation
                pos = chr_blok.index(character)
                mod_n = len(chr_blok)
                new_pos = (pos - rotation) % mod_n
                decoded_chr = chr_blok[new_pos]
                break
        decoded_string += decoded_chr
    return decoded_string
