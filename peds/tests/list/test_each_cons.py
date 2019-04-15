
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestEachCons(TestCase):

    def test_each_cons_if_param_is_equal_to_length(self):
        e = List([1, 2, 3, 4])
        it = e.each_cons(4)
        expect(next(it)).to(equal([1, 2, 3, 4]))

    def test_each_cons_if_param_is_less_length(self):
        e = List([1, 2, 3, 4])
        it = e.each_cons(3)
        expect(next(it)).to(equal([1, 2, 3]))
        expect(next(it)).to(equal([2, 3, 4]))

    def test_each_cons_if_param_is_less_than_zero_raises_error(self):
        e = List([1, 2, 3, 4])
        it = e.each_cons(-1)
        expect(lambda: next(it)).to(raise_error(TypeError))

    def test_each_cons_if_func_is_valid(self):
        e = List([1, 2, 3, 4])
        it = e.each_cons(2, lambda i: print(i))
        expect(next(it)).to(equal(None))

    def test_each_cons_if_param_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        it = e.each_cons('...')
        expect(lambda: next(it)).to(raise_error(TypeError))

    def test_each_cons_if_param_is_int_and_func_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        it = e.each_cons(3, '...')
        expect(lambda: next(it)).to(raise_error(TypeError))

