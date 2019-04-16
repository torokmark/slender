
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from peds import List 

class TestMaxN(TestCase):

    def test_max_n_if_list_of_numbers(self):
        e = List([5, 3, 5, 2, 4])
        it = e.max_n(2)
        expect(next(it)).to(equal(5))
        expect(next(it)).to(equal(5))

    def test_max_n_if_list_of_string(self):
        e = List(['apple', 'bear', 'dog', 'plum'])
        it = e.max_n(2)
        expect(next(it)).to(equal('dog'))
        expect(next(it)).to(equal('plum'))

    def test_max_n_if_list_is_empty(self):
        e = List([])
        it = e.max_n(2)
        expect(next(it)).to(equal(None))
     
    def test_max_n_if_list_is_empty_with_lambda(self):
        e = List([])
        it = e.max_n(2, lambda x: len(x))
        expect(next(it)).to(equal(None))
    
    def test_max_n_if_compare_with_lambda_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        it = e.max_n(3, lambda x: len(x))
        expect(next(it)).to(equal('plum'))
        expect(next(it)).to(equal('apple'))
        expect(next(it)).to(equal('caterpillar'))

    def test_max_n_if_compare_with_lambda_div(self):
        e = List([1, 2, 3, 4, 5, 6, 7])
        it = e.max_n(3, lambda x: x % 4)
        expect(next(it)).to(equal(6))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(7))

    def test_max_n_if_num_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        it = e.max_n('...', lambda x: len(x))
        expect(lambda: next(it)).to(raise_error(TypeError))

    def test_max_n_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        it = e.max_n(2, '...')
        expect(lambda: next(it)).to(raise_error(TypeError))

