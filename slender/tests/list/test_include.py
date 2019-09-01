
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from slender import List 

class TestInclude(TestCase):

    def test_include_if_value_in_array(self):
        e = List(['apple', 'bear', 'dog', 'plum', 'grape', 'cat', 'anchor'])
        expect(e.include('bear')).to(be_true)

    def test_include_if_value_not_in_array(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.include('dog')).to(be_false)
        
