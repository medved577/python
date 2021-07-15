my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

indx = 0
while indx < (len(my_list)):
    val_list = my_list[indx]
    last_space = val_list.rfind(' ') # с конца до первого пробела
    str_value = val_list [0 : last_space] # сохраняем строчку до имени
    name = val_list [last_space+1:] # получаем имя
    my_list [indx] = str_value + " " +  name.capitalize()

    indx += 1

print(my_list)
