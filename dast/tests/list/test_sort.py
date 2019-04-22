
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from dast import List 

class TestSort(TestCase):

    def test_sort_if_lambda_is_none(self):
        e = List([5, 0, 3, 5, 2, 4])
        expect(e.sort().to_list()).to(equal([0, 2, 3, 4, 5, 5]))

    def test_sort_if_list_is_empty(self):
        e = List([])
        expect(e.sort(lambda x: len(x)).to_list()).to(equal([]))
  
    def test_sort_if_lambda_is_valid_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.sort(lambda x: len(x)).to_list()).to(equal(['dog', 'bear', 'plum', 'apple', 'caterpillar']))
    
    def test_sort_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.sort('...')).to(raise_error(TypeError))
