from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestSubtract(TestCase):

    def test_subtract_if_other_subset_of_self_enhanced_set(self):
        e = Set({1, 2, 3, 4})
        o = Set({2, 3})
        expect(e.subtract(o).to_set()).to(equal({1, 4}))

    def test_subtract_if_other_equivalent_to_self(self):
        e = Set({1, 2, 3, 4})
        o = {1, 2, 3, 4}
        expect(e.subtract(o).to_set()).to(equal(set()))

    def test_subtract_if_set_is_empty(self):
        e = Set()
        o = {1, 2}
        expect(e.subtract(o).to_set()).to(equal(set()))




