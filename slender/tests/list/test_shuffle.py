
from unittest import TestCase
from expects import expect, equal, contain 

from slender import List 

class TestShuffle(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3, 2])

    def test_shuffle_if_self_empty(self):
        l = List()
        expect(l.shuffle().to_list()).to(equal([]))
        
    def test_append_if_self_not_empty(self):
        l = List([1, 2, 3])
        act = l.shuffle().to_list()
        expect(act).to(contain(1))
        expect(act).to(contain(2))
        expect(act).to(contain(3))
        
 




