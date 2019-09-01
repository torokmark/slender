from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestChain(TestCase):

    def test_chain_if_other_empty(self):
        e = List([])
        expect(e.chain([1, 2]).to_list()).to(equal([1, 2]))

    def test_chain_if_other_non_empty(self):
        e = List(['a', 'b'])
        expect(e.chain([1, 2]).to_list()).to(equal(['a', 'b', 1, 2]))

    def test_chain_if_other_is_none(self):
        e = List([1, 2])
        expect(lambda: e.chain(None)).to(raise_error(TypeError))

    def test_chain_if_other_is_not_iterable(self):
        e = List([])
        expect(lambda: e.chain(123)).to(raise_error(TypeError))

