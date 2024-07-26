import pytest
from string_utils import StringUtils

util = StringUtils()

# Тест для функции capitilize
## Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
@pytest.mark.parametrize("input_string, expected_output", [
    ## Позитивные тесты
    ("skypro", "Skypro"),                 # Приводим первую букву к заглавной
    ("Skypro", "Skypro"),                 # Первая буква уже заглавная
    ("123", "123"),                       # Числа как строка
    ("04 апреля 2023", "04 апреля 2023"), # Строка с пробелами
    ## Негативные тесты
    ("", ""),                             # Пустая строка
    (" ", " ")                            # Строка с пробелом
])
def test_capitilize(input_string, expected_output):
    assert util.capitilize(input_string) == expected_output
def test_capitalize_with_none():
    with pytest.raises(AttributeError):
        util.capitalize(None)              # None

# Тест для функции trim
## Принимает на вход текст и удаляет пробелы в начале, если они есть
@pytest.mark.parametrize("input_string, expected_output", [
    ## Позитивные тесты
    ("   SkyPro", "SkyPro"),              # Удаляем пробелы в начале строки
    ("SkyPro", "SkyPro"),                 # Пробелов в начале нет
    ("123", "123"),                       # Числа как строка
    ("04 апреля 2023", "04 апреля 2023"), # Строка с пробелами
    ## Негативные тесты
    ("", ""),                             # Пустая строка
    (" ", "")                             # Пробелы в начале строки
])
def test_trim(input_string, expected_output):
    assert util.trim(input_string) == expected_output
def test_trim_with_none():
    with pytest.raises(AttributeError):
        util.trim(None)                    # None

# Тест для функции to_list
# # Принимает на вход текст с разделителем и возвращает список строк.
@pytest.mark.parametrize("input_string, input_delimeter, expected_output", [
    ## Позитивные тесты
    ("a,b,c,d", None, ['a', 'b', 'c', 'd']),                     # Разделяем строку с разделителем ",", delimeter не указан
    ("1:2:3", ":", ["1", "2", "3"]),                             # Разделяем строку с разделителем ":"
    ("gfdboiwoujuiwjiwbnwrn", None, ["gfdboiwoujuiwjiwbnwrn"]),  # Текст без пробелов и разделителя
    ("123", ".", ["123"]),                                       # Числа как строка
    ## Негативные тесты
    ("", "любой", []),                                           # Пустая строка
    (" ", " ", [])                                               # Пробелы в строке
])
def test_to_list(input_string, input_delimeter, expected_output):
    assert util.to_list(input_string, input_delimeter) == expected_output
def test_to_list_no_delimetr():
    assert util.to_list("a,b,c,d") == ['a', 'b', 'c', 'd']
def test_to_list_with_none():
    with pytest.raises(AttributeError):
        util.to_list(None)                                       # None

# Тест для функции contains
## Возвращает `True`, если строка содержит искомый символ и `False` - если нет
@pytest.mark.parametrize("input_string, input_symbol, expected_output", [
    ## Позитивные тесты
    ("SkyPro", "S", True),     # Символ есть в строке
    ("SkyPro", "U", False),    # Символ отсутствует в строке
    ## Негативные тесты
    ("", "", True),            # Пустая строка
    (" ", " ", True)           # Строка с пробелом
])
def test_contains(input_string, input_symbol, expected_output):
    assert util.contains(input_string, input_symbol) == expected_output
def test_contains_with_none():
    with pytest.raises(TypeError):
        util.contains(None)    # None

# Тест для функции delete_symbol
## Удаляет все подстроки из переданной строки
@pytest.mark.parametrize("input_string, input_symbol, expected_output", [
    ## Позитивные тесты
    ("SkyPro", "k", "SyPro"),                 # Удаляем символ 1 символ
    ("123", "12", "3"),                       # Удаляем символы из строки с числами
    ("04 апреля 2023", "еля ", "04 апр2023"), # Удаляем несколько символов, чтрока с пробелом
    ("SkyPro", "QA Studio", "SkyPro"),        # Подстроки нет в строке
    ## Негативные тесты
    ("Pro", "SkyPro", "Pro"),                 # Подстрока длиннее строки
    ("", "SkyPro", ""),                       # Пустая строка
    (" ", "SkyPro", " ")                      # Строка с пробелом
])
def test_delete_symbol(input_string, input_symbol, expected_output):
    assert util.delete_symbol(input_string, input_symbol) == expected_output
