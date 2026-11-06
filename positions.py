raw_input = input("Введите целые числа через пробел: ")

if not raw_input.strip():
    print("Нет данных")
else:
    numbers = []
    for part in raw_input.split():
        numbers.append(int(part))

    maximum = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)

    print(f"Позиции максимума: {positions}")
