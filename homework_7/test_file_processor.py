import pytest
from file_prog import FileProcessor


def test_file_write_read(tmpdir):
    """Перевіряє запис і читання даних із тимчасового файлу."""
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_empty_string_write_read(tmpdir):
    """Перевіряє запис і читання порожнього рядка."""
    file = tmpdir.join("emptyfile.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)
    assert content == ""


def test_large_data_write_read(tmpdir):
    """Перевіряє запис і читання великих обсягів даних."""
    file = tmpdir.join("largefile.txt")
    large_data = "A" * 10**6  # 1 мільйон символів
    FileProcessor.write_to_file(file, large_data)
    content = FileProcessor.read_from_file(file)
    assert content == large_data


def test_file_not_found(tmpdir):
    """Перевіряє поведінку при спробі читання неіснуючого файлу."""
    non_existent_file = tmpdir.join("nofile.txt")
    with pytest.raises(FileNotFoundError, match=f"Файл {non_existent_file} не знайдено."):
        FileProcessor.read_from_file(non_existent_file)


def test_append_to_file(tmpdir):
    """Перевіряє, що файл перезаписується, а не додається до існуючого."""
    file = tmpdir.join("appendtest.txt")
    FileProcessor.write_to_file(file, "First Line")
    FileProcessor.write_to_file(file, "Second Line")  # Перезапис
    content = FileProcessor.read_from_file(file)
    assert content == "Second Line"
