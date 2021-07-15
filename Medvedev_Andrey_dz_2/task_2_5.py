# список цен на товары
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Добавить нули: должно быть 07 коп или 00 коп
sum_str = ""
for indx in prices:
    price = str(indx)
    if price.find('.') < 1:  # копеек нет
        rub = price  # получаем целое - рубли
        kop = "00"
    else:
        rub = str(indx)[0: price.find('.')]  # получаем целое - рубли
        kop = price[(str(indx).rfind('.')) + 1:]  # получаем дробное - копейки
        if (len(kop) < 2) and (int(kop)) < 10:
            kop = "0" + kop

    sum_str += rub + " руб " + kop + " коп ,"

print("Домашнее задание 2а: ")
print(sum_str)

# B. Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
print(" ")
print("Домашнее задание 2b: ")
print("Список отсортированный по возрастанию: ")
print(sorted(prices))
print("Исходный список не изменился: ")
print(prices)

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
new_prices = []
new_prices.extend(prices)
print(" ")
print("Домашнее задание 2c: ")
print(id(prices), "Старый список")
print(id(new_prices), "Новый список")
print("Новый список отсортированный по убыванию")
print(sorted(new_prices, reverse=True))

# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(" ")
print("Домашнее задание 2d: ")
print("Пять самых дорогих товаров: ")
print(sorted(prices, reverse=True)[:5])