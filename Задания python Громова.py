evgenia, [28.09.2024 14:38]
def analyze(text):
    cleaned_text =''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    words = cleaned_text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] +=1
        else:
            frequency[word] = 1 
                
    sorted_text = sorted(frequency.items(),key=lambda item: (-item[1],item[0]))
    
    for word, count in sorted_text:
        print(f"{word}: {count}")

user_text = input("Enter text: ")
analyze(user_text)

evgenia, [28.09.2024 14:42]
# задание "названия переменных"
print("Hello, world!")

greetings = "Hello, world!"
print(greetings)

evgenia, [28.09.2024 14:46]
# задание "операции числами"
length = 8 
width = 10 
print (length*width)

length = 8 
width = 10 
print (20*width)

print(23*13)

evgenia, [28.09.2024 14:49]
# задание "операторы сравнения(логические операторы)"
print((6 * 6) - 1 == 8 + 1)

print(13 - 7 != (3 * 2) + 1)

print(3 * (2 - 1) == 4 - 1 )

evgenia, [28.09.2024 14:50]
# задание "логические операторы больше и меньше"
print((6 * 6) - 1 >= 8 + 1)

print(13 - 7 <= (3 * 2) + 1)

print(3 * (2 - 1) > 4 - 1 )

evgenia, [28.09.2024 14:54]
# задание "логические переменные"

bool_variable = 'true'
print(type(bool_variable))

bool_variable_2 = True
print(type(bool_variable_2))

evgenia, [28.09.2024 15:08]
# задание "выражения if"

user_name = input("Введите имя:")
dmitriy_check = "Дмитрий, твое рабочее мето находится в другой комнате. Отойди от чужого компьюетра и займись работой!"
others_check = "Добро пожаловать!"
if user_name == "Дмитрий":
    print(dmitriy_check)
else:
    print(others_check)

enter_number = int(input("Введите количество попыток: "))
if enter_number < 3:
    print('Попробуйте еще раз. У вас осталось {} попыток.'.format(3-enter_number))
else:
    print("Вы превысили максимальное число попыток. ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

evgenia, [28.09.2024 15:22]
# задание "логические операторы: and"

statement_one = ((2 + 2 + 2 >= 6) and (-1 * -1 < 0))
statement_two = ((4 * 2 <= 8) and (7 - 1 == 6))
print(statement_one, statement_two)

user_name = input("Введите имя:")
arm = int(input("Введите номер рабочего места: "))

if (user_name == "Дмитрий" and arm == 1) or (user_name == "Ангелина" and arm == 2) or (user_name == "Василий" and arm == 3) or (user_name == "Екатерина" and arm == 4):
    print("Добро пожаловать!")
elif user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз.")
else:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

evgenia, [28.09.2024 15:24]
# задание "логические операторы: or"

statement_one = ((2 - 1 > 3) or (-5 * 2 == -10))
statement_two = ((9 + 5 <= 15) or (7 != 4 + 3))
print(statement_one, statement_two)

evgenia, [28.09.2024 15:27]
# задание "else if оператор"
grade = float(input("Введите средний балл студента: "))

# Проверяем, какой грейд соответствует среднему баллу
if grade >= 4.0:
    print("Грейд: A")
elif grade >= 3.0:
    print("Грейд: B")
elif grade >= 2.0:
    print("Грейд: C")
elif grade >= 1.0:
    print("Грейд: D")
elif grade >= 0.0:
    print("Грейд: F")
else:
    print("Некорректный балл.")

evgenia, [30.09.2024 21:48]
# задание "Конструкция match\case"
grade = float(input("Введите средний балл студента: "))
match grade:
    case grade if grade >= 4.0:
        result = "A"
    case grade if grade >= 3.0:
        result = "B"
    case grade if grade >= 2.0:
        result = "C"
    case grade if grade >= 1.0:
        result = "D"
    case grade if grade >= 0.0:
        result = "F"
    case _:
        result = "Некорректный балл."

print("Грейд студента: {}".format(result))

evgenia, [30.09.2024 21:55]
# задание "функции"
def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " with " + str(row_count) + " lines")
    
