from unittest import TestCase
from expects import expect, equal, raise_error 

from slender import Set 

class TestOr(TestCase):

    def test_or_other_with_common_values(self):
        e = Set[int]({1, 2, 3, 4})
        o = Set[int]({1, 2, 3, 4})
        expect(e | o).to(equal(Set[int]({1, 2, 3, 4})))

    def test_or_other_without_common_values(self):
        e = Set[int]({1, 2, 3})
        o = Set[int]({4, 5, 6})
        expect(e | o).to(equal(Set[int]({1, 2, 3, 4, 5, 6})))

    def test_or_other_is_different(self):
        e = Set[int]({1, 2, 3})
        expect(lambda: e | None).to(raise_error(TypeError))



