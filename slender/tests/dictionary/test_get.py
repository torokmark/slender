from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestGet(TestCase):
    
    def test_get_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.get('a')).to(equal(None))
    
    def test_get_if_dictionary_is_empty_and_callback_is_given(self):
        d1 = Dictionary[str, int]({})
        expect(d1.get('a', lambda k: k + '---')).to(equal('a---'))
    
    def test_get_if_dictionary_contains_elements_and_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.get('a')).to(equal(1))

    def test_get_if_dictionary_contains_elements_and_not_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.get('z')).to(equal(None))

    def test_get_if_dictionary_contains_elements_and_not_finds_match_and_callback_is_given(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.get('z', lambda k: 'apple')).to(equal('apple'))