create_spreadsheet("Загрузки")

create_spreadsheet("Приложения", 10)

evgenia, [30.09.2024 21:59]
# задание "области видимости"
def define_age(current_year, birth_year):
    age = current_year - birth_year
    return age
   
my_age = define_age(2049, 1993)
dads_age = define_age(2049, 1953)

print("Мне " + str(my_age) + " лет, а моему отцу " + str(dads_age) + " лет")

evgenia, [30.09.2024 22:03]
# задание "несколько возвращаемых значений"
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
    
low_limit, high_limit = get_boundaries(100, 20)

print("Нижний предел:", low_limit, ", верхний предел:", high_limit)

evgenia, [30.09.2024 22:09]
# задание "несколько возвращаемых значений"
def repeat_stuff(stuff, num_repeats = 10):
    return stuff * num_repeats
    
lyrics = repeat_stuff("Row", 3) + "Your Boat."

song = repeat_stuff("Row")

print(song)

evgenia, [30.09.2024 22:11]
# задание "Список – это"
product_list = ["торт", 1]

evgenia, [30.09.2024 22:13]
# задание "Список списков"
household_chemicals = [["стиральный порошок", 1],["средство для мытья посуды", 1]]

evgenia, [30.09.2024 22:18]
# задание "Метод Zip"
names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

evgenia, [30.09.2024 22:20]
# задание "Метод append"
orders = ['маргаритки', 'васильки']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)

evgenia, [30.09.2024 22:24]
# задание "Оператор + при работе со списками"
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print(new_orders)

broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

evgenia, [30.09.2024 22:29]
# задание "Range I"

list1 = range(9)
list2 = range(8)

print(list(list1), list(list2))

evgenia, [30.09.2024 22:32]
# задание "Range II"

list1 = range(5,15,3)
list2 = range(0,40,5)

print(list(list1), list(list2))

evgenia, [30.09.2024 22:37]
# задание "Заключение"

first_names = ['Анна', 'Борис', 'Александр', 'Денис']
age = []
age.append(42)
all_ages = [32, 41, 29] + age

name_and_age = zip(first_names, all_ages)
ids = range(0,4)

print(list(name_and_age), list(ids))

evgenia, [30.09.2024 22:38]
# задание "Длина списка"

list1 = range(2, 20, 2)
list1_len = len(list1)
print(list(list1))
print(list1_len)

list1 = range(2, 20, 3)
list1_len = len(list1)
print(list(list1))
print(list1_len)

evgenia, [30.09.2024 22:41]
# задание "Выбор элементов списка II"

shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))

last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5, last_element)

evgenia, [30.09.2024 22:43]
# задание "Срезы списков"

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0:2]
print(beginning)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0:4]
print(beginning)

middle = suitcase [2:4]
print(middle)

evgenia, [30.09.2024 22:44]
# задание "Срез списков II"

suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase [:3]
print(start)

evgenia, [30.09.2024 22:46]
# задание "Подсчет элементов в списке"

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie',
'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

evgenia, [30.09.2024 22:48]
# задание "Сортировка списков I"

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace'
, '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

evgenia, [30.09.2024 22:50]
# задание "Сортировка списков II"

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

evgenia, [30.09.2024 22:59]
# задание "Выводы"

inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двуспальная кровать', 'двуспальная кровать', 'комод', 'комод', 'стол', 'стол', 'тумбочка', 'тумбочка', 'королевский кровать', 'двуспальная кровать', 'две односпальные кровати', 'две односпальные кровати', 'простыни', 'простыни', 'подушка', 'подушка']
inventory_len = len(inventory)
print(inventory_len)

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory [:3]
print(first_3)

twin_beds = inventory.count("две односпальные кровати")*2
print(twin_beds)

inventory.sort()
print(inventory)

