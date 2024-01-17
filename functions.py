def get_min(a, b):
    return a if a < b else b
def get_max(a,b):
    return b if b > a else a

# Четене на три числа от конзолата
num1 = float(input("Въведете първо число: "))
num2 = float(input("Въведете второ число: "))
num3 = float(input("Въведете трето число: "))

# Намиране на най-малкото число използвайки get_min
min_number = get_min(get_min(num1, num2), num3)
max_number = get_max(get_max(num1, num2), num3)

# Извеждане на резултата
print(f"Най-малкото число е: {min_number}")
print(f"Nai - golqmoto chislo e:{max_number}")
