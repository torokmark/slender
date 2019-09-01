
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestFindAll(TestCase):

    def test_find_all_if_func_is_none(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.find_all().to_list()).to(equal([1, 2, 3, 4, 5]))

    def test_find_all_if_func_is_valid(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.find_all(lambda item: item > 3).to_list()).to(equal([4, 5]))

    def test_find_all_if_func_is_invalid_for_all_items(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.find_all(lambda item: item > 6).to_list()).to(equal([]))

    def test_find_all_if_func_is_different(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.find_all('...')).to(raise_error(TypeError))



