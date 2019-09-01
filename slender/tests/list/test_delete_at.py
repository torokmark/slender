from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List 

class TestDeleteAt(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3, 2, 3, 2])

    def test_delete_at_if_index_in_range(self):
        expect(self.l.delete_at(2).to_list()).to(equal([1, 2, 2, 3, 2]))
 
    def test_delete_at_if_index_out_of_range(self):
        expect(lambda: self.l.delete_at(10)).to(raise_error(IndexError))

    def test_delete_at_if_self_is_empty(self):
        l = List()
        expect(lambda: l.delete_at(3)).to(raise_error(IndexError))




