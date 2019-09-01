from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true

from slender import Set 

class TestEq(TestCase):

    def test_eq_other_not_equal(self):
        e = Set({1, 2, 3, 4})
        o = {3, 4, 5, 6}
        expect(e == o).to(be_false)

    def test_eq_other_not_equal_both_enhanced_set(self):
        e = Set({1, 2, 3})
        o = Set({4, 5, 6})
        expect(e == o).to(be_false)

    def test_eq_other_greater_len(self):
        e = Set({1, 2, 3})
        o = {1, 2, 3, 4}
        expect(e == o).to(be_false)

    def test_eq_other_is_equal(self):
        e = Set({1, 2, 3})
        o = {3, 2, 1}
        expect(e == o).to(be_true)

    def test_eq_other_is_equal_with_enhanced_set(self):
        e = Set({1, 2, 3})
        o = Set({3, 2, 1})
        expect(e == o).to(be_true)

    def test_eq_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e == '...').to(raise_error(TypeError))



