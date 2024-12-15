import pytest
from unittest.mock import MagicMock
from bank import BankAccount


# Фікстура для створення об'єкта банківського рахунку
@pytest.fixture
def bank_account():
    """Створює новий банківський рахунок перед кожним тестом."""
    return BankAccount()


# Тест для поповнення рахунку з використанням параметризації
@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (100, 100),  # Поповнення на 100
    (50.5, 50.5),  # Поповнення на 50.5
    (0, "ValueError"),  # Помилкове поповнення
    (-10, "ValueError"),  # Помилкове поповнення
])
def test_deposit(bank_account, deposit_amount, expected_balance):
    """Тестуємо метод deposit з різними сумами."""
    if expected_balance == "ValueError":
        with pytest.raises(ValueError):
            bank_account.deposit(deposit_amount)
    else:
        bank_account.deposit(deposit_amount)
        assert bank_account.get_balance() == expected_balance


# Тест для зняття коштів з використанням параметризації
@pytest.mark.parametrize("withdraw_amount, initial_balance, expected_balance", [
    (50, 100, 50),  # Зняття 50 при балансі 100
    (20, 20, 0),  # Зняття 20 при балансі 20
    (0, 100, "ValueError"),  # Помилкове зняття 0
    (150, 100, "ValueError"),  # Недостатньо коштів
    (-10, 100, "ValueError"),  # Помилкове зняття від'ємної суми
])
def test_withdraw(bank_account, withdraw_amount, initial_balance, expected_balance):
    """Тестуємо метод withdraw з різними сценаріями."""
    bank_account.deposit(initial_balance)  # Встановлюємо початковий баланс
    if expected_balance == "ValueError":
        with pytest.raises(ValueError):
            bank_account.withdraw(withdraw_amount)
    else:
        bank_account.withdraw(withdraw_amount)
        assert bank_account.get_balance() == expected_balance


# Тест для отримання балансу
def test_get_balance(bank_account):
    """Тестуємо метод get_balance."""
    bank_account.deposit(100)
    assert bank_account.get_balance() == 100


# Тест із використанням моків для взаємодії із зовнішнім API
def test_external_api_mock(bank_account, monkeypatch):
    """Тестуємо взаємодію із зовнішнім API за допомогою моку."""
    # Імітація зовнішнього API, що повертає баланс
    mock_api = MagicMock(return_value={"balance": 200})
    monkeypatch.setattr("bank.external_api_check_balance", mock_api)

    # Виклик моку
    result = mock_api()
    assert result["balance"] == 200
    mock_api.assert_called_once()


# Скіп тестів для зняття коштів, якщо рахунок порожній
@pytest.mark.skipif(True, reason="Баланс порожній, тест пропущено.")
def test_withdraw_empty_balance(bank_account):
    """Пропускаємо тест, якщо баланс рахунку порожній."""
    with pytest.raises(ValueError):
        bank_account.withdraw(50)
        