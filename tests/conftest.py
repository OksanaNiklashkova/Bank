import pytest

@pytest.fixture()
def bill_info(str_info, nums):
    str_info = ['Maestro', 'Счёт', 'MasterCard', 'Счет', 'Visa Classic', 'Visa Platinum', 'Visa Gold']
    nums = [
        '1596837868705199',
        '64686473678894779589',
        '7158300734726758',
        '35383033474447895560',
        '6831982476737658',
        '8990922113665229',
        '5999414228426353'
    ]
    for i in range(len(str_info)):
        return str_info[i] + ' ' + nums[i]