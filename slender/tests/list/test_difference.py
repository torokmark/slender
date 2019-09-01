
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List 

class TestDifference(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3, 2])

    def test_difference_if_other_is_none(self):
        expect(lambda: self.l.difference(None)).to(raise_error(TypeError))
        
    def test_difference_if_other_has_intersection(self):
        expect(self.l.difference([1, 3]).to_list()).to(equal([2, 2]))
 
    def test_difference_if_other_is_disjoint(self):
        expect(self.l.difference([5, 6]).to_list()).to(equal([1, 2, 3, 2]))
    
    def test_difference_if_other_is_different(self):
        o = '...'
        expect(lambda: self.l.difference(o)).to(raise_error(TypeError))






