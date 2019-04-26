from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestIspropersubset(TestCase):

    def test_ispropersubset_self_is_proper_subset_of_other_set(self):
        e = Set({2, 3})
        o = {1, 2, 3, 4}
        expect(e.ispropersubset(o)).to(be_true)

    def test_ispropersubset_self_is_not_subset_of_other_set(self):
        e = Set({1, 2, 3, 4})
        o = {0, 1, 2, 3}
        expect(e.ispropersubset(o)).to(be_false)

    def test_ispropersubset_self_is_not_proper_subset_of_other_enhanced_set(self):
        e = Set({1, 2, 3, 4, 5})
        o = Set({1, 4, 2, 3, 5})
        expect(e.ispropersubset(o)).to(be_false)

    def test_ispropersubset_self_is_not_subset_of_other_enhanced_set(self):
        e = Set({1, 2, 3, 4})
        o = Set({0, 1, 2, 3})
        expect(e.ispropersubset(o)).to(be_false)

    def test_ispropersubset_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e.ispropersubset('...')).to(raise_error(TypeError))



