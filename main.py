from src.widget import get_date, mask_account_card

# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305

input_information = str(input("Введите номер карты или счета: "))
print(mask_account_card(input_information))

# 2024-03-11T02:26:18.671407

input_date = str(input("Введите данные о дате и времени: "))
print(get_date(input_date))