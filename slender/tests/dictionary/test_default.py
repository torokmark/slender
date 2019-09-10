from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestDefault(TestCase):

    def test_default_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        d1.default('---')
        expect(d1['a']).to(equal('---'))

    def test_default_if_dictionary_not_contains_none_element(self):
        d1 = Dictionary[str, int]({'b': 2, 'c': 3})
        d1.default('---')
        expect(d1['a']).to(equal('---'))
 
    def test_default_if_dictionary_contains_none_element(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        d1.default('---')
        expect(d1['a']).to(equal(1))
    
