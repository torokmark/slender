from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestEachValue(TestCase):
    
    def test_each_value_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.each_value(lambda v: v + 'a')).to(equal(Dictionary[str, int]({})))

    def test_each_value_if_dictionary_contains_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.each_value(lambda v: v + 1)).to(equal(Dictionary[str, int]({'a': 2, 'b': 3, 'c': 4})))

    def test_each_value_if_dictionary_contains_elements_and_value_will_be_the_same(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.each_value(lambda v: 'a')).to(equal(Dictionary[str, int]({'a': 'a', 'b': 'a', 'c': 'a'})))

