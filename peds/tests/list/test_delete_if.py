
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from peds import List 

class TestDeleteIf(TestCase):

    def test_delete_if_if_list_is_empty(self):
        e = List([])
        expect(e.delete_if(lambda x: x == 1).to_list()).to(equal([]))
  
    def test_delete_if_if_lambda_is_valid_greater_than(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.delete_if(lambda x: x > 3).to_list()).to(equal([3, 2]))

    def test_delete_if_if_lambda_is_valid_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.delete_if(lambda x: len(x) > 5).to_list()).to(equal(['apple', 'bear', 'dog', 'plum']))
    
    def test_delete_if_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.delete_if('...')).to(raise_error(TypeError)) 


