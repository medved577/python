#  Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def nums_generator(max_num):
   for num in range(1, max_num + 1, 2):
       yield num

print(*nums_generator(16))
