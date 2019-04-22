
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List

class TestFindIndex(TestCase):

    def test_find_index_if_param_is_in_range(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find_index(lambda x: x == 2)
        expect(act).to(equal(1))

    def test_find_index_if_param_is_out_of_range(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find_index(lambda x: x == 6)
        expect(act).to(equal(None))

    def test_find_index_if_param_is_lambda_with_match(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find_index(lambda item: item > 3)
        expect(act).to(equal(3))



