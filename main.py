import json

from src.filter import make_transactions, normalize_transaction, search_transactions, get_statistic
from src.external_api import get_amount_transaction
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operations
from src.widget import get_date, mask_account_card

def main() -> None:
    """Функция, позволяющая пользователю производить отбор банковских транзакций,
    соответствующих заданным им критериям"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    transactions = make_transactions()
    filtered_transactions = None
    while filtered_transactions is None:
        input_state_of_operations = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: 
        1 - EXECUTED, 
        2 - CANCELED, 
        3 - PENDING.
        => """)
        if input_state_of_operations == "1":
            state = "EXECUTED"
            filtered_transactions = filter_by_state(transactions, state)
        elif input_state_of_operations == "2":
            state = "CANCELED"
            filtered_transactions = filter_by_state(transactions, state)
        elif input_state_of_operations == "3":
            state = "PENDING"
            filtered_transactions = filter_by_state(transactions, state)
        else:
            print(f"Статус операции \"{input_state_of_operations}\" недоступен")

    sorted_by_date_check = input("""Отсортировать операции по дате? 
    1 - Да
    0 - Нет
    => """)
    if bool(int(sorted_by_date_check)):
        flow_check = input("""Отсортировать по возрастанию или по убыванию?
        1 - по убыванию
        0 - по возрастанию
        => """)
        filtered_transactions = sort_by_date(filtered_transactions, flow=bool(flow_check))

    currency_check = input("""Выводить только рублевые транзакции? 
    1 - Да
    0 - Нет
    => """)
    if bool(int(currency_check)):
        filtered_transactions = list(filter_by_currency(filtered_transactions, currency="RUB"))

    search_check = input("""Отфильтровать список транзакций по определенному слову в описании?
    1 - Да
    0 - Нет
    => """)
    if bool(int(search_check)):
        target = input("""Введите слово для поиска
        => """)
        filtered_transactions = search_transactions(filtered_transactions, target)

    transaction_number = len(filtered_transactions)
    if transaction_number > 0:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {transaction_number}")
        for transaction in filtered_transactions:
            print(f"""{get_date(transaction.get("date", ""))} {transaction.get('description')}""")
            if "Перевод" in transaction.get('description'):
                print(
                    f"""{mask_account_card(transaction.get("from"))} -> {mask_account_card(transaction.get("to"))}"""
                )
            else:
                print(f"""{mask_account_card(transaction.get("to"))}""")
            if transaction.get("currency_code") == "RUB":
                transaction["currency_code"] = "руб."
            print(f"""Сумма: {transaction.get("amount")} {transaction.get("currency_code")}\n""")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()

