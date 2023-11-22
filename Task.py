# Создать функцию, которая принимает список чисел. В функции посчитать
# количество элементов списка у которых есть нечетные соседи

def get_count(lst):
   return len([lst[i] for i in range(1,len(lst) - 1) if lst[i - 1] % 2 != 0 and lst[i + 1] % 2 != 0])

print(get_count([11,2,3,4,5,7,3,1,91]))
