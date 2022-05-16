#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 8.5 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 8.5: General Caesar Cypher

from os import system


def code_generator(start, end):
    code_points = []
    chr_map = {}
    for code_point in range(start, end + 1):
        code_points.append(code_point)
        chr_map[chr(code_point)] = code_point
    return [code_points, chr_map]


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


if __name__ == "__main__":
    system('clear')
    # block1 = code_generator(ord("A"), ord("Z"))
    # block2 = code_generator(ord("a"), ord("z"))
    en_bhr1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    en_bhr2 = "abcdefghijklmnopqrstuvwxyz"
    en_sp_pr_bhr1 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    en_sp_pr_bhr2 = "abcdefghijklmnñopqrstuvwxyz"
    en_sp_pr_bhr3 = "ÁÇÉÍÓÚ"
    en_sp_pr_bhr4 = "áçéíóú"
    en_sp_pr_bhr3 = "ÄËÏÖÜ"
    en_sp_pr_bhr4 = "äëïöü"
    en_sp_pr_bhr5 = "ÀÁÂÃÄÅÆÇĀĂÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß"
    en_sp_pr_bhr6 = "àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿāă"
    en_sp_pr_bhr7 = "'\"¡!¿?,;:.×()/%&$#-_÷–·—#―‘’’‚‛“”„‟‥…‧«»"
    en_sp_pr_bhr8 = "ÖÀÄÒÎÈÁÞĂĀÉÛÊÇßÍØÃÆÝÂÜÔÌÕÓÅÑÚÙËÐÏ"
    en_sp_pr_bhr9 = "âêðïçøèõáñäíôùúåýëãöòîàüóæÿûìþéăā"
    en_sp_pr_bhr10 = '÷”„?,»/#–¿!’:¡&%(“‧×’·.‚‛)«‥—-#\'_―‘";$…‟'

    # encoded_string = rot_encoder("mazucamba, MAZUCAMBA", 13,
    #                             [en_letters1, en_letters2])
    # decoded_string = rot_decoder(encoded_string, 13,
    #                             [en_letters1, en_letters2])
    system("clear")
    # print(encoded_string)
    # print(decoded_string, "\n\n")
    # string = "No te comas el puré. ¡Está dañado! ¿Podrías escribirme a\n" \
    #         "mi correo? Es delpinoivivas@gmail.com. Te voy a mandar una\n" \
    #         "información importante. ¡Escríbeme!."
    string = "This was sent in by a fellow named Dan O’Leary. He came upon\n" \
             "a common one-syllable, five-letter word recently that has\n" \
             "the following unique property. When you remove the first\n" \
             "letter, the remaining letters form a homophone  of the\n" \
             "original word, that is a word that sounds exactly the same.\n" \
             "Replace the first letter, that is, put it back and remove\n" \
             "the second letter and the result is yet another homophone\n" \
             "of the original word. And the question is, what’s the word?"
    # es_bloks = [en_sp_pr_bhr1, en_sp_pr_bhr2, en_sp_pr_bhr8, en_sp_pr_bhr9,
    #            en_sp_pr_bhr10]
    en_letters = [en_bhr1, en_bhr2]
    encoded_string = rot_encoder(string, 21, en_letters)
    decoded_string = rot_decoder(encoded_string, 21, en_letters)
    print(string, "\n")
    print(encoded_string, "\n")
    print(decoded_string, "\n\n")
