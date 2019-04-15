from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestCollect(TestCase):

    def test_collect_if_none(self):
        e = List([2, 4, 3, 5, 6, 7])
        it = e.collect()
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(5))
        expect(next(it)).to(equal(6))
        expect(next(it)).to(equal(7))


    def test_collect_if_lambda(self):
        e = List([1,2,4,9,10,11,12,15,16,19,20,21])
        act = e.collect(lambda i: i + 1)
        expect(act).to(equal([2, 3, 5, 10, 11, 12, 13, 16, 17, 20, 21, 22]))

