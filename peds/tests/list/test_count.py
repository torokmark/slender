from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestCount(TestCase):

    def test_count_if_none(self):
        e = List([1, 2, 4, 2])
        expect(e.count()).to(equal(4))
   
    def test_count_if_item(self):
        e = List([1, 2, 4, 2])
        expect(e.count(lambda i: i == 2)).to(equal(2))

    def test_count_if_lambda(self):
        e = List([1, 2, 4, 2])
        act = e.count(lambda i: i % 2 == 0)
        expect(act).to(equal(3))

    def test_count_if_param_is_string(self):
        e = List([1, 2, 4, 2])
        expect(lambda: e.count('str')).to(raise_error(TypeError))


