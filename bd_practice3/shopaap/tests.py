from django.test import TestCase
from .utils import add_two_numbers


class Add_two_numbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 2)
        self.assertEqual(result, 4)
