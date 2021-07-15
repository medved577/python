# Проверьте алгоритм, должны получаться суммы: 17485588610, 15392909930
my_list = [n ** 3 for n in range(1000)][1::2]
sum_value = 0 # общая сумма чисел

# а. Вычислим сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
for idx in range(len(my_list)):
    value_list = my_list[idx]
    sum_number = 0  # сумма числа

    while value_list > 0:
        sum_number += value_list % 10
        value_list = value_list // 10

    if sum_number % 7 == 0 :
        sum_value = sum_value + sum_number


print(sum_value)
