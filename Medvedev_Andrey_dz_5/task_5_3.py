#  Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)

from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


# Вариант - 1
# iterator = zip_longest(tutors, klasses, fillvalue=None)
# print(list(iterator))

# Вариант - 2

def gen():
    i, j = 0, 0
    while i < len(klasses):
        if i >= len(tutors):
            yield None, klasses[i]
            i += 1
            j += 1
            break
        else:
            yield tutors[j], klasses[i]
            i += 1
            j += 1

print(gen)  # это генератор
for gen in gen():
    print(gen)
