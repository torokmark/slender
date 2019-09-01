
from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import List

class TestRotate(TestCase):

    def test_rotate_if_param_is_in_range(self):
        e = List([1, 2, 4, 4, 5])
        expect(e.rotate(2).to_list()).to(equal([4, 5, 1, 2, 4]))

    def test_rotate_if_param_is_equal_to_len(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.rotate(5).to_list()).to(equal([1, 2, 3, 4, 5]))

    def test_rotate_if_param_is_out_of_range(self):
        e = List([1, 2, 3, 4, 5])
        expect(e.rotate(6).to_list()).to(equal([5, 1, 2, 3, 4]))

    def test_rotate_if_param_is_different(self):
        e = List([1, 2, 3, 4, 5])
        expect(lambda: e.rotate('...')).to(raise_error(TypeError))


