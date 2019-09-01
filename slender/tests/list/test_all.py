import re

from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestAll(TestCase):
    def setUp(self):
        self.e = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_all_is_regex_with_no_matching(self):
        e = List(['apple', 'hola', 'appletree', 'applejuice', 'juice'])
        pattern = re.compile('apple*')
        result = e.all(pattern)
        expect(result).to(equal(False))

    def test_all_is_regex_with_all_matching(self):
        e = List(['apple', 'applehola', 'appletree', 'applejuice'])
        pattern = re.compile('apple*')
        result = e.all(pattern)
        expect(result).to(equal(True))

    def test_all_is_lambda_with_no_matching(self):
        predicate = lambda x: x % 3 == 0
        result = self.e.all(predicate)
        expect(result).to(equal(False))

    def test_all_is_lambda_with_all_matching(self):
        predicate = lambda x: x > 0 
        result = self.e.all(predicate)
        expect(result).to(equal(True))

    def test_all_is_lambda_with_all_matching(self):
        predicate = 'predicate'
        expect(lambda: self.e.all(predicate)).to(raise_error(TypeError))

