""""list  = [12, 45, 67, 23, 89, 34, 78]

max_num = list[0]

for число in list:
    if число > max_num:
        max_num = число

print("Най-голямото число в списъка е:", max_num)"""

"""list = ['Vladislav', 'Mila', 'Dimitar']

max_word = list[0]

for word in  list:
    if word > max_word:
        max_word = word
print(max_word)"""


"""l1 = [0, 12,13,14,15,5]
l2 = [0, 23,13,15,8,6]

elements = []

for element in l1:
    if element in l2:
        elements.append(element)

print("Общите елементи са:", elements)"""

"""l = [0,1,2,3,4,5,6,7,8,9,10]
odd = []
even = []
for element in l:
    if element % 2 == 0:
        odd.append(element)
    else:
        even.append(element)

print(f"Chetni: {odd}")
print(f"Nechetni {even}")"""

"""def намери_подсписъци(списък):
    подсписъци = []

    for дължина in range(1, len(списък) + 1):
        for начало in range(len(списък) - дължина + 1):
            край = начало + дължина
            подсписъци.append(списък[начало:край])

    return подсписъци

# Пример
списък = [1, 2, 3]

всички_подсписъци = намери_подсписъци(списък)

print("Всички подсписъци на списъка", списък, "са:")
for подсписък in всички_подсписъци:
    print(подсписък)"""



"""def елементи_над_средната(списък):
    средна = sum(списък) / len(списък)
    над_средната = [елемент for елемент in списък if елемент > средна]
    return над_средната

# Пример
списък = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

елементи = елементи_над_средната(списък)

print("Елементите по-големи от средната стойност са:", елементи)"""



# Дефиниране на речник с данни за хората
"""people_data = {
    'Иван': 30,
    'Мария': 22,
    'Петър': 28,
    'Анна': 26,
    'Георги': 35
}

# Намиране на хората над 25 години
people_over_25 = {name: age for name, age in people_data.items() if age > 25}

# Извеждане на резултата
print("Хора на възраст над 25 години:")
for name, age in people_over_25.items():
    print(f"{name}: {age} години")"""

# Дефиниране на речник с данни за растения и време на цъфтеж
"""plants_data = {
    'Роза': 'пролет',
    'Лале': 'пролет',
    'Слънчоглед': 'лято',
    'Хризантема': 'есен',
    'Лавандула': 'лято',
    'Магнолия': 'пролет',
    'Клен': 'есен'
}

# Въвеждане на времето на годината за търсене
desired_season = input("Въведете времето на годината (пролет, лято, есен): ").lower()

# Намиране на растенията, които цъфтят през зададеното време на годината
matching_plants = [plant for plant, season in plants_data.items() if season == desired_season]

# Извеждане на резултата
if matching_plants:
    print(f"Растения, цъфтящи през {desired_season} са:")
    for plant in matching_plants:
        print(plant)
else:
    print(f"Няма растения, цъфтящи през {desired_season}.")"""


"""# Дефиниране на речник с думи
words_dict = {
    'apple': 'ябълка',
    'banana': 'банан',
    'cherry': 'череша',
    'date': 'дател',
    'fig': 'смокиня',
    'grape': 'грозде',
    'kiwi': 'киви'
}

# Въвеждане на буквата за търсене
desired_letter = input("Въведете буква за търсене: ").lower()

# Намиране на думите, които съдържат зададената буква
matching_words = [word for word in words_dict if desired_letter in word]

# Извеждане на резултата
if matching_words:
    print(f"Думи, съдържащи буквата '{desired_letter}':")
    for word in matching_words:
        print(f"{word}: {words_dict[word]}")
else:
    print(f"Няма думи, съдържащи буквата '{desired_letter}'.")"""

"""import random
def generate_random_inputs():
    return random.randint(1, 100)
def check_input(value):
    random_value = generate_random_inputs()
    print(f"Generated random input: {random_value}")
    result = check_input(random_value)
    print(f"check result : {result}")"""

"""age = float(input())
gender = str(input())

if age < 16:
    if gender == 'm':
        print("Master")
    elif gender == 'f':
        print("Miss")
else:
    if age > 16:
        if gender == 'm':
            print("Mr")
        elif gender == 'f':
            print("Ms")"""

product = str(input())
town = str(input())
quantity = int(input())

if town == 'Sofia':
    if product =='coffe':
        print(quantity * 0.50)
    elif product == 'water':
        print(quantity * 0.80)
    elif product == 'beer':
        print(quantity * 1.20)
    elif product == 'sweets':
        print(quantity * 1.45)
    elif product == 'peanuts':
        print(quantity * 1.60)

