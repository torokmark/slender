from unittest import TestCase
from expects import expect, equal 

import pedast

class TestDeleteIf(TestCase):

    def setUp(self):
        self.l = pedast.List([1, 2, 3])

    def test_delete_if_if_predicate_false(self):
        pass

    def test_delete_if_if_predicate_true(self):
        pass
 
