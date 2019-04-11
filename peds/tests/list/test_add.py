from unittest import TestCase
from expects import expect, equal 

import pedast

class TestAdd(TestCase):
    def setUp(self):
        self.l = pedast.List([1, 2, 3])

    def test_add_if_other_is_none(self):
        expect(self.l + None).to(equal([1, 2, 3]))
        
    def test_add_if_other_is_empty(self):
        expect(self.l + []).to(equal([1, 2, 3]))
 
    def test_add_if_other_is_non_empty(self):
        o = pedast.List(['a', 'b'])
        expect(self.l + o).to(equal([1, 2, 3, 'a', 'b']))

    def test_add_if_self_is_empty(self):
        l = pedast.List()
        o = pedast.List(['a', 'b'])
        expect(l + o).to(equal(['a', 'b']))



