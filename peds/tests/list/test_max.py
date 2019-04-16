
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from peds import List 

class TestMax(TestCase):

    def test_max_if_list_of_numbers(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.max()).to(equal(5))

    def test_max_if_list_of_string(self):
        e = List(['apple', 'bear', 'dog', 'plum'])
        expect(e.max()).to(equal('plum'))


    def test_max_if_list_is_empty(self):
        e = List([])
        expect(e.max()).to(equal(None))
     
    def test_max_if_list_is_empty_with_lambda(self):
        e = List([])
        expect(e.max(lambda x: len(x))).to(equal(None))
    
    def test_max_if_compare_with_lambda_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.max(lambda x: len(x))).to(equal('caterpillar'))

    def test_max_if_compare_with_lambda_div(self):
        e = List([1, 2, 3, 4, 5, 6, 7])
        expect(e.max(lambda x: x % 4)).to(equal(3))

    def test_max_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.max('...')).to(raise_error(TypeError))

