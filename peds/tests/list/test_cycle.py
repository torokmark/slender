from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List 

class TestCycle(TestCase):

    def test_cycle_if_param_and_func_not_none(self):
        e = List(['a', 'b', 'c'])
        it = e.cycle(2, lambda x: x.upper())
        expect(next(it)).to(equal('A'))
        expect(next(it)).to(equal('B'))
        expect(next(it)).to(equal('C'))
        expect(next(it)).to(equal('A'))
        expect(next(it)).to(equal('B'))
        expect(next(it)).to(equal('C'))

    def test_cycle_if_func_is_none(self):
        e = List([1, 2, 0])
        it = e.cycle(2)
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(0))
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(0))
    
    def test_cycle_if_lambda(self):
        e = List([1, 2, 4, 2])
        it = e.cycle(lambda i: i % 2 == 0)
        expect(next(it)).to(equal(False))
        expect(next(it)).to(equal(True))
        expect(next(it)).to(equal(True))
        expect(next(it)).to(equal(True))

    def test_cycle_if_no_params(self):
        e = List([1, 2, 4, 2])
        it = e.cycle()
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(2))

    def test_cycle_if_param_type_is_different(self):
        e = List(['a', 'b', 'c'])
        it = e.cycle('...')
        expect(lambda: next(it)).to(raise_error(TypeError))

