
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from peds import List 

class TestReduce(TestCase):

    def test_reduce_if_init_is_not_given_and_concat(self):
        e = List(['apple', 'bear', 'dog', 'plum'])
        expect(e.reduce(lambda memo, s: memo + s)).to(equal('applebeardogplum'))

    def test_reduce_if_init_is_not_given_and_add_up(self):
        e = List([1, 2, 3, 4, 5, 6])
        expect(e.reduce(lambda sum, x: sum + x)).to(equal(21))
 
    def test_reduce_if_init_is_given_and_concat(self):
        e = List(['apple', 'bear', 'dog', 'plum'])
        expect(e.reduce(lambda memo, s: memo + s, '')).to(equal('applebeardogplum'))

    def test_reduce_if_init_is_given_and_add_up(self):
        e = List([1, 2, 3, 4, 5, 6])
        expect(e.reduce(lambda sum, x: sum + x, 2)).to(equal(23))

    def test_reduce_if_array_is_empty(self):
        e = List([])
        expect(e.reduce(lambda sum, x: sum + x, 2)).to(equal(None))

    def test_reduce_if_callback_is_different(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.reduce(5, 2)).to(raise_error(TypeError))

