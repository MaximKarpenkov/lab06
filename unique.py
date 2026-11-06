raw_input = input("Введите целые числа через пробел: ")

numbers = []
if raw_input.strip():
    for part in raw_input.split():
        numbers.append(int(part))

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print(f"Без повторов: {unique}")
