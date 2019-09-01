from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import Set 

class TestIter(TestCase):

    def test_iter(self):
        it = iter(Set({1, 2, 3, 4}))
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(4))


