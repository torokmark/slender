from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestDifference(TestCase):

    def test_difference_if_other_subset_of_self_enhanced_set(self):
        e = Set({1, 2, 3, 4})
        o = Set({2, 3})
        expect(e.difference(o).to_set()).to(equal({1, 4}))

    def test_difference_if_other_equivalent_to_self(self):
        e = Set({1, 2, 3, 4})
        o = {1, 2, 3, 4}
        expect(e.difference(o).to_set()).to(equal(set()))

    def test_difference_if_set_is_empty(self):
        e = Set()
        o = {1, 2}
        expect(e.difference(o).to_set()).to(equal(set()))




