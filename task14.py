import re

# in_text=input()

in_text = "Lorem"

# txt = re.sub(pattern='[A-Z]', repl='[a-z]', string=in_text, count=len(in_text))


def find_latin_set(text):
    # text = re.sub(pattern='[A-Z]', repl='[a-z]', string=text, count=len(text))
    latin_set = set()
    for letter in text:
        l=letter.lower
        latin_set.update(l)
    return print(latin_set)


find_latin_set(in_text.lower)
