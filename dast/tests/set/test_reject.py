from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from dast import Set 

class TestReject(TestCase):

    def test_reject_if_lambda_find_match(self):
        e = Set({1, 2, 3, 4})
        expect(e.reject(lambda x: x % 2 == 0).to_set()).to(equal({1, 3}))

    def test_reject_if_lambda_finds_no_match(self):
        e = Set({1, 2, 3, 4})
        expect(e.reject(lambda x: x > 5).to_set()).to(equal({1, 2, 3, 4}))

    def test_reject_if_set_is_empty(self):
        e = Set({1, 2, 3})
        expect(lambda: e.reject('...')).to(raise_error(TypeError))




