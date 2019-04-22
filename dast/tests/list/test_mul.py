
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List 

class TestMul(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3])

    def test_mul_if_other_is_none(self):
        expect(lambda: self.l * None).to(raise_error(TypeError))
        
    def test_mul_if_scalar_is_positive(self):
        expect((self.l * 3).to_list()).to(equal([1, 2, 3, 1, 2, 3, 1, 2, 3]))
 
    def test_mul_if_scalar_is_negative(self):
        expect((self.l * -1).to_list()).to(equal([]))
    
    def test_mul_if_scalar_is_zero(self):
        expect((self.l * 0).to_list()).to(equal([]))

    def test_mul_if_other_is_different(self):
        o = '...'
        expect(lambda: self.l * o).to(raise_error(TypeError))

