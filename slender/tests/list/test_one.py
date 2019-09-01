
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from slender import List 

class TestOne(TestCase):

    def test_one_if_all_of_them_are_truthy(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.one()).to(be_false)

    def test_one_if_more_than_one_is_truthy(self):
        e = List([False, None, 'dog', 'plum'])
        expect(e.one()).to(be_false)

    def test_one_if_only_one_is_truthy(self):
        e = List([None, '', None, 0, False, ['apple'], None])
        expect(e.one()).to(be_true)
     
    def test_one_if_list_is_empty(self):
        e = List([])
        expect(e.one()).to(be_false)
   
    def test_one_if_lambda_is_true_on_all(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.one(lambda x: len(x) > 1)).to(be_false)

    def test_one_if_lambda_is_true_only_one(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.one(lambda x: len(x) > 5)).to(be_true)

    def test_one_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.one('...')).to(raise_error(TypeError))
