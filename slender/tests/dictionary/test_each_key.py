from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestEachKey(TestCase):
    
    def test_each_key_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.each_key(lambda k: k + 'a')).to(equal(Dictionary[str, int]({})))

    def test_each_key_if_dictionary_contains_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.each_key(lambda k: k + 'a')).to(equal(Dictionary[str, int]({'aa': 1, 'ba': 2, 'ca': 3})))

    def test_each_key_if_dictionary_contains_elements_and_key_will_be_the_same(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.each_key(lambda k: 'a')).to(equal(Dictionary[str, int]({'a': 3})))

