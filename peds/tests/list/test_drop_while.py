
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestDropWhile(TestCase):
    
    def test_drop_while_if_param_is_lambda_and_finds_match(self):
        e = List([1, 2, 3, 4])
        expect(e.drop_while(lambda x: x < 3).to_list()).to(equal([3, 4]))

    def test_drop_while_if_param_is_lambda_and_finds_match(self):
        e = List([1, 2, 3, 4])
        expect(e.drop_while(lambda x: x < 5).to_list()).to(equal([]))

    def test_drop_while_if_param_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.drop_while('...')).to(raise_error(TypeError))



