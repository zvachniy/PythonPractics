import re

# in_text=input()

in_text = "Lorem"

txt = re.search(r"\W", in_text)


def find_latin_set(text):
    latin_set = set()
    for letter in text:

        latin_set.update(letter)
    return print(latin_set)


find_latin_set(txt)
