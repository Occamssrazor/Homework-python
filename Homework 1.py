#  Задача 1. Сумма первых n положительных чисел
# n = int(input("Enter the last num:..")
#print(f"The sum of the first {n} numbers is {n*(n+1)/2}")

# Задача 2. Калькулятор
import math
a = int(input("The first number:..."))
b = int(input("The second number:..."))
print(f"The sum: {a+b}, \nThe difference: {a-b}, \n"
      f"The multiplication: {a*b},\nThe division: {a/b}, \n"
      f"The division without a trace: {a//b}, \n"
      f"The trace: {a%b}, \nThe extent: {a**b}, \n"
      f"The logarithm: {round(math.log10(a), 2)}")
print(f"A is more than b: {a>b}, \nA is less than b: {a<b}, \n"
      f"B is more or is a: {b>=a}, \nB is less or is a: {b>=a}, \n"
      f"B is not a: {b !=a}, \nB is a: {b == a}")

# Задача 3
x = int(input("Enter the number x..."))
y = int(input("Enter the number y..."))
z = int(input("Enter the number z..."))
f = (((x**5+7)/(abs(-6)*y))**(1./3.))/7-z%y
print(round(f, 3))

# Задача 4 Электрическая цепь
chain_1 = float(input("Введите сопротивление первой цепи:..."))
chain_2 = float(input("Введите сопротивление второй цепи:..."))
print(f"Общее сопротивление = {round(chain_1+chain_2, 1)}")

# Задача 5
a = float(input("Enter a:..."))
b = float(input("Enter b:..."))
m = float(input("Enter m:..."))
n = float(input("Enter n:..."))
x = -(b)/a
if m <= x <= n:
    print(f"x = {x} is in the interval [{m},{n}]")
else:
    print(f"x = {x} is not in the interval [{m}, {n}]")

# Задача 6 Поездка по кругу
d = 123
v = float(input("Enter the velocity:..."))
t = float(input("Enter the time:..."))
result = round((v*t)%123, 0)
print(f"The sportsman is on the {result} km")

# Задача 7 Сумма и произведение цифр в числе
two_digits = int(input("Enter two digits num:..."))
three_digits = int(input("Enter three digits num:..."))

