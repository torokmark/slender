import re

from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestUnique(TestCase):

    def test_unique_if_lambda_is_none(self):
        e = List(['apple', 'apple', 'apple', 'tree', 'apple', 'juice'])
        act = e.unique()
        expect(sorted(act)).to(equal(['apple', 'juice', 'tree']))

    def test_unique_if_lambda_is_not_none(self):
        e = List(['apple', 'hola', 'appletree', 'applejuice', 'juice'])
        act = e.unique(lambda x: x[0] )
        expect(act).to(equal(['applejuice', 'hola', 'juice']))
    
    def test_unique_if_lambda_is_different(self):
        e = List(['apple', 'applehola', 'appletree', 'applejuice'])
        expect(lambda: e.unique('...')).to(raise_error(TypeError))



