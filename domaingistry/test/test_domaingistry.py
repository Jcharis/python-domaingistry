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

    def test_get_subdomain(self):
        self.maxDiff = None
        d = Domain()
        d.name = 'mytests'
        d.category = 'common'
        result = 'string'
        result2 = 90

        self.assertEqual(len(d.get_subdomain()),result2)
        self.assertEqual(type(d.category),type(result))   