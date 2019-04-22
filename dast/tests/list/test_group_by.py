
import re
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List 

class TestGroupBy(TestCase):

    def test_group_by_if_param_is_lambda(self):
        e = List(['apple', 'bear', 'dog', 'plum', 'grape', 'cat', 'anchor'])
        act = e.group_by(lambda x: len(x))
        expect(act[3].sort()).to(equal(['dog', 'cat'].sort()))
        expect(act[4].sort()).to(equal(['bear', 'plum'].sort()))
        expect(act[5].sort()).to(equal(['apple', 'grape'].sort()))
        expect(act[6].sort()).to(equal(['anchor'].sort()))

    def test_group_by_if_param_is_lambda_create_one_key(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        act = e.group_by(lambda x: 'a' in x)
        expect(act.get(True).sort()).to(equal(['apple', 'bear', 'cat', 'anchor'].sort()))
        expect(act.get(False)).to(equal(None))
        
    def test_group_by_if_param_is_non_regex_object_nor_string(self):
        e = List([1, 2, 3, 4, 5, 6])
        expect(lambda: e.group_by(1)).to(raise_error(TypeError))
