# Функция filter похожа на функцию map, она также первым аргументом принимаент функцию а вторым итерабельную
# последовательность – результатом будет являться обьект filter
# Возвращает как и функция map итератор и в него войдут только те элементы итерабельной коллекции  для которых функция вернет знгачение true
#(Return at iterator yielding those items  of iterable for  which function(item) is true. If function is None return is items that are true)
# Функция фильтра должна возвращать true or false


def f(x):
    return x > 10

a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
b = filter(f, a)
print(list(b))
# то что мы делали можно заменить генератором списка
c = [i for i in a if i > 10]
print(c)
# в функцию filter мы так же можем передавать встроенные функции, функция должна возвращать True or False
# одна из таких является функция bool() которая возвращает Тру если число не является пустым множеством(0)
g = filter(bool, a)
# фналогично g = filter(None, a)
print(list(g))

v = ['world', 'hi', 'love', 'mum']
# В функицю filter также можно передавать анонимные функции(lambda), Функция должна возвращать True or False
t = filter(lambda x: len(x) > 4, v)
print(list(t))

# Также первым аргументом в функцию filter можно передавать методы объектов, но только те, которые возвращают true or false:
d = 'mkkltrtt111212135uybvns54eh'
p = list(filter(str.isdigit, d))
print(p)

# Разберем как можно отфильтровать словарь
j = {
    'Moscow': 600,
    'Ivanovo':100,
    'London': 5050,
    'Italy': 1251
}
k = list(filter(lambda x: j[x] > 700, j))
print(k)

