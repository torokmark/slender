from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import Set 

class TestUnion(TestCase):

    def test_union_other_with_common_values(self):
        e = Set({1, 2, 3, 4})
        o = {3, 4, 5, 6}
        expect(e.union(o).to_set()).to(equal({1, 2, 3, 4, 5, 6}))


    def test_union_other_without_common_values(self):
        e = Set({1, 2, 3})
        o = Set({4, 5, 6})
        expect(e.union(o).to_set()).to(equal({1, 2, 3, 4, 5, 6}))


    def test_union_other_with_empty_set(self):
        e = Set({1, 2, 3})
        o = set()
        expect(e.union(o).to_set()).to(equal({1, 2, 3}))


    def test_union_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e.union(None)).to(raise_error(TypeError))




