from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestGe(TestCase):

    def test_ge_other_is_set_and_subset_of_self(self):
        e = Set({1, 2, 3, 4})
        o = {2, 3}
        expect(e >= o).to(be_true)

    def test_ge_other_is_set_and_not_subset_of_self(self):
        e = Set({1, 2, 3, 4})
        o = {0, 1, 2, 3}
        expect(e >= o).to(be_false)

    def test_ge_other_is_enhanced_set_and_subset_of_self(self):
        e = Set({1, 2, 3, 4, 5})
        o = Set({2, 3, 5})
        expect(e >= o).to(be_true)

    def test_ge_other_is_enhanced_set_and_not_subset_of_self(self):
        e = Set({1, 2, 3, 4})
        o = Set({0, 1, 2, 3})
        expect(e >= o).to(be_false)

    def test_ge_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e >= '...').to(raise_error(TypeError))




