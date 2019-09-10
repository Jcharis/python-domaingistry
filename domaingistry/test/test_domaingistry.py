from unittest import TestCase

from domaingistry.domaingistry import Domain


class TestDomain(TestCase):
    def test_result_is_list(self):
        d = Domain()
        d.name = 'mytests'
        d.category = 'common'
        result = []
        self.assertEqual(type(d.generate()),type(result))

    def test_is_string(self):
        d = Domain()
        d.name = 'mytests'
        d.category = 'common'
        result = 'string'
        self.assertEqual(type(d.name),type(result))
        self.assertEqual(type(d.category),type(result))   