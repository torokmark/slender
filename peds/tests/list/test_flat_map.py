from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestFlatMap(TestCase):

    def test_flat_map_if_none(self):
        e = List([2, 4, 3, 5, 6, 7])
        expect(e.flat_map().to_list()).to(equal([2, 4, 3, 5, 6, 7]))
 
    def test_flat_map_if_none_with_sublists(self):
        e = List([[2, 4], 3, [5, 6, 7]])
        expect(e.flat_map().to_list()).to(equal([2, 4, 3, 5, 6, 7]))
       
    def test_flat_map_if_lambda(self):
        e = List([1, 2, 3, 4])
        act = e.flat_map(lambda i: [i, -i] if isinstance(i, int) else [i, None]).to_list()
        expect(act).to(equal([1, -1, 2, -2, 3, -3, 4, -4]))

    def test_flat_map_if_lambda_is_given_mixed_list(self):
        e = List([[1], 2, 3, 4])
        act = e.flat_map(lambda i: [i, -i] if isinstance(i, int) else [i, None]).to_list()
        expect(act).to(equal([[1], None, 2, -2, 3, -3, 4, -4]))

