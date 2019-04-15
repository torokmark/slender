
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestFind(TestCase):


    def test_find_if_default_and_func_none(self):
        e = List([1, 2, 3, 4, 5])
        it = e.find()
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(5))

    def test_find_if_default_none_and_func_not_none(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find(lambda x: x % 2 == 0)
        expect(act).to(equal(2))

    def test_find_if_default_and_func_not_none(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find(lambda: 100, lambda x: x == 0)
        expect(act).to(equal(100))

    def test_find_if_default_applied_func_results_no_match(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find(lambda: 100, lambda x: x == 0)
        expect(act).to(equal(100))

    def test_find_if_default_and_func_none_overiterate_raises_error(self):
        e = List([1, 2])
        it = e.find()
        next(it), next(it)
        expect(lambda: next(it)).to(raise_error(StopIteration))

    def test_find_if_default_is_different_raises_error(self):
        e = List([1, 2, 3, 4, 5])
        expect(lambda: e.find('...', lambda x: x % 2 == 0)).to(raise_error(TypeError))

    def test_find_if_func_is_different_raises_error(self):
        e = List([1, 2, 3, 4, 5])
        expect(lambda: e.find(lambda: 0, '...')).to(raise_error(TypeError))



