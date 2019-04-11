from unittest import TestCase
from expects import expect, equal, raise_error 

import peds

class TestFlatMap(TestCase):

    def test_flat_map_if_none(self):
        e = peds.Enumerable([2, 4, 3, 5, 6, 7])
        it = e.flat_map()
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(5))
        expect(next(it)).to(equal(6))
        expect(next(it)).to(equal(7))
    
    def test_flat_map_if_lambda(self):
        e = peds.Enumerable([1, 2, 3, 4])
        act = e.flat_map(lambda i: [i, -i])
        expect(act).to(equal([1, -1, 2, -2, 3, -3, 4, -4]))

