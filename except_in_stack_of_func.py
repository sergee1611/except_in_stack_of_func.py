def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    counter = (result, incorrect_data)
    return counter


def calculate_average(numbers):
    try:
        int_counter = 0
        for number in numbers:
            if isinstance(number, int):
                int_counter += 1
        average = personal_sum(numbers)[0] / int_counter
        return average
    except ZeroDivisionError:
        average = 0
        return average
    except TypeError:
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
