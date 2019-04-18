from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestChunk(TestCase):

    def test_chunk(self):
        e = List([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        expect(e.chunk(lambda x: x % 2 == 0).to_list()).to(equal([[False, [3, 1]], [True, [4]], [False, [1, 5, 9]], [True, [2, 6]], [False, [5, 3, 5]]]))

    def test_chunk_if_param_is_not_lambda(self):
        e = List([1, 2])
        expect(lambda: e.chunk(123)).to(raise_error(TypeError))

