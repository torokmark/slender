
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from slender import List 

class TestMin(TestCase):

    def test_min_if_list_of_numbers(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.min()).to(equal(2))

    def test_min_if_list_of_string(self):
        e = List(['apple', 'bear', 'dog', 'plum'])
        expect(e.min()).to(equal('apple'))

    def test_min_if_list_is_empty(self):
        e = List([])
        expect(e.min()).to(equal(None))
     
    def test_min_if_list_is_empty_with_lambda(self):
        e = List([])
        expect(e.min(lambda x: len(x))).to(equal(None))
    
    def test_min_if_compare_with_lambda_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.min(lambda x: len(x))).to(equal('dog'))

    def test_min_if_compare_with_lambda_div(self):
        e = List([1, 2, 3, 4, 5, 6, 7])
        expect(e.min(lambda x: x % 4)).to(equal(4))

    def test_min_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.min('...')).to(raise_error(TypeError))
