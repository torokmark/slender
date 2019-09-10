from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestDelete(TestCase):

    def test_delete_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.delete('a')).to(equal(None))

    def test_delete_if_dictionary_contains_element_and_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.delete('a')).to(equal(1))
    
    def test_delete_if_dictionary_contains_element_and_not_find_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.delete('d')).to(equal(None))

    def test_delete_if_dictionary_contains_element_and_callback_is_given_and_not_find_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.delete('d', callback=lambda x: x + '---')).to(equal('d---'))


