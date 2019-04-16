
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from peds import List 

class TestPartition(TestCase):

    def test_partition_if_lambda_is_none(self):
        e = List([None, 5, 0, [], 3, 5, 2, '', 4])
        expect(e.partition()).to(equal([[5, 3, 5, 2, 4], [None, 0, [], '']]))

    def test_partition_if_list_is_empty(self):
        e = List([])
        expect(e.partition(lambda x: x == 1)).to(equal([[], []]))
  
    def test_partition_if_lambda_is_valid_greater_than(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.partition(lambda x: x > 3)).to(equal([[5, 5, 4], [3, 2]]))

    def test_partition_if_lambda_is_valid_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.partition(lambda x: len(x) > 5)).to(equal([['caterpillar'], ['apple', 'bear', 'dog', 'plum']]))
    
    def test_partition_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.partition('...')).to(raise_error(TypeError))
