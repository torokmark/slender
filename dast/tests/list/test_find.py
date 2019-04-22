
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List

class TestFind(TestCase):


    def test_find_if_default_none_and_func_not_none(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find(lambda x: x % 2 == 0)
        expect(act).to(equal(2))

    def test_find_if_default_and_func_not_none(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find(default=100, callback=lambda x: x == 0)
        expect(act).to(equal(100))

    def test_find_if_default_applied_func_results_no_match(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find(default=100, callback=lambda x: x == 0)
        expect(act).to(equal(100))

    def test_find_if_func_is_different_raises_error(self):
        e = List([1, 2, 3, 4, 5])
        expect(lambda: e.find(default=0, callback='...')).to(raise_error(TypeError))



