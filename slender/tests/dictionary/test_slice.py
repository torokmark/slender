from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestSlice(TestCase):
    
    def test_slice_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.slice('a')).to(be_empty)

    def test_slice_if_dictionary_contains_elements_and_not_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.slice('z')).to(be_empty)

    def test_slice_if_dictionary_contains_elements_and_all_keys_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.slice('a', 'b')).to(equal(Dictionary[str, int]({'a': 1, 'b': 2})))

    def test_slice_if_dictionary_contains_elements_and_some_key_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.slice('a', 'b', 'z')).to(equal(Dictionary[str, int]({'a': 1, 'b': 2})))

    

