from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestDig(TestCase):
    
    def test_dig_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.dig('a', 'b', 'c')).to(equal(None))

    def test_dig_if_keys_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.dig()).to(equal(None))

    def test_dig_if_dictionary_contains_element(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': {'ba':1, 'bb': {'bba': 1, 'bbb': 2}}, 'c': 3})
        expect(d1.dig('a')).to(equal(1))
    
    def test_dig_if_dictionary_contains_embedded_dictionary_with_keys_path(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': {'ba':1, 'bb': {'bba': 1, 'bbb': 2}}, 'c': 3})
        expect(d1.dig('b', 'bb', 'bbb')).to(equal(2))

    def test_dig_if_dictionary_not_contains_key(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': {'ba':1, 'bb': {'bba': 1, 'bbb': 2}}, 'c': 3})
        expect(d1.dig('b', 'bb', 'bbc')).to(equal(None))

    def test_dig_if_dictionary_contains_embedded_dictionary_intermediate_key_is_none(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': {'ba':1, 'bb': {'bba': 1, 'bbb': 2}}, 'c': 3})
        expect(d1.dig('b', 'cbb', 'bbc')).to(equal(None))

    def test_dig_if_dictionary_embedded_key_is_not_dictionary(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': {'ba':1, 'bb': []}, 'c': 3})
        expect(d1.dig('b', 'bb', 'bbc')).to(equal(None))


