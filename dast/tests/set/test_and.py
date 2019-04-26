from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import Set 

class TestAnd(TestCase):

    def test_and_other_with_inersection(self):
        e = Set({1, 2, 3, 4})
        o = {3, 4, 5, 6}
        expect((e & o).to_set()).to(equal({3, 4}))


    def test_and_other_without_intersection(self):
        e = Set({1, 2, 3})
        expect((e & {4, 5, 6}).to_set()).to(equal(set()))


    def test_and_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e & None).to(raise_error(TypeError))




