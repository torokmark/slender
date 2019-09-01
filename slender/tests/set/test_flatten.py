from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestFlatten(TestCase):

    def test_flatten_if_unflatten_set(self):
        e = Set({frozenset({1}), frozenset({2, 3}), 4, frozenset({4, 5, 6, 7})})
        expect(e.flatten().to_set()).to(equal({1, 2, 3, 4, 5, 6, 7}))

    def test_flatten_flat_set(self):
        e = Set({1, 2, 3, 4})
        expect(e.flatten().to_set()).to(equal({1, 2, 3, 4}))

    def test_flatten_if_subset_is_enhanced_set(self):
        e = Set({Set({1, 2, 3}), frozenset({1, 2, 4}), 5, Set({2, 5, 6})})
        expect(e.flatten().to_set()).to(equal({1, 2, 3, 4, 5, 6}))

    def test_flatten_empty_set(self):
        e = Set()
        expect(e.flatten().to_set()).to(equal(set()))