evgenia, [30.09.2024 23:04]
# задание "Расширение списка"

order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
print(order)

evgenia, [30.09.2024 23:05]
# задание "Метод insert"

order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
order.insert(0, "закуска из овощей")
print(order)

evgenia, [30.09.2024 23:06]
# задание "Метод remove"

order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
order.insert(0, "закуска из овощей")
order.remove("салат капрезе")
print(order)

evgenia, [30.09.2024 23:08]
# задание "Метод pop"

order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
order.insert(0, "закуска из овощей")
order.remove("салат капрезе")
order.pop(-1)
print(order)

evgenia, [30.09.2024 23:11]
# задание "Ключевое слово del"

list1 = [0,1,2,3,4,5,6,7]
print(list(list1))
del list1[3:5]
print(list(list1))

evgenia, [30.09.2024 23:11]
# задание "Метод reverse"

x = [15, 11, 13, 12, 14, 10]
x.reverse()
print(x)

evgenia, [30.09.2024 23:13]
# задание "Создание цикла for"

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
    
for game in sport_games:
    print(game)

evgenia, [30.09.2024 23:15]
# задание "Использование range в циклах"

for i in range(5):
    promise = "I will not chew gum in class"
    print(promise)

evgenia, [30.09.2024 23:18]
# задание "Бесконечные циклы"

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)

print(students_period_B)

evgenia, [30.09.2024 23:19]
# задание "Continue"

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
    print(breed) 
    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")  
        break

evgenia, [30.09.2024 23:22]
# задание "Вложенные циклы"

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0 

for shop_sales in sales_data:
    for scoops in shop_sales:
        scoops_sold += scoops

print(scoops_sold)

evgenia, [30.09.2024 23:26]
# задание "Заключение"

single_digits = range(0,10)
squares = []
for i in single_digits:
    print(i)
    squares.append(i  2)
print(squares)

cubes = [digit  3 for digit in single_digits]
print(cubes)

evgenia, [30.09.2024 23:28]
# задание "Строки"

favour_word = "лягушка"
print(favour_word)

evgenia, [30.09.2024 23:32]
# задание "Как получить срез строки"

first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
print(new_account)

temp_password = last_name[2:6]
print(temp_password)

evgenia, [30.09.2024 23:35]
# задание "Конкатенация (объединение строк)"

def account_generator(first_name,last_name):
    first_name_3 = first_name[:3]
    last_name_3 = last_name[:3]
    new_account = first_name_3 + last_name_3
    print(new_account)

account_generator("Виталий","Красилов")

evgenia, [30.09.2024 23:40]
# задание "Измерение длины строки"

def password_generator(first_name, last_name):
    first_part = first_name[-3:]
    last_part = last_name[-3:]
    return first_part + last_part

temp_password = password_generator("Виталий","Красилов")
print(temp_password)

evgenia, [30.09.2024 23:42]
# задание "Отрицательные индексы"

company_motto = "Мечты сбываются"

second_to_last = company_motto[-2]
print(second_to_last)

final_word = company_motto[-4:]
print(final_word)

evgenia, [30.09.2024 23:43]
# задание "Строки неизменяемы (иммутабельны)"

first_name = "Боб"  
fixed_first_name = "Р" + first_name[1:] 
print(fixed_first_name)

evgenia, [30.09.2024 23:45]
# задание "Escape-последовательности"

print("theycallme\"crazy\"91")

evgenia, [30.09.2024 23:49]
# задание "Итерации по строкам"

def get_length(text):
    count = 0
    for letter in text:
        count += 1 
    print(count)
    
get_length("Доброе утро, коллеги")

evgenia, [30.09.2024 23:54]
# задание "Строки и условные выражения (часть первая)"

def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False

print(letter_check("Мир","и"))

evgenia, [30.09.2024 23:59]
# задание "Строки и условные выражения (часть вторая)"

def contains(big_string, little_string):
    return little_string in big_string

