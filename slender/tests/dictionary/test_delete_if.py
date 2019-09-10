from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestDeleteIf(TestCase):
    
    def test_delete_if_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.delete_if(lambda k, v: k=='a')).to(equal(Dictionary[str, int]({})))

    def test_delete_if_if_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.delete_if(lambda k, v: k=='a')).to(equal(Dictionary[str, int]({'b': 2, 'c': 3})))
    
    def test_delete_if_if_not_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.delete_if(lambda k, v: k=='d')).to(equal(Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})))


