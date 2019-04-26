from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestIspropersuperset(TestCase):

    def test_ispropersuperset_other_is_set_and_subset_of_self(self):
        e = Set({1, 2, 3, 4})
        o = {2, 3}
        expect(e.ispropersuperset(o)).to(be_true)

    def test_ispropersuperset_other_is_set_and_not_subset_of_self(self):
        e = Set({1, 2, 3, 4})
        o = {0, 1, 2, 3}
        expect(e.ispropersuperset(o)).to(be_false)

    def test_ispropersuperset_other_is_enhanced_set_and_subset_of_self(self):
        e = Set({1, 2, 3, 4, 5})
        o = Set({1, 4, 2, 3, 5})
        expect(e.ispropersuperset(o)).to(be_false)

    def test_ispropersuperset_other_is_enhanced_set_and_not_subset_of_self(self):
        e = Set({1, 2, 3, 4})
        o = Set({0, 1, 2, 3})
        expect(e.ispropersuperset(o)).to(be_false)

    def test_ispropersuperset_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e.ispropersuperset('...')).to(raise_error(TypeError))




