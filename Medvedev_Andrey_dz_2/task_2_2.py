#Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

indx = 0

while indx < (len(my_list)):
    val_list = my_list[indx]

    indx += 1
    if val_list.isdigit():
        my_list.insert(indx, '"')
        my_list.insert(indx - 1, '"')
        if int(val_list) < 10:
            new_val = str('0' + str(val_list))
            my_list[indx] = new_val

        indx += 2
    elif val_list[0] in '+-':
        my_list.insert(indx, '"')
        my_list.insert(indx - 1, '"')
        only_digit = val_list[1:]
        new_val = str(val_list[0]+ '0' + str(only_digit))
        my_list[indx] = new_val
        indx += 2
indx += 1

print(' '.join(my_list))
