
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestReverse(TestCase):

    def test_reverse_if_list_is_not_empty(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.reverse().to_list()).to(equal([5, 4, 3, 2, 1]))

    def test_reverse_if_list_is_empty(self):
        e = List([])
        expect(e.reverse().to_list()).to(equal([]))

    def test_reverse_if_list_contains_lists(self):
        e = List([[1, 2], ['a', 'b'], None, [None, [1, 2, 'a']]])
        expect(e.reverse().to_list()).to(equal([[None, [1, 2, 'a']], None, ['a', 'b'], [1, 2]]))


