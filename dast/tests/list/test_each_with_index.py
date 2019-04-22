
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List

class TestEachWithIndex(TestCase):

    def test_each_with_index_if_param_is_none(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.each_with_index().to_list()).to(equal([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]))

    def test_each_with_index_if_param_is_const(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.each_with_index(start=2).to_list()).to(equal([[2, 3], [3, 4], [4, 5]]))

    def test_each_with_index_if_param_is_none_and_func_is_not_none(self):
        e = List([1, 2, 3, 4])
        expect(e.each_with_index(callback=lambda index, item: [index, item * index] ).to_list()).to(equal([[0, 0], [1, 2], [2, 6], [3, 12]]))

    def test_each_with_index_if_param_is_const_and_func_is_not_none(self):
        e = List([1, 2, 3, 4])
        expect(e.each_with_index(start=2, callback=lambda index, item: [index, item * index] ).to_list()).to(equal([[2, 6], [3, 12]]))

    def test_each_with_index_if_param_is_const_func_is_different(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.each_with_index(start=2, callback='...')).to(raise_error(TypeError))