first_digit = two_digits // 10
second_digit = two_digits % 10
print(f"The sum: {first_digit+second_digit}, the multiplication: {first_digit*second_digit}")
first_digit = three_digits // 100
second_digit = (three_digits // 10) % 10
third_digit = three_digits % 10
print(f"The sum: {first_digit+second_digit+third_digit}, the multiplication: {first_digit*second_digit*third_digit}")

# Задача 8. Сортировка трех чисел
a = int(input("The first num:..."))
b = int(input("The second num:..."))
c = int(input("The third num..."))
first = min(a, b, c)
last = max(a, b, c)
mid = a+b+c-first-last
print(f"Sorted list: [{first}, {mid}, {last}].")

# Задача 9. Поменять местами: не всё так просто!
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# Задача 10
command = input("Enter the command's name:...")
print(f"{command} - чемпион!")
print('-'*len(command))
command = command.lower()
print(f"The length - {len(command)},\nIs п in command? {'п' in command},\n"
      f"a repeats {command.count('a')}")

# Задача 11
country = input("Enter the country: ")
capital = input("Enter the capital: ")
print(f"Государство - {country}, столица - {capital}")

# Задача 12
word = 'объектно-ориентированный'
print(word[0:6])
print(word[9:17])
print(word[14:17])
print(word[4]+word[7]+word[5])
print(word[10]+word[12:15]+word[-5])

# Задача 13
# Создать 2 пустых списка
a = []
b = []

# Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
a.append(4.5)
a.append(3.4)
# Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
a.extend([8.7, 1.3])

# Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
b.append(14.5)
b.append(3.4)

# Добавить 2 вещественных числа (8.7, 11.3) в список 'b'с помощью extend
b.extend([8.7, 11.3])

# Вставить целое число 100 на 2-е и 4-е место списка 'a'
a.insert(1, 100)
a.insert(3, 100)

# Вставить целое число 200 на 1-е и 3-е место списка 'b'
b.insert(0, 200)
b.insert(2, 200)

# Вывести списки на экран
print("Исходные списки:")
print(f" 1й: {a}")
print(f" 2й: {b}")

# Удалить первые элементы из списков 'a' и 'b'
del a[0]
del b[0]

# Удалить элемент 100 из списка 'a'
a.remove(100)
# Удалить элемент 200 из списка 'b'
b.remove(200)

# Вывести списки на экран
print("\nПосле удалений:")
print(f" 1й: {a}")
print(f" 2й: {b}")

# Создать множества из списков 'a' и 'b', а также их пересечение
sa = set(a)
sb = set(b)
sa_and_sb = sa&sb
# Вывести экран уникальные элементы каждого списка и общие
print("\nУникальные элементы:")
print(f"1-й: {sa}")
print(f"2-й: {sb}")
print("общие:", sa_and_sb)

# Соединить списки 'a' и 'b'
c = a+b

# Отсортировать список 'c' по возрастанию и убыванию
c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

# Среднее арифметическое элементов списка 'c', расположенных на четных местах
sr_ar = sum(c[1::2])/len(c[1::2])
# Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
sr_geom = (c[::2][0]*c[::2][1])**0.5

# Максимальный и минимальный элементы
c_max = max(c)
c_min = min(c)

# Вывести результаты на экран
print("\nИтоговые:")
print("3-й:", c)
print(f"Сортировка (возр.): {c_asc}")
print(f"Сортировка (убыв.): {c_desc}")
print(f"Ср. арифм. = {sr_ar}, ср. геометр. = {sr_geom}")
print(f"Макс. и мин.: {c_max} {c_min}")


# Задача 14
# 1. Создание словаря

info = {}

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = 'Иванов Иван Иванович'
info["дата_рождения"] = '19/07/2002'
info["место_рождения"] = 'Москва'

# Напечатать словарь
print(info)

# Создать ключ "хобби" со значением = список из строк -
# наименований хобби (например "плавание")
info["хобби"] = ['пение','футбол','гольф']

# Добавить "программирование" в список хобби
info["хобби"].append('программирование')

# Создать ключ "животные" со значением = кортеж из строк -
# имен домашних животных (например "кошка Мурка" и т.д.)
info["животные"] = ('кошка Мурка', 'собака Лайка', 'хомяк Боб')

# Создать ключ "ЕГЭ" и поместить в него пустой словарь
info["ЕГЭ"] = {}

# В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах,
# где ключ - наименование предмета, а значение - количество баллов
info["ЕГЭ"]["Математика"] = 90
info["ЕГЭ"]["Информатика"] = 88
info["ЕГЭ"]["Русский язык"] = 67

# Добавить экзамен, который не был сдан, после чего удалить его
info["ЕГЭ"]["Литература"] = 30
del info["ЕГЭ"]["Литература"]
# Создать ключ "вузы" и поместить в него пустой словарь
info["вузы"] = {}

# В словарь info["вузы"] добавить информацию о вузах,
# где ключ - аббревиатура вуза, а значение -
# количество баллов для специальности, на которую хотели поступить
info["вузы"]["МГТУ"] = 120
info["вузы"]["МГУ"] = 155
info["вузы"]["МИРЭА"] = 123

# 2. Вывод на экран
print("Данные:")
print(info)

# Список экзаменов ЕГЭ в алфавитном порядке
# (используйте метод ``keys()``, преобразовав результат в кортеж)
exams = tuple(sorted(info["ЕГЭ"].keys()))
print("Предметы:", exams)
# Список вузов в алфавитном порядке
uni = tuple(sorted(info["вузы"].keys()))
print("Вузы:", uni)

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# Выделить имя из info["фио"]
name = info["фио"].split()[1]
# Начинается на гласную? (True/False)
starts_with_vowel = name.lower()[0] in "аоеуиюяыэё"
print("* мое имя начинается на гласную букву:", starts_with_vowel)

# Выделить месяц из info["дата_рождения"]
month = info["дата_рождения"].split("/")
# Родился зимой или летом? (True/False)
born_in_winter_or_summer = month[1] in ["01", "02", "12", "06", "07", "08"]
print("* родился летом или зимой:", born_in_winter_or_summer)

# Количество хобби и первое из них
hobbies_count = len(info["хобби"])
first_hobby = info["хобби"][0]
print(f"* у меня {hobbies_count} хобби, первое \"{first_hobby}\"")

# Количество сданных экзаменов
exams_passed = len(tuple(info["ЕГЭ"].keys()))
print(f"* после окончания школы сдавал {exams_passed} экз.")


# Сумма баллов по экзаменам
sum_mark = sum([float(x) for x in info["ЕГЭ"].values()])
print(f"* сумма баллов = {sum_mark}")

# Максимальный балл среди сданных
max_mark = max(tuple(info["ЕГЭ"].values()))
print(f"* макс. балл = {max_mark}")

result_unis = int(sum_mark > info["вузы"]["МГТУ"]) + int(sum_mark > info["вузы"]["МГУ"]) + int(sum_mark > info["вузы"]["МИРЭА"])
print(f"* кол-во вузов в которые прохожу: {result_unis}")




