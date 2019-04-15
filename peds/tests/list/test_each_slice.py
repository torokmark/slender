
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestEachSlice(TestCase):

    def test_each_slice_if_param_greater_than_length(self):
        e = List([1, 2, 3, 4])
        it = e.each_slice(5)
        expect(next(it)).to(equal([1, 2, 3, 4]))

    def test_each_slice_if_param_is_equal_to_length(self):
        e = List([1, 2, 3, 4])
        it = e.each_slice(4)
        expect(next(it)).to(equal([1, 2, 3, 4]))

    def test_each_slice_if_param_is_less_length(self):
        e = List([1, 2, 3, 4])
        it = e.each_slice(3)
        expect(next(it)).to(equal([1, 2, 3]))
        expect(next(it)).to(equal([4]))

    def test_each_slice_if_param_is_less_than_zero_raises_error(self):
        e = List([1, 2, 3, 4])
        it = e.each_slice(-1)
        expect(lambda: next(it)).to(raise_error(TypeError))

    def test_each_slice_if_func_is_valid(self):
        e = List([1, 2, 3, 4, 5])
        it = e.each_slice(2, lambda i: i * 2)
        expect(next(it)).to(equal([2, 4]))
        expect(next(it)).to(equal([6, 8]))
        expect(next(it)).to(equal([10]))

    def test_each_slice_if_param_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        it = e.each_slice('...')
        expect(lambda: next(it)).to(raise_error(TypeError))

    def test_each_slice_if_param_is_int_and_func_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        it = e.each_slice(3, '...')
        expect(lambda: next(it)).to(raise_error(TypeError))
