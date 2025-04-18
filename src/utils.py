import json
import os
from json import JSONDecodeError
from typing import Union

from src.decorators import log


@log(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "my_log.txt"))
def get_operations(data_path: Union[str | None] = None) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список"""
    if not data_path:
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(utils_dir, "..", "data", "operations.json")
    try:
        with open(data_path, "r", encoding="utf-8") as file:
            operations = json.load(file)
            if type(operations) == list:
                return operations
            else:
                return []
    except (ValueError, FileNotFoundError, JSONDecodeError):
        return []

# print(len(get_operations()))
