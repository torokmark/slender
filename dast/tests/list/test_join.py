
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List 

class TestJoin(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3, 2])

    def test_join_if_separator_is_none(self):
        expect(self.l.join(None)).to(equal('1232'))
        
    def test_join_if_separator_is_emtpy_str(self):
        expect(self.l.join('')).to(equal('1232'))
 
    def test_join_if_separator_is_str(self):
        expect(self.l.join('-')).to(equal('1-2-3-2'))
    
    def test_join_if_separator_is_different(self):
        o = 123321 
        expect(lambda: self.l.join(o)).to(raise_error(TypeError))






