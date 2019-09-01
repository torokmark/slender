from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestChunkWhile(TestCase):

    def test_chunk_while_one_by_one(self):
        e = List([1,2,4,9,10,11,12,15,16,19,20,21])
        expect(e.chunk_while(lambda i, j: i + 1 == j).to_list()).to(equal([[1, 2], [4], [9, 10, 11, 12], [15, 16], [19, 20, 21]]))

    def test_chunk_while_non_decreasing(self):
        e = List([0, 9, 2, 2, 3, 2, 7, 5, 9, 5])
        expect(e.chunk_while(lambda i, j: i <= j).to_list()).to(equal([[0, 9], [2, 2, 3], [2, 7], [5, 9], [5]]))

    def test_chunk_while_adjacent_evens_odds(self):
        e = List([7, 5, 9, 2, 0, 7, 9, 4, 2, 0])
        expect(e.chunk_while(lambda i, j: i % 2 == j % 2).to_list()).to(equal([[7, 5, 9], [2, 0], [7, 9], [4, 2, 0]]))

    def test_chunk_while_if_param_is_not_lambda(self):
        e = List([1, 2])
        expect(lambda: e.chunk_while(123)).to(raise_error(TypeError))