def common_letters(string_one, string_two):
    common = [] 
    for letter in string_one:
        if letter in string_two and letter not in common:  
            common.append(letter)  
    return common  

print(contains("watermelon", "melon"))  
print(contains("watermelon", "berry"))  

print(common_letters("banana", "cream"))

evgenia, [01.10.2024 0:10]
# задание "Заключение"

def username_generator(first_name, last_name):
    if len(first_name) <= 3:
        user_first = first_name
    else:
        user_first = first_name[:3]
    if len(last_name) <= 4:
        user_last = last_name
    else:
        user_last = last_name[:4]
    username = user_first + user_last
    return username
    
print(username_generator("Abe", "Simpson"))

def password_generator(username):
    password = username[-1] + username[:-1]
    return password

print(password_generator(username_generator("Abe", "Simpson")))

evgenia, [03.10.2024 18:10]
# задание "Методы форматирования"

poem_title = "spring storm"
poem_title_fixed = poem_title.title()
print(poem_title, poem_title_fixed)

evgenia, [03.10.2024 18:12]
# задание "Разделение строк"

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

evgenia, [03.10.2024 18:16]
# задание "Разделение строк"

authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
author_names = authors.split(', ')
print(author_names)

author_last_names = [name.split()[-1] for name in author_names]

# Выводим список фамилий авторов
print(author_last_names)

evgenia, [03.10.2024 18:23]
# задание "Escape-последовательности"

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

evgenia, [03.10.2024 18:28]
# задание "Создание словаря"

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

print(translations)

evgenia, [03.10.2024 18:30]
# задание "Добавить ключ"

animals_in_zoo = {}
animals_in_zoo["зебры"] = 8 
animals_in_zoo["обезьяны"] = 12
animals_in_zoo["динозавры"] = 0 

print(animals_in_zoo)

evgenia, [03.10.2024 18:32]
# задание "Добавить несколько ключей"

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475,"stringQueen":85739})

print(user_ids)

evgenia, [03.10.2024 18:34]
# задание "Перезаписать значения"

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

evgenia, [03.10.2024 18:37]
# задание "Генерирование словаря"

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

print(drinks_to_caffeine)

evgenia, [03.10.2024 18:44]
# задание "Получить значение по ключу"

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

evgenia, [03.10.2024 18:46]
# задание "Недействительные ключи"

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements["energy"] = "Not a zodiac sign"
print(zodiac_elements["energy"])

evgenia, [03.10.2024 18:49]
# задание "Try/Except для получения ключа"

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30
try:
    drink = "matcha"
    print(caffeine_level[drink])
except KeyError:
    print("Неизвестный уровень кофеина")

evgenia, [03.10.2024 18:51]
# задание "Безопасно получить ключ"

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder",100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash",100000)
print(stack_id)

evgenia, [03.10.2024 18:54]
# задание "Получить все ключи"

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
classes = num_exercises.keys()

print(users)
print(classes)

evgenia, [03.10.2024 18:56]
# задание "Получить все значения"

total_exercises = 0
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

for exercises in num_exercises.values():
    total_exercises += exercises

print(total_exercises)

evgenia, [03.10.2024 18:58]
# задание "Заключение"

tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor",
5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10:
"Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance",
15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}

spread['прошлое'] = tarot[13]  
spread['настоящее'] = tarot[22]  
spread['будущее'] = tarot[10]  

print(spread)

evgenia, [03.10.2024 20:02]
# задание "Итоговое задание"
import csv
data = [{'ФИО': 'Иванов Иван Иванович', 'Должность': 'Менеджер', 'Дата найма': '22.10.2013', 'Оклад': 250000},
        {'ФИО': 'Сорокина Екатерина Матвеевна', 'Должность': 'Аналитик', 'Дата найма': '12.03.2020', 'Оклад': 75000},
        {'ФИО': 'Струков Иван Сергеевич', 'Должность': 'Старший программист', 'Дата найма': '23.04.2012', 'Оклад': 150000},
        {'ФИО': 'Корнеева Анна Игоревна', 'Должность': 'Ведущий программист', 'Дата найма': '22.02.2015', 'Оклад': 120000},
        {'ФИО': 'Старчиков Сергей Анатольевич', 'Должность': 'Младший программист', 'Дата найма': '12.11.2021', 'Оклад': 50000},
        {'ФИО': 'Бутенко Артем Андреевич', 'Должность': 'Архитектор', 'Дата найма': '12.02.2010', 'Оклад': 200000},
        {'ФИО': 'Савченко Алина Сергеевна', 'Должность': 'Старший аналитик', 'Дата найма': '13.04.2016', 'Оклад': 100000}]

