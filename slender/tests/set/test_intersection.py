from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import Set 

class TestIntersection(TestCase):

    def test_intersection_other_with_inersection(self):
        e = Set({1, 2, 3, 4})
        o = {3, 4, 5, 6}
        expect(e.intersection(o).to_set()).to(equal({3, 4}))


    def test_intersection_other_without_intersection(self):
        e = Set({1, 2, 3})
        o = Set({4, 5, 6})
        expect(e.intersection(o).to_set()).to(equal(set()))


    def test_intersection_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e.intersection(None)).to(raise_error(TypeError))