def test_delete_symbol_with_none():
    with pytest.raises(TypeError):
        util.delete_symbol(None)              # None


# Тест для функции starts_with
## Возвращает `True`, если строка начинается с заданного символа и `False` - если нет 
@pytest.mark.parametrize("input_string, input_symbol, expected_output", [
    ## Позитивные тесты
    ("SkyPro", "S", True),          # Строка начинается с заданного символа
    ("SkyPro", "P", False),         # Строка НЕ начинается с заданного символа
    ("123", "1", True),             # Строка начинается с заданного числа
    ("123", "9", False),            # Строка НЕ начинается с заданного числа
    ("04 апреля 2023", "0", True),  # Строка (буквы, цифры, пробелы) начинается с заданного символа
    ("04 апреля 2023", "а", False), # Строка (буквы, цифры, пробелы) НЕ начинается с заданного символа
    ## Негативные тесты
    ("", "", True),                 # Пустая строка
    (" ", " ", True)                # Строка содержит пробел
])
def test_starts_with(input_string, input_symbol, expected_output):
    assert util.starts_with(input_string, input_symbol) == expected_output
def test_starts_with_none():
    with pytest.raises(TypeError):
        util.starts_with(None)      # None

# Тест для функции end_with
## строка заканчивается заданным символом - Возвращает `True'
@pytest.mark.parametrize("input_string, input_symbol, expected_output", [
    ## Позитивные тесты
    ("SkyPro", "o", True),           # Строка заканчивается заданным символом
    ("SkyPro", "P", False),          # Строка НЕ заканчивается заданным символом
    ("123", "3", True),              # Строка заканчивается заданным числом
    ("123", "9", False),             # Строка НЕ заканчивается заданным числом
    ("04 апреля 2023", "3", True),   # Строка (буквы, цифры, пробелы) заканчивается заданным символом
    ("04 апреля 2023", "4", False),  # Строка (буквы, цифры, пробелы) НЕ заканчивается заданным символом
    ## Негативные тесты
    ("", "", True),                  # Пустая строка
    (" ", " ", True)                 # Строка с пробелом
])
def test_end_with(input_string, input_symbol, expected_output):
    assert util.end_with(input_string, input_symbol) == expected_output
def test_end_with_none():
    with pytest.raises(TypeError):
        util.end_with(None)          # None

# Тест для функции is_empty
## Возвращает `True`, если строка пустая и `False` - если нет
@pytest.mark.parametrize("input_string, expected_output", [    
    ## Позитивные тесты
    ("", True),                 # Пустая строка
    (" ", True),                # 1 пробел в строке
    ("        ", True),         # Много пробелов в строке
    ("S", False),               # Строка с 1 символом
    ("Тест", False),            # Строка несколькими символами
    ("123", False),             # Числа как строка
    ("04 апреля 2023", False)   # Строка с пробелами
])
def test_is_empty(input_string, expected_output):
    assert util.is_empty(input_string) == expected_output
    ## Негативные тесты
def test_is_empty_with_none():
     with pytest.raises(AttributeError):
         util.is_empty(None)     # None
         util.is_empty([1,8])    # Тип данных не строка

# Тест для функции list_to_string
## Преобразует список элементов в строку с указанным разделителем
@pytest.mark.parametrize("input_lst, input_joiner, expected_output", [
    ## Позитивные тесты
    ([1,2,3,4], None, "1, 2, 3, 4"),     # Преобразуем список в строку без разделителя
    (["Sky", "Pro"], "-", "Sky-Pro"),  # Преобразуем список в строку с разделителем "-"
    ([" ", " ", " "], "", "   "),      # Список с пробелами
    ([], "", ""),                      # Пустой список
])
def test_list_to_string(input_lst, input_joiner, expected_output):
    assert util.list_to_string(input_lst, input_joiner) == expected_output
    ## Негативные тесты
def test_list_to_string_no_list():
    with pytest.raises(TypeError):
        util.list_to_string({1, 2, 3}) # Не List