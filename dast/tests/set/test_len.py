from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true

from dast import Set 

class TestLen(TestCase):

    def test_len_if_not_empty(self):
        e = Set({1, 2, 3, 4})
        expect(len(e)).to(equal(4))

    def test_len_if_empty(self):
        e = Set()
        expect(len(e)).to(equal(0))





