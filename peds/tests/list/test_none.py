
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from peds import List 

class TestNone(TestCase):

    def test_none_if_none_of_them_are_falsy(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.none()).to(be_false)

    def test_none_if_not_all_of_them_are_falsy(self):
        e = List([False, None, 'dog', 'plum'])
        expect(e.none()).to(be_false)

    def test_none_if_all_of_them_are_falsy(self):
        e = List([None, '', None, 0, False, [], None])
        expect(e.none()).to(be_true)
     
    def test_none_if_list_is_empty(self):
        e = List([])
        expect(e.none()).to(be_true)
   
    def test_none_if_lambda_is_true_on_all(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.none(lambda x: len(x) > 1)).to(be_false)

    def test_none_if_lambda_is_true_on_some(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.none(lambda x: len(x) > 5)).to(be_false)

    def test_none_if_lambda_is_false_on_all(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.none(lambda x: len(x) > 15)).to(be_true)

    def test_none_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.none('...')).to(raise_error(TypeError))
