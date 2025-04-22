import pandas as pd
import os
import csv


def get_transactions_csv(file_path=None):
    if not file_path:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(file_dir, '..', 'data', 'transactions.csv')

    try:
        data_csv = []
        with open(file_path, "r", encoding="UTF-8") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=";")
            for row in reader:
                data_csv.append(row)
        return data_csv
    except FileNotFoundError:
        print("Ошибка! Файл не найден!")


def get_transactions_xlsx(file_path=None):
    if not file_path:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(file_dir, '..', 'data', 'transactions_excel.xlsx')

    try:
        data_frame = pd.read_excel(file_path)
        data_xlsx = data_frame.to_dict(orient="records")
        return data_xlsx
    except FileNotFoundError:
        print("Ошибка! Файл не найден!")

if __name__ == '__main__':
    x = get_transactions_csv()
    print(x[0])
    y = get_transactions_xlsx()
    print(y[0])
