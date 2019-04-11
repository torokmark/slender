from unittest import TestCase
from expects import expect, equal 

import pedast

class TestGetitem(TestCase):

    def setUp(self):
        self.l = pedast.List([1, 2, 3])

    def test_support_indexing_get(self):
        expect(self.l[2]).to(equal(3))


