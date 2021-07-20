# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
def num_translate ( rus_num ):
    eng_rus = dict(zero='ноль', one='один', two='два', three='три', four='четыре', five='пять', six='шесть',
                   seven='семь', eight='восемь', nine='девять', ten='десять')
    return eng_rus.get(rus_num)

input_num = input("Введите число прописью (от 0 до 10) по английски: ")
print ("По английски: ", input_num, ", по русски : ", num_translate (input_num))