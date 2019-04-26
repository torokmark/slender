from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestKeepIf(TestCase):

    def test_keep_if_if_self_is_empty(self):
        e = Set()
        expect(e.keep_if(lambda x: x % 2 == 0)).to(equal(set()))

    def test_keep_if_if_no_match(self):
        e = Set({1, 2, 3, 4})
        expect(e.keep_if(lambda x: x > 5)).to(equal(set()))

    def test_keep_if_if_all_match(self):
        e = Set({1, 2, 3, 4, 5})
        expect(e.keep_if(lambda x: x >= 1)).to(equal({1, 2, 3, 4, 5}))

    def test_keep_if_if_partial_match(self):
        e = Set({1, 2, 3, 4})
        expect(e.keep_if(lambda x: x % 2 == 0)).to(equal({2, 4}))

    def test_keep_if_lambda_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e.keep_if('...')).to(raise_error(TypeError))




