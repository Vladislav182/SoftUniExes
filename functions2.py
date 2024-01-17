def repeat_string(input_str, count):
    return input_str * count

# Четене на входни данни от потребителя
user_input_str = input("Въведете низ: ")
user_input_count = int(input("Въведете брой повторения: "))

# Извикване на функцията и извеждане на резултата
result = repeat_string(user_input_str, user_input_count)
print(f"Резултат: {result}")
