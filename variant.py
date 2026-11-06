raw_input = input("Введите целые числа через пробел: ")

numbers = []
if raw_input.strip():
    for part in raw_input.split():
        numbers.append(int(part))

# Условие варианта 1: чётные числа
selected = []
for num in numbers:
    if num % 2 == 0:
        selected.append(num)

total = sum(selected)
count = len(selected)
sorted_copy = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Отсортированная копия: {sorted_copy}")
