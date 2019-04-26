from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestStr(TestCase):

    def test_str_if_self_is_empty(self):
        e = Set()
        expect(str(e)).to(equal('{}'))

    def test_str_if_self_contains_elements(self):
        e = Set({1, 2, 3, 4})
        expect(str(e)).to(equal('{1, 2, 3, 4}'))



