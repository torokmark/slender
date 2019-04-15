
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestDropWhile(TestCase):
    def test_drop_while_if_param_none(self):
        e = List([1, 2, 3, 4])
        it = e.drop_while()
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(4))
    
    def test_drop_while_if_param_is_lambda_and_finds_match(self):
        e = List([1, 2, 3, 4])
        it = e.drop_while(lambda x: x < 3)
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(4))

    def test_drop_while_if_param_is_lambda_and_no_matching_found(self):
        e = List([1, 2, 3, 4])
        it = e.drop_while(lambda x: x < 5)
        expect(lambda: next(it)).to(raise_error(StopIteration))
    
    def test_drop_while_if_param_is_different_raises_error(self):
        e = List([1, 2, 3, 4])
        it = e.drop_while('...')
        expect(lambda: next(it)).to(raise_error(TypeError))



