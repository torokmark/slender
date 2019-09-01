from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestMap(TestCase):

    def test_map_if_self_is_empty(self):
        e = Set()
        expect(e.map(lambda x: x % 2 == 0)).to(equal(set()))

    def test_map_with_aritmethic(self):
        e = Set({1, 2, 3, 4})
        expect(e.map(lambda x: x * 2)).to(equal({2, 4, 6, 8}))

    def test_map_with_bool(self):
        e = Set({1, 2, 3, 4, 5})
        expect(e.map(lambda x: x >= 3)).to(equal({False, True}))

    def test_map_lambda_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e.map('...')).to(raise_error(TypeError))




