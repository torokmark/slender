
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List

class TestLen(TestCase):

    def test_len_if_list_is_not_empty(self):
        e = List([1, 2, 3, 4, 5])
        expect(len(e)).to(equal(5))

    def test_len_if_list_is_empty(self):
        e = List([])
        expect(len(e)).to(equal(0))




