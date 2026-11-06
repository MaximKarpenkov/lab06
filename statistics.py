raw_input = input("Введите целые числа через пробел: ")

if not raw_input.strip():
    print("Нет данных")
else:
    numbers = []
    for part in raw_input.split():
        numbers.append(int(part))

    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / count

    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")

