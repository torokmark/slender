from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List

class TestMap(TestCase):

    def test_map_if_none(self):
        e = List([2, 4, 3, 5, 6, 7])
        expect(e.map().to_list()).to(equal([2, 4, 3, 5, 6, 7]))

    def test_map_if_lambda(self):
        e = List([1,2,4,9,10,11,12,15,16,19,20,21])
        expect(e.map(lambda i: i + 1).to_list()).to(equal([2, 3, 5, 10, 11, 12, 13, 16, 17, 20, 21, 22]))

