#"//how   make  a funtion  with   python?"?
from itertools import count


def count_letters(word):
    return (count_vowels(word) + count_consonants(word))


a = ("ef3ergqerf FCRWV  revgweger tgwtgw tegwet")

count_letters(a)
