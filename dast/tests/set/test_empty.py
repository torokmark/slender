from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestEmpty(TestCase):

    def test_empty_if_self_is_empty(self):
        e = Set()
        expect(e.empty()).to(be_true)

    def test_empty_if_self_is_not_empty(self):
        e = Set({1, 2, 3, 4})
        expect(e.empty()).to(be_false)





