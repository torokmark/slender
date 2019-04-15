
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestSelect(TestCase):

    def test_select_if_func_is_none(self):
        e = List([1, 2, 3, 4, 5])
        it = e.select()
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(5))

    def test_select_if_func_is_valid(self):
        e = List([1, 2, 3, 4, 5])
        it = e.select(lambda item: item > 3) 
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(5))

    def test_select_if_func_is_invalid_for_all_items(self):
        e = List([1, 2, 3, 4, 5])
        it = e.select(lambda item: item > 6)
        expect(lambda: next(it)).to(raise_error(StopIteration))

    def test_select_if_func_is_different(self):
        e = List([1, 2, 3, 4])
        it = e.select('...')
        expect(lambda: next(it)).to(raise_error(TypeError))



