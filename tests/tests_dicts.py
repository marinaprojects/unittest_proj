import unittest
from utils.dicts import get_val


class TestGetVal(unittest.TestCase):

    def test_existing_key(self):
        # Проверяем, что функция возвращает значение для существующего ключа в словаре
        data = {"vcs": "mercurial"}
        key = "vcs"
        expected_result = "mercurial"
        self.assertEqual(get_val(data, key), expected_result)

    def test_default_value(self):
        # Проверяем, что функция возвращает значение по умолчанию, если ключ не найден
        data = {}
        key = "vcs"
        default_value = "git"
        self.assertEqual(get_val(data, key, default_value), default_value)

    def test_custom_default_value(self):
        # Проверяем, что функция возвращает пользовательское значение по умолчанию, если ключ не найден
        data = {}
        key = "vcs"
        custom_default_value = "bazaar"
        self.assertEqual(get_val(data, key, custom_default_value), custom_default_value)


