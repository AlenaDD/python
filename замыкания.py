# def mine_func(name):
#     def inner_func():
#         print('hello my friend', name)
#     return inner_func
# d = mine_func('Ivan')
# print(d())

''' функция возвращает сумму переданых чисел'''
# def adder(value):
#     def inner(a):
#         return value + a
#     return inner
# a2 = adder(5)
# print(a2(5))
# a5 = adder(10)
# print(a5(10))

'''Функция ведет подсчет того, сколько раз ее вызвали'''
# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner
#
# q = counter()
# print(q())
# print(q())
# print(q())
# print(q())


'''Первый способ'''
# def average_numbers():                           # функция для нахождения среднего арифметического введенных чисел
#     numbers= []                                  # создаем список в области видимости основной функции
#     def inner(number):                           # зоздаем вспомогательную функцию в которую будем передавать значения, которые будут сохраняиться в наш список
#         numbers.append(number)                   # добавляем введенные значения в наш список
#         print(numbers)
#         return sum(numbers) / len(numbers)      #  возвращаем среднее арифметическое введенных в список чисел
#     return inner                                # возвращаем функцию inner (без вызова функции, просто возвращаем саму функцию) чтобы получилось замыкание
# d1 = average_numbers()                          # создаем переменную d1  и она будет равна ваызову нашей основной функции ( по сути d1 сама становится функцией)
# print(d1(5))                                    # передаем в d1 значение , которое сохранится в наш список numbers
# print(d1(20))                                   # при дальнейшей передаче значений в переменную d1 они будут добавлчяться в список( старые значения 6не удаляются)
# print(d1(10))
# print(d1(45))

'''ВАЖНО!!'''
''' Если мы создадим новую переменную вместо d1, например d2, то создается новая область видимости фунции и появится 
пустой список в который мы так жен сможем добавлять элементы'''

'''Второй способ'''

# def average_numbers():
#     summa = 0                                    # создаем переменную в области видимости основной функции, которая будет считать сумму вводимых чисел
#     count = 0                                    #  создаем переменную для подсчета количества элементов ( для того чтобы найти среднее арифметическое
#     def inner(number):                           # зоздаем вспомогательную функцию в которую будем передавать значения, которые будут сохраняиться в наш список
#         nonlocal summa                           # данной строкой говорим , что значение переменной summa необходимо брать именнол из строки кода 55
#         nonlocal count
#         print(number)
#         summa += number
#         count +=1
#         return summa / count
#     return inner
# d1 = average_numbers()
# print(d1(5))
# print(d1(20))
# print(d1(10))
# print(d1(45))


# '''напишем функцию timer, которая будет засекать сколько време6ни прошло с последнего вызова нашей функции '''
# from time import perf_counter
#
# def timer():
#     start = perf_counter()
#     def inner():
#         return perf_counter() - start
#     return inner
# s = timer()
# print(s())

# ' напишите функцию timer которая считает разницу между двумя соседними вызовами функции'
#
# from time import perf_counter
# def timer():
#     start = perf_counter()
#     def inner():
#         nonlocal start
#         s = perf_counter()
#         res = s - start
#         start = s
#         return res
#     return inner
# s = timer()
# print(s())


def add(a,b):
    return a+b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print(f'Функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)
    return inner

q = counter(add)
print(q(10, 20))