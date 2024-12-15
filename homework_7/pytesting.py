import pytest
from usermanager import UserManager


@pytest.fixture
def user_manager():
    """Фікстура для попереднього налаштування UserManager."""
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def test_add_user(user_manager):
    """Тест на додавання користувача"""
    user_manager.add_user("Charlie", 20)
    assert len(user_manager.get_all_users()) == 3
    assert {"name": "Charlie", "age": 20} in user_manager.get_all_users()


def test_remove_user(user_manager):
    """Тест на видалення користувача"""
    user_manager.remove_user("Alice")
    users = user_manager.get_all_users()
    assert len(users) == 1
    assert {"name": "Alice", "age": 30} not in users


def test_get_all_users(user_manager):
    """Тест на відображення користувачів на ім'я"""
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert {"name": "Alice", "age": 30} in users
    assert {"name": "Bob", "age": 25} in users


@pytest.mark.skipif(
    len(UserManager().get_all_users()) < 3,
    reason="Пропуск тесту, якщо користувачів менше трьох"
)
def test_skip_condition(user_manager):
    assert len(user_manager.get_all_users()) >= 3
    