from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestInclude(TestCase):

    def test_include_if_self_contains_element(self):
        e = Set({1, 2, 3})
        expect(e.include(2)).to(be_true)

    def test_include_if_self_not_contains_elements(self):
        e = Set({1, 2, 3, 4})
        expect(e.include(11)).to(be_false)



