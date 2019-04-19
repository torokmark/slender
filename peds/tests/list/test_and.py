
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List 

class TestAnd(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3])

    def test_and_if_other_is_none(self):
        expect(lambda: self.l & None).to(raise_error(TypeError))
        
    def test_and_if_other_is_empty(self):
        expect((self.l & []).to_list()).to(equal([]))
 
    def test_and_if_other_is_non_empty(self):
        o = List([2, 3])
        expect((self.l & o).to_list()).to(equal([2, 3]))

    def test_and_if_self_is_empty(self):
        l = List()
        o = List(['a', 'b'])
        expect((l & o).to_list()).to(equal([]))

    def test_and_if_self_and_other_are_disjoint(self):
        l = List([1, 2, 3])
        o = List([4, 5, 6])
        expect((l & o).to_list()).to(equal([]))

    def test_and_if_other_is_different(self):
        l = List()
        o = '...'
        expect(lambda: l & o).to(raise_error(TypeError))


