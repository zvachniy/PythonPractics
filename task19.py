input_string = input()
InputNumber = int(input_string)
# int_to_string_dict={
#     'один':
#     'два'
#     'три'
#     'четыре'
#     'пять'
#     'шесть'
#     'семь'
#     'восемь'
#     'девять'
#     'десять'
# }
def number_to_words(number):
    chifry = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
    }
    desytki = {
        10: "десять",
        20: "двадцать",
        30: "тридцать",
        40: "сорок",
        50: "пятьдесят",
        60: "шестьдесят",
        70: "семьдесят",
        80: "восемьдесят",
        90: "девяносто",
    }
    sotni = {
        100: "сто",
        200: "двести",
        300: "триста",
        400: "четыреста",
        500: "пятьсот",
        600: "шестьсот",
        700: "семьсот",
        800: "восемьсот",
        900: "девятьсот",
    }
    tysachi={
        1000: "тысяча"
    }
    desytki_except = {
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать",
    }

    number1 = number % 1000
    number2 = number - number1
    if number < 10:
        return print(chifry.get(number))
    elif 10 < number < 20:
        return print(desytki_except.get(number))
    elif number > 20:
        return print(desytki.get(number2) + " " + chifry.get(number1))
    elif number < 1000000:
        return print()
    else:
        return "Введено число, которое не лежит в [1:99]!"


number_to_words(InputNumber)
