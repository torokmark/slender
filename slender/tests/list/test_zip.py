
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from slender import List 

class TestZip(TestCase):

    def test_zip_if_other_is_empty(self):
        e = List([5, 0, 3 ])
        expect(e.zip([]).to_list()).to(equal([[5, None], [0, None], [3, None]]))

    def test_zip_if_other_len_is_equal(self):
        e = List([1, 2, 3])
        expect(e.zip([4, 5, 6]).to_list()).to(equal([[1, 4], [2, 5], [3, 6]]))
  
    def test_zip_if_other_is_longer(self):
        e = List([1, 2, 4])
        expect(e.zip([5, 6, 7, 8]).to_list()).to(equal([[1, 5], [2, 6], [4, 7], [None, 8]]))
   
    def test_zip_if_other_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.zip('...')).to(raise_error(TypeError))


