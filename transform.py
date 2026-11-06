raw_input = input("Введите целые числа через пробел: ")

numbers = []
if raw_input.strip():
    for part in raw_input.split():
        numbers.append(int(part))

# Создаём новый список, заменяя отрицательные на их модули
new_numbers = []
for num in numbers:
    if num < 0:
        new_numbers.append(-num)
    else:
        new_numbers.append(num)

print(f"Исходный список: {numbers}")
print(f"Новый список: {new_numbers}")
