# class map(object)
#   map(func, *iterables) --> map object
# в качестве func мы можем передавать как встроенные функции, так и те, которые создаем сами
# *iterables - к итерабельным последовательностям относятся (списки, кортежи, словари, функция range и.т.д)
# к итерабельным последовательностям можно применять функции , которые действуют над коллекциями, такие как max, min, sum
# итераторы можно преобразовывать к другим коллекциям
# map object - представляет собой итератор который вычисляет результат работы функции которую вы передали
# на каждый аргумент из этой последовательности
a = [-1, 2, -3, 4, 5]
b = list(map(abs, a))   # преобразуем к списку при помощи функции list
print(b)
# эту же программу можно было написать при помощи генератора списков
c = [abs(i) for i in a]
print(c)


# используем собственную функцию
n = [-1, 5, -3, 4, -17, 1]

def f(x):
    return x**2

k = list(map(f, n))  # не указываем ни скобки , ни аргумент, только название функции
print(k)


p = ['hello', 'hi', 'good morning']
l = list(map(len, p))
print(l)

# для строк в качестве функций можно передавать и методы этих объектов
v = list(map(str.upper, p))
print(v)

# в функцию map можно передавать анонимные функции
j = list(map(lambda x: x[::-1], p))
print(j)

u = list(map(lambda x: x+'!', p))
print(u)

# можем например преобразовать строку к списку
w = list(map(list, p))
print(w)

# отсортируем w в алфавитном порядке
g = list(map(sorted, w))
print(g)

h = list(map(int, input().split()))
print(h)
# напоминаю, что все что делается через функцию map можно сделать и через генератор списка
d = [i[::-1] for i in p]
print(d)
