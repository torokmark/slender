from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List 

class TestConcat(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3])

    def test_concat_if_other_is_empty(self):
        expect(self.l.concat([]).to_list()).to(equal([1, 2, 3]))
 
    def test_concat_if_other_is_non_empty(self):
        o = List(['a', 'b'])
        expect(self.l.concat(o).to_list()).to(equal([1, 2, 3, 'a', 'b']))

    def test_concat_if_self_is_empty(self):
        l = List()
        o = List(['a', 'b'])
        expect(l.concat(o).to_list()).to(equal(['a', 'b']))

    def test_concat_if_other_is_different(self):
        l = List()
        o = '...'
        expect(lambda: l.concat(o)).to(raise_error(TypeError))