with open('employees.csv', 'w') as employees_csv:
    fields = ['ФИО', 'Должность', 'Дата найма', 'Оклад']
    employees_writer = csv.DictWriter(employees_csv, fieldnames=fields)
    employees_writer.writeheader()
    for item in data:
        employees_writer.writerow(item)


def calculate_programmer_bonus(csv_file):
    import csv

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        bonuses = []
        for row in reader:
            if row['Должность'].endswith('программист'):
                bonus = float(row['Оклад']) * 0.03
                bonuses.append({
                    'ФИО': row['ФИО'],
                    'Должность': row['Должность'],
                    'Премия': bonus
                })
    return bonuses

bonuses = calculate_programmer_bonus('employees.csv')
for bonus in bonuses:
    print(f"{bonus['ФИО']} ({bonus['Должность']}): {bonus['Премия']:.2f} руб.")


def calculate_bonus(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        bonuses = []
        for row in reader:
            if 'Екатерина' in row['ФИО'] or 'Анна' in row['ФИО'] or 'Алина' in row['ФИО']:
                bonus = 2000
            else:
                bonus = 2000
            bonuses.append({
                'ФИО': row['ФИО'],
                'Должность': row['Должность'],
                'Премия': bonus
            })
    return bonuses
    
bonuses = calculate_bonus('employees.csv')
for bonus in bonuses:
    print(f"{bonus['ФИО']} ({bonus['Должность']}): {bonus['Премия']} руб.")

from datetime import datetime, date

def calculate_salary_increase(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        salary_increases = []
        for row in reader:
            hire_date = datetime.strptime(row['Дата найма'], '%d.%m.%Y').date()
            today = date.today()
            years_worked = (today - hire_date).days 
            if years_worked >= 10:
                increase_percent = 0.07 
            else:
                increase_percent = 0.05
            new_salary = int(row['Оклад']) * (1 + increase_percent)
            salary_increases.append({
                'ФИО': row['ФИО'],
                'Должность': row['Должность'],
                'Оклад': int(row['Оклад']),
                'Новый оклад': new_salary,
                'Индексация': f"{increase_percent * 100}%"
            })
    return salary_increases
    
salary_increases = calculate_salary_increase('employees.csv')
for increase in salary_increases:
    print(f"{increase['ФИО']}: {increase['Оклад']} - {increase['Новый оклад']} ({increase['Индексация']})")
    def create_vacation_schedule(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        eligible_employees = []
        for row in reader:
            hire_date = datetime.strptime(row['Дата найма'], '%d.%m.%Y').date()
            today = date.today()
            months_worked = (today.year - hire_date.year) * 12 + (today.month - hire_date.month)
            if months_worked >= 6:
                eligible_employees.append({
                    'ФИО': row['ФИО'],
                    'Должность': row['Должность'],
                    'Дата найма': row['Дата найма'],
                    'Оклад': int(row['Оклад']),
                    'Отработано месяцев': months_worked
                })
    return eligible_employees
    
vacation_schedule = create_vacation_schedule('employees.csv')
for employee in vacation_schedule:
    print(f"{employee['ФИО']} ({employee['Должность']}), дата найма: {employee['Дата найма']}, отработано месяцев: {employee['Отработано месяцев']}")

import json
with open('employees.json', 'w') as json_file:
    json.dump(data, json_file)
