from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List 

class TestDelete(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3, 2, 3, 2])

    def test_delete_if_obj_is_found_multiple_times(self):
        expect(self.l.delete(2).to_list()).to(equal([1, 3, 3]))
 
    def test_delete_if_obj_is_not_found(self):
        expect(self.l.delete(5).to_list()).to(equal([1, 2, 3, 2, 3, 2]))

    def test_delete_if_self_is_empty(self):
        l = List()
        expect(l.delete(3).to_list()).to(equal([]))




