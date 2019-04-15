from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestChain(TestCase):

    def test_chain_if_other_empty(self):
        e = List([])
        it = e.chain([1, 2])
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))

    def test_chain_if_other_non_empty(self):
        e = List(['a', 'b'])
        it = e.chain([1, 2])
        expect(next(it)).to(equal('a'))
        expect(next(it)).to(equal('b'))
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))

    def test_chain_if_other_is_none(self):
        e = List([1, 2])
        expect(lambda: e.chain(None)).to(raise_error(TypeError))

    def test_chain_if_other_is_not_iterable(self):
        e = List([])
        expect(lambda: e.chain(123)).to(raise_error(TypeError))

