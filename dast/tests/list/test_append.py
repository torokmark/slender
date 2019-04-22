

from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List 

class TestAppend(TestCase):
    def setUp(self):
        self.l = List([1, 2, 3, 2])

    def test_append_if_other_is_none(self):
        expect(self.l.append(None).to_list()).to(equal([1, 2, 3, 2, None]))
        
    def test_append_if_other_is_not_none(self):
        expect(self.l.append([1, 3]).to_list()).to(equal([1, 2, 3, 2, [1, 3]]))
 





