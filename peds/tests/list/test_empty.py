
from unittest import TestCase
from expects import expect, equal, be_true, be_false 

from peds import List 

class TestEmpty(TestCase):

    def test_empty_if_list_is_empty(self):
        expect(List([]).empty()).to(be_true)

    def test_empty_if_list_is_not_empty(self):
        expect(List([1, 2, 3]).empty()).to(be_false)





