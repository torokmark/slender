import re

from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestFirstWhile(TestCase):

    def test_first_while_if_lambda_finds_matching(self):
        e = List(['apple', 'hola', 'appletree', 'applejuice', 'juice'])
        act = e.first_while(lambda x: len(x) < 6).to_list()
        expect(act).to(equal(['apple', 'hola']))

    def test_first_while_if_lambda_is_not_matching(self):
        e = List(['apple', 'applehola', 'appletree', 'applejuice'])
        act = e.first_while(lambda x: len(x) < 2).to_list()
        expect(act).to(equal([]))

    def test_first_while_if_lambda_finds_all_matching(self):
        e = List(['apple', 'applehola', 'appletree', 'applejuice'])
        act = e.first_while(lambda x: len(x) > 1).to_list()
        expect(act).to(equal(['apple', 'applehola', 'appletree', 'applejuice']))

    def test_first_while_if_lambda_is_different(self):
        e = List(['apple', 'applehola', 'appletree', 'applejuice'])
        expect(lambda: e.first_while('...')).to(raise_error(TypeError))
    
