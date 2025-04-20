import logging
import os

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
log_file = os.path.join(log_dir, "masks_logs.log")
masks_logger = logging.getLogger("masks_logger")
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    masks_logger.info("Запуск функции маскировки номера карты")
    try:
        card_number = card_number.replace(" ", "")
        masks_logger.debug("Проверка полученных для обработки данных")
        if card_number.isdigit() and len(card_number) == 16:
            masks_logger.info("Маскировка номера карты прошла успешно")
            masked_number = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
            return masked_number
        else:
            masks_logger.warning("Входные данные не могут быть обработаны корректно!")
            return "Проверьте правильность введенного номера карты!"
    except (TypeError, AttributeError):
        masks_logger.error("Входные данные имеют неверный формат!")
        return "Введены некорректные данные!"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""
    masks_logger.info("Запуск функции маскировки номера счета")
    try:
        account_number = account_number.replace(" ", "")
        masks_logger.debug("Проверка полученных для обработки данных")
        if account_number.isdigit() and len(account_number) == 20:
            masks_logger.info("Маскировка номера счета прошла успешно")
            masked_account = "**" + account_number[-4:]
            return masked_account
        else:
            masks_logger.warning("Входные данные не могут быть обработаны корректно!")
            return "Проверьте правильность введенного номера счета!"
    except (TypeError, AttributeError):
        masks_logger.error("Входные данные имеют неверный формат!")
        return "Введены некорректные данные!"


if __name__ == "__main__":
    print(get_mask_card_number("1596837868705199"))
    print(get_mask_card_number("159683786870519"))
    print(get_mask_card_number(159683786870519))
    print(get_mask_account("12751596837868705199"))
    print(get_mask_account("1596837868705199"))
    print(get_mask_account(1596837868705199))
