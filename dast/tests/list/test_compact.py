
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List 

class TestCompact(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3, 2])

    def test_compact_if_self_contains_none(self):
        l = List([None, 1, 2, None, 3])
        expect(l.compact().to_list()).to(equal([1, 2, 3]))
        
    def test_compact_if_self_does_not_contain_none(self):
        l = List([1, 2, 3])
        expect(l.compact().to_list()).to(equal([1, 2, 3]))
 





