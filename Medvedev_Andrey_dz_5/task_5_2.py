#  Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

# Вариант - 1
#num = input("Введите число: ")
#print(list (range(1, int(num) + 1, 2)) )
# list - иначе работает не правильно

# Вариант - 2
#num = input("Введите число: ")
#nums = [num for num in range(1, int(num), 2)]
#print(*nums)

# Вариант - 3
num = [num for num in range(1, int(input("Введите число: ")) + 1, 2)]
print(num)

