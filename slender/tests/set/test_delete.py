from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestDelete(TestCase):

    def test_delete_if_set_contains_element(self):
        e = Set({1, 2, 3, 4})
        expect(e.delete(2).to_set()).to(equal({1, 3, 4}))

    def test_delete_if_set_not_contains_element(self):
        e = Set({1, 2, 3, 4})
        expect(lambda: e.delete(7)).to(raise_error(KeyError))





