
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List

class TestFindRindex(TestCase):

    def test_find_rindex_if_param_is_in_range(self):
        e = List([1, 2, 4, 4, 5])
        act = e.find_rindex(lambda x: x == 4)
        expect(act).to(equal(3))

    def test_find_rindex_if_param_is_the_first_item_in_the_list(self):
        e = List([1, 2, 4, 4, 5])
        act = e.find_rindex(lambda x: x <= 1)
        expect(act).to(equal(0))

    def test_find_rindex_if_param_is_out_of_range(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find_rindex(lambda x: x == 6)
        expect(act).to(equal(None))

    def test_find_rindex_if_param_is_lambda_with_match(self):
        e = List([1, 2, 3, 4, 5])
        act = e.find_rindex(lambda item: item > 3)
        expect(act).to(equal(4))



