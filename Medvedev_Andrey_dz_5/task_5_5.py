# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке

from functools import reduce

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

tmp = []
unique_brands = []
for el in src:
    if src.count(el) == 1:
        unique_brands.append(el)

print(unique_brands)

unique2 = []
unique = [unique2.append(el) for el in src if src.count(el) == 1]
print(unique2)
