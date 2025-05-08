import json
import logging
import os
from json import JSONDecodeError
from typing import Union

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
log_file = os.path.join(log_dir, "utils_logs.log")
utils_logger = logging.getLogger("utils_logger")
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def get_operations(data_path: Union[str | None] = None) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список"""
    utils_logger.info("поиск файла со списком операций")
    if not data_path:
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(utils_dir, "..", "data", "operations.json")
    try:
        with open(data_path, "r", encoding="utf-8") as file:
            utils_logger.info("чтение файла со списком операций")
            operations = json.load(file)
            if type(operations) == list:
                utils_logger.info("список операций успешно сформирован")
                return operations
            else:
                utils_logger.warning("файл содержит некорректные данные!")
                return []
    except (ValueError, JSONDecodeError):
        utils_logger.error("файл не может быть прочитан!")
        return []
    except FileNotFoundError:
        utils_logger.error("файл не найден!")
        return []


# Для тестирования
if __name__ == "__main__":
    operations = get_operations()
    print(operations[0])
