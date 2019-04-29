from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestDivide(TestCase):

    def test_divide_lambda_creates_subsets(self):
        e = Set({1, 3, 4, 6, 9, 10, 11})
        expect(e.divide(lambda i, j: abs(i - j) == 1).to_set()).to(equal({Set({1}), Set({3, 4}), Set({6}), Set({9, 10, 11})}))

    def test_divide_lambda_creates_single_element_subsets(self):
        e = Set({1, 3, 5, 7, 9})
        print(e.divide(lambda i, j: abs(i - j) == 1))
        expect(e.divide(lambda i, j: abs(i - j) == 1).to_set()).to(equal({Set({1}), Set({3}), Set({5}), Set({7}), Set({9})}))

    def test_divide_if_set_is_empty(self):
        e = Set({1, 2, 3})
        expect(lambda: e.divide('...')).to(raise_error(TypeError))




