from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestContain(TestCase):

    def setUp(self):
        self.key = 'a'

    def test_contain_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(self.key in d1).to(be_false)

    def test_contain_if_dictionary_not_contains_key(self):
        d1 = Dictionary[str, int]({'b' : 2, 'c' : 3})
        expect(self.key in d1).to(be_false)

    def test_contain_if_dictionary_contains_key(self):
        d1 = Dictionary[str, int]({'a': 1, 'b' : 20, 'c' : 3})
        expect(self.key in d1).to(be_true)

    def test_contain_if_negate(self):
        d1 = Dictionary[str, int]({'b' : 2})
        expect(self.key not in d1).to(be_true)


