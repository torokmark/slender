from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestIspropersubset(TestCase):

    def test_ispropersubset_self_is_not_proper_subset_of_other_enhanced_set(self):
        e = Set[int]({1, 2, 3, 4, 5})
        o = Set[int]({1, 4, 2, 3, 5})
        expect(e.ispropersubset(o)).to(be_false)

    def test_ispropersubset_self_is_not_subset_of_other_enhanced_set(self):
        e = Set[int]({1, 2, 3, 4})
        o = Set[int]({0, 1, 2, 3})
        expect(e.ispropersubset(o)).to(be_false)



