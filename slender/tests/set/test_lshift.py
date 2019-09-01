from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestLshift(TestCase):

    def test_lshift_if_set_already_contains_element(self):
        e = Set({1, 2, 3, 4})
        expect((e << 2).to_set()).to(equal({1, 2, 3, 4}))

    def test_lshift_if_set_not_contains_element(self):
        e = Set({1, 2, 3, 4})
        expect((e << 7).to_set()).to(equal({1, 2, 3, 4, 7}))

    def test_lshift_if_set_is_empty(self):
        e = Set()
        expect((e << 1).to_set()).to(equal({1}))




