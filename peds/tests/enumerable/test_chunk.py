from unittest import TestCase
from expects import expect, equal, raise_error 

import peds

class TestChunk(TestCase):

    def test_chunk(self):
        e = peds.Enumerable([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        it = e.chunk(lambda x: x % 2 == 0)
        expect(next(it)).to(equal([False, [3, 1]]))
        expect(next(it)).to(equal([True, [4]]))
        expect(next(it)).to(equal([False, [1, 5, 9]]))
        expect(next(it)).to(equal([True, [2, 6]]))
        expect(next(it)).to(equal([False, [5, 3, 5]]))

    def test_chunk_if_param_is_not_lambda(self):
        e = peds.Enumerable([1, 2])
        expect(lambda: e.chunk(123)).to(raise_error(TypeError))

