from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestIsdisjoint(TestCase):

    def test_isdisjoint_if_have_intersection(self):
        e = Set({1, 2, 3, 4})
        expect(e.isdisjoint({1, 2, 7})).to(be_false)

    def test_isdisjoint_if_disjoint(self):
        e = Set({1, 2, 3, 4})
        expect(e.isdisjoint({5, 6, 7})).to(be_true)

    def test_isdisjoint_if_set_is_empty(self):
        e = Set({1, 2, 3})
        expect(lambda: e.isdisjoint('...')).to(raise_error(TypeError))




