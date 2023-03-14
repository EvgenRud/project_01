# TODO функция def
# TODO отладка
# TODO импорт модулей (примеры)




# Принцип DRY - Don't repeat yourself
# Создание функции 
#def greeting(name):
    #print(f'Hello, {name}')

# Вызов функции
#greeting('Mark')

# Вызов функции с параметром
#for i in ['Mark',  'R2D2', 'Anakin', 'World']:
   #greeting(i)

# Структура файла с кодом
# 1 Импорты
# import чото

# 2 Функции
# def чото
#     print(чото)

# Код который содержит цикл или инициализацию

print('Start Debuging')

def get_topmgr_list(dct_report):
    mgrs_list = []
    for name in dct_report.keys():
        if dct_report[name] >= 100000:
            mgrs_list.append(name)
    return mgrs_list        

employees = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121
     }

top_managers = get_topmgr_list(employees)
print(top_managers)



a = [1, 2, 3]
b = [1, 2, 3]
def af(lst):
    lst = lst * 2
    return None
def bf(lst):
    lst.extend([1, 2, 3])
    return None
    af(a)
    bf(b)
print(a, b)






