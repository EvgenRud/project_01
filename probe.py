# TODO итерируемые объекты list, turple, dict
# TODO условный оператор if (bool)
# TODO операторы цикла for, while

# Задача 1
# Приведём список покупок в магазине

#shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

# а. Вставте рыбу между горошком и рисом

#print(type(shop_list),
      #len(shop_list)
      #)

#from pprint import pprint
#pprint(dir(shop_list))


#shop_list.insert(
    #shop_list.index('Рис'), 'Рыба')

#print(shop_list)

# b. Добавьте фрукты из списка fruits в конец списка shop_list

#fruits = ['Яблоко', 'Апельсин', 'Клубника']

#shop_list.extend(fruits)
#print(shop_list)

# c. Удалите из списка shop_list картофель

#shop_list.remove('Картофель')
#shop_list.pop(shop_list.index('Картофель'))
#print(shop_list)
#print(shop_list)

# d. Какими по счёту стоят хлеб и апельсин? Вывести номера на консоль в формате 
# Номер "номер" продукта в списке - N

#print(shop_list.index('Хлеб'), shop_list.index('Апельсин'), sep='\n')


#primes = [1, 2, 3, 8, 10, 20]
#empty_lst = []

#empty_lst.append(primes)
#empty_lst.append(primes)
#empty_lst.append(primes)

#print(empty_lst)

#[[1, 2, 3, 8, 10, 20],
#[1, 2, 3, 8, 10, 20],
#[1, 2, 3, 8, 10, 20]]

#print(empty_lst[1][3])

# Сравнение кортежей и списков

#rainbow = ('Red', 'Green', 'Blue') # кортеж - неизменяемый массив
#primes = [1, 2, 3, 8, 10, 20] # список - изменяемый массив

#print(id(primes))

# Проблема изменяемых объектов

#new_lst = primes
#new_lst.append('JDJFKJJFKJJL')
#print(new_lst, primes, sep='\n')
#print(id(primes) == id(new_lst))

#Копии кортежей

#print(id(rainbow))

#new_tpl = rainbow + ('Violet', 'Orange')

#print(new_tpl, rainbow, sep='\n')
#print(id(rainbow) == id(new_tpl))

# Условный оператор if-elif-else

# Заданы размеры коробки box_x, box_y и товара product_x, product_y
# Определить, поместится ли товар в коробке (габариты товара параллельны размеру коробки)
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные
#box_x, box_y = 10, 7
#product_x, product_y = 8, 9

# проверить для 
# product_x, product_y = 9, 8
# product_x, product_y = 8, 6
# product_x, product_y = 3, 4
# product_x, product_y = 11, 9
# product_x, product_y = 9, 11

# раскомментируйте нужную строку
# Вариант1
#if box_x >= product_x:
    #print('По грани х входит')
    #if box_y >= product_y:
        #print('ДА')
    #else:
        #print('НЕТ')   
#else:
    #print('НЕТ') 

# Вариант 2
#if box_x >= product_x and box_y >= product_y:
    #print('Да')
#else:
    #print('Нет')    

# Вариант 3

#print(True if box_x >= product_x and box_y >= product_y else False )

# Операторы цикла
# while

# Последовательность Фибоначчи
#№       1 2 3 4 5 6 7 ... 100
#Число   1 1 2 3 5 8 13 ... ?

#fib1, fib2 = 1, 1

#search = input('Введите искомый номер последовательности: ')
#i = int(search) - 2

#while i > 0:
    #print(fib2)
    #(fib1, fib2) = (fib2, fib1 + fib2)
    #print(f'Счётчик {i}')
    #i -= 1
    
#print(fib2)    

# for

#room_prices = [41, 94, 100, 7, 92, 62, 49, 37, 17]

#for price in room_prices:
    #print(price)

# Словари

employees = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121
}
#1
top_managers = []
for name in employees.keys():
    if employees[name] >= 100000:
        top_managers.append(name)
print(top_managers)  

#2
top_managers = [name for name, salary in employees.items() if salary >= 100000]

print(top_managers)






#primes = [1, 2, 3, 4, 5]
#rainbow = ('Red', 'Green', 'Blue')

#capitals = {}
#capitals['Россия'] = 'Москва'
#capitals['Италия'] = 'Рим'

#print(capitals)
#print(capitals['Италия'])



    



