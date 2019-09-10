from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestMerge(TestCase):
    
    def test_merge_if_both_dictionaries_are_empty(self):
        d1 = Dictionary[str, int]({})
        d2 = Dictionary[str, int]({})
        expect(d1.merge(d2)).to(be_empty)
 
    def test_merge_if_dictionary_is_empty_and_param_contains_elements(self):
        d1 = Dictionary[str, int]({})
        d2 = Dictionary[str, int]({'a': 1, 'b': 2})
        expect(d1.merge(d2)).to(equal(Dictionary[str, int]({'a': 1, 'b': 2})))
 
    def test_merge_if_dictionary_is_not_emtpy_and_param_is_empty(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        d2 = Dictionary[str, int]({})
        expect(d1.merge(d2)).to(equal(Dictionary[str, int]({'a': 1, 'b': 2})))
    
    def test_merge_if_both_dictionaries_contain_different_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        d2 = Dictionary[str, int]({'c': 3, 'd': 4})
        expect(d1.merge(d2)).to(equal(Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})))

    def test_merge_if_both_dictionaries_contain_same_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        d2 = Dictionary[str, int]({'c': 3, 'b': 4})
        expect(d1.merge(d2)).to(equal(Dictionary[str, int]({'a': 1, 'b': 4, 'c': 3})))

    def test_merge_if_both_dictionaries_contain_same_elements_and_callback_is_given(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        d2 = Dictionary[str, int]({'c': 3, 'b': 4})
        expect(d1.merge(d2, lambda k, ov, nv: ov + nv)).to(equal(Dictionary[str, int]({'a': 1, 'b': 6, 'c': 3})))

