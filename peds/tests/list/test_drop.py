
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestDrop(TestCase):

    def test_drop_if_param_greater_than_length_returns_empty(self):
        e = List([1, 2, 3, 4])
        act = e.drop(6)
        expect(act).to(equal([]))

    def test_drop_if_param_is_between_zero_and_length_returns_part(self):
        e = List([1, 2, 3, 4])
        act = e.drop(2)
        expect(act).to(equal([3, 4]))

    def test_drop_if_param_is_less_than_zero_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.drop(-1)).to(raise_error(TypeError))

    def test_drop_if_param_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.drop('...')).to(raise_error(TypeError))


