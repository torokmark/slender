
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestEachSlice(TestCase):

    def test_each_slice_if_param_greater_than_length(self):
        e = List([1, 2, 3, 4])
        expect(e.each_slice(5).to_list()).to(equal([[1, 2, 3, 4]]))

    def test_each_slice_if_param_is_equal_to_length(self):
        e = List([1, 2, 3, 4])
        expect(e.each_slice(4).to_list()).to(equal([[1, 2, 3, 4]]))

    def test_each_slice_if_param_is_less_length(self):
        e = List([1, 2, 3, 4])
        expect(e.each_slice(3).to_list()).to(equal([[1, 2, 3], [4]]))

    def test_each_slice_if_param_is_less_than_zero_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.each_slice(-1)).to(raise_error(TypeError))

    def test_each_slice_if_func_is_valid(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.each_slice(2, lambda i: i * 2).to_list()).to(equal([[2, 4], [6, 8], [10]]))

    def test_each_slice_if_param_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.each_slice('...')).to(raise_error(TypeError))

    def test_each_slice_if_param_is_int_and_func_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.each_slice(3, '...')).to(raise_error(TypeError))
