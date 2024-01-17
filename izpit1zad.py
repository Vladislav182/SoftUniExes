import random

def main():
    try:
        p = int(input("Въведете брой елементи (цяло число между 30 и 100): "))
        if not (30 < p < 100):
            raise ValueError("Броят на елементите трябва да бъде между 30 и 100.")
    except ValueError as ve:
        print(f"Грешка: {ve}")
        return

    # Генериране на списък със случайни числа
    numbers = [random.randint(20, 600) for _ in range(p)]

    # Намиране на броя на елементите, чиято цифра на единиците е кратна на 2
    count_even_units = sum(1 for num in numbers if num % 10 == 0 or num % 10 == 2 or num % 10 == 4 or num % 10 == 6 or num % 10 == 8)

    # Намиране на индекса на минималния елемент, който има остатък 3 при целочислено деление на 7
    min_index = min((index, num) for index, num in enumerate(numbers) if num % 7 == 3)[0]

    # Извеждане на резултатите
    print(f"Списък: {numbers}")
    print(f"Брой на елементите с цифра на единиците, кратна на 2: {count_even_units}")
    print(f"Индекс на минималният елемент с остатък 3 при деление на 7: {min_index}")

if __name__ == "__main__":
    main()
