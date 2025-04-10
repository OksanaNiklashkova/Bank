"""декоратор log, который будет автоматически регистрировать детали
выполнения функций, такие как: время вызова, имя функции,
передаваемые аргументы, результат выполнения и информация об ошибках"""

import datetime


def log(filename=None):
    def decorator_1(func):
        def wrapper(*args, **kwargs):
            # Формируем информацию о запуске функции
            mark = ""
            start_time = datetime.datetime.now()
            log_entry = [f"{func.__name__} started with arguments: {args}, {kwargs}", ]

            try:
                # Вызываем функцию и получаем результат
                result = func(*args, **kwargs)

                if result:
                    mark = "OK"

                # Формируем информацию об успешном выполнении
                end_time = datetime.datetime.now()
                log_entry.extend([
                    f"Execution time: {end_time - start_time}",
                    f"{func.__name__} ended -> {mark}",
                    f"Results: {result}"
                ])

                # Объединяем все строки лога
                full_log = "\n".join(log_entry) + "\n"

                # Записываем лог в файл или выводим в консоль
                if filename:
                    with open(filename, "a") as file:
                        file.write(full_log)
                else:
                    print(full_log)

                return result

            except Exception as e:
                # Формируем информацию об ошибке
                error_time = datetime.datetime.now()
                log_entry.extend([
                    f"{error_time} - {func.__name__} raised an error.",
                    f"Error type: {type(e).__name__}",
                    f"Error message: {str(e)}",
                    f"Execution time before error: {error_time - start_time}"
                ])

                # Объединяем все строки лога
                full_log = "\n".join(log_entry) + "\n"

                # Записываем лог в файл или выводим в консоль
                if filename:
                    with open(filename, "a") as file:
                        file.write(full_log)
                else:
                    print(full_log)

                # Пробрасываем исключение дальше
                raise
        return wrapper
    return decorator_1

# print(log(get_mask_card_number('7158300734726758')))