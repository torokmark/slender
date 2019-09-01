
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestEachCons(TestCase):

    def test_each_cons_if_param_is_equal_to_length(self):
        e = List([1, 2, 3, 4])
        expect(e.each_cons(4).to_list()).to(equal([[1, 2, 3, 4]]))

    def test_each_cons_if_param_is_less_length(self):
        e = List([1, 2, 3, 4])
        expect(e.each_cons(3).to_list()).to(equal([[1, 2, 3], [2, 3, 4]]))

    def test_each_cons_if_param_is_less_than_zero_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.each_cons(-1).to_list()).to(raise_error(TypeError))

    def test_each_cons_if_param_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.each_cons('...')).to(raise_error(TypeError))


