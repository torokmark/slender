
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestFirst(TestCase):

    def test_first_if_param_is_none(self):
        e = List([1, 2, 3, 4, 5])
        act = e.first()
        expect(act).to(equal(1))

    def test_first_if_param_is_in_range(self):
        e = List([1, 2, 3, 4, 5])
        act = e.first(3) 
        expect(act).to(equal([1, 2, 3]))

    def test_first_if_param_is_out_of_range(self):
        e = List([1, 2, 3, 4, 5])
        act = e.first(10)
        expect(act).to(equal([1, 2, 3, 4, 5]))

    def test_first_if_array_is_empty_and_param_is_none(self):
        e = List([])
        act = e.first()
        expect(act).to(equal(None))

    def test_first_if_array_is_empty_and_param_is_greater_than_zero(self):
        e = List([])
        act = e.first(10)
        expect(act).to(equal([]))

    def test_first_if_param_is_non_int(self):
        e = List([])
        expect(lambda: e.first('...')).to(raise_error(TypeError))




