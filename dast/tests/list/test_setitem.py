from unittest import TestCase
from expects import expect, equal 

import pedast

class TestSetitem(TestCase):

    def setUp(self):
        self.l = pedast.List([1, 2, 3])

    def test_support_indexing_set_raise_error_if_index_out_of_array(self):
        try:
            self.l[5] = 4
        except IndexError as e:
            expect(isinstance(e, IndexError)).to(equal(True))

    def test_support_indexing_set(self):
        self.l[2] = 4
        expect(self.l[2]).to(equal(4))


