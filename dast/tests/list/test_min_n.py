
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from dast import List 

class TestMinN(TestCase):

    def test_min_n_if_list_of_numbers(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.min_n(2).to_list()).to(equal([2, 3]))

    def test_min_n_if_list_of_string(self):
        e = List(['apple', 'bear', 'dog', 'plum'])
        expect(e.min_n(2).to_list()).to(equal(['apple', 'bear']))

    def test_min_n_if_list_is_empty(self):
        e = List([])
        expect(e.min_n(2).to_list()).to(equal([]))
     
    def test_min_n_if_list_is_empty_with_lambda(self):
        e = List([])
        expect(e.min_n(2, lambda x: len(x)).to_list()).to(equal([]))
    
    def test_min_n_if_compare_with_lambda_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.min_n(3, lambda x: len(x)).to_list()).to(equal(['dog', 'bear', 'plum']))

    def test_min_n_if_compare_with_lambda_div(self):
        e = List([1, 2, 3, 4, 5, 6, 7])
        expect(e.min_n(3, lambda x: x % 4).to_list()).to(equal([4, 1, 5]))

    def test_min_n_if_num_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.min_n('...', lambda x: len(x))).to(raise_error(TypeError))

    def test_min_n_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.min_n(2, '...')).to(raise_error(TypeError))
