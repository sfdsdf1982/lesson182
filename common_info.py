# Модуль functools предлагает фукнции для быстрой обработки коллекций

# from _functools import reduce

# Функция reduce - применяет функцию из параметра к каждой паре элементов коллекции

# def my_func(prev,cur):
#     return prev + cur
#
# print(reduce(my_func,[1,2,3,4,5]))

from itertools import count,cycle

# for item in count(5): #функция count нам даст новый список от 5 до беск-ти
#     if item > 15:
#         break
#     print(item)

# Пример на cycle
c = 0
for item in cycle("ABC"):
    if c > 10:
        break
    print(item,end=" ")
    c += 1