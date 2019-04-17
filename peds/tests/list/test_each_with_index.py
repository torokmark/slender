
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestEachWithIndex(TestCase):

    def test_each_with_index_if_param_is_none(self):
        e = List([1, 2, 3, 4, 5])
        it = e.each_with_index()
        expect(next(it)).to(equal([0, 1]))
        expect(next(it)).to(equal([1, 2]))
        expect(next(it)).to(equal([2, 3]))
        expect(next(it)).to(equal([3, 4]))
        expect(next(it)).to(equal([4, 5]))

    def test_each_with_index_if_param_is_const(self):
        e = List([1, 2, 3, 4, 5])
        it = e.each_with_index(start=2)
        expect(next(it)).to(equal([2, 3]))
        expect(next(it)).to(equal([3, 4]))
        expect(next(it)).to(equal([4, 5]))

    def test_each_with_index_if_param_is_none_and_func_is_not_none(self):
        e = List([1, 2, 3, 4])
        it = e.each_with_index(callback=lambda index, item: [index, item * index] )
        expect(next(it)).to(equal([0, 0]))
        expect(next(it)).to(equal([1, 2]))
        expect(next(it)).to(equal([2, 6]))
        expect(next(it)).to(equal([3, 12]))

    def test_each_with_index_if_param_is_const_and_func_is_not_none(self):
        e = List([1, 2, 3, 4])
        it = e.each_with_index(start=2, callback=lambda index, item: [index, item * index] )
        expect(next(it)).to(equal([2, 6]))
        expect(next(it)).to(equal([3, 12]))

    def test_each_with_index_if_param_is_const_func_is_different(self):
        e = List([1, 2, 3, 4])
        it = e.each_with_index(start=2, callback='...')
        expect(lambda: next(it)).to(raise_error(TypeError))


