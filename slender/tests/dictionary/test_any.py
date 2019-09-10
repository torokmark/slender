from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestAny(TestCase):

    def test_any_if_dictionary_is_empty_and_callback_given(self):
        d1 = Dictionary[str, int]({})
        expect(d1.any(callback=lambda x: len(x) < 5)).to(be_false)

    def test_any_if_dictionary_contains_element_and_callback_given_find_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.any(callback=lambda k, v: k == 'a')).to(be_true)
    
    def test_any_if_dictionary_contains_element_and_callback_given_not_find_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.any(callback=lambda k, v: v % 5 == 0)).to(be_false)

    def test_any_if_callback_is_none(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(lambda: d1.any(None)).to(raise_error(TypeError))

