from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List 

class TestAdd(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3])

    def test_add_if_other_is_none(self):
        expect((self.l + None).to_list()).to(equal([1, 2, 3]))
        
    def test_add_if_other_is_empty(self):
        expect((self.l + []).to_list()).to(equal([1, 2, 3]))
 
    def test_add_if_other_is_non_empty(self):
        o = List(['a', 'b'])
        expect((self.l + o).to_list()).to(equal([1, 2, 3, 'a', 'b']))

    def test_add_if_self_is_empty(self):
        l = List()
        o = List(['a', 'b'])
        expect((l + o).to_list()).to(equal(['a', 'b']))

    def test_add_if_other_is_different(self):
        l = List()
        o = '...'
        expect(lambda: l + o).to(raise_error(TypeError))



