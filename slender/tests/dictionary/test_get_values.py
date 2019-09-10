from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestGetValues(TestCase):
    
    def test_get_values_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(lambda: d1.get_values('a', 'b')).to(raise_error(KeyError))
    
    def test_get_values_if_dictionary_is_empty_and_callback_is_given(self):
        d1 = Dictionary[str, int]({})
        expect(d1.get_values('a', 'b', callback=lambda k: k.upper())).to(equal(['A', 'B']))

    def test_get_values_if_dictionary_contains_elements_and_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.get_values('a', 'b')).to(equal([1, 2]))

    def test_get_values_if_dictionary_contains_elements_and_not_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(lambda: d1.get_values('a', 'g')).to(raise_error(KeyError))

    def test_get_values_if_dictionary_contains_elements_and_not_finds_match_and_callback_is_given(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.get_values('a', 'g', callback=lambda k: k.upper())).to(equal([1, 'G']))

