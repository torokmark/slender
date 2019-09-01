
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestSelect(TestCase):

    def test_select_if_func_is_valid(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.select(lambda item: item > 3).to_list()).to(equal([4, 5]))

    def test_select_if_func_is_invalid_for_all_items(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.select(lambda item: item > 6).to_list()).to(equal([]))

    def test_select_if_func_is_different(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.select('...')).to(raise_error(TypeError))




