
import re
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List 

class TestGrep(TestCase):

    def test_grep_if_param_regex_string_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep(r'^a[a-z]*$').to_list()).to(equal(['apple', 'anchor']))
    
    def test_grep_if_param_regex_object_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep(re.compile('^a[a-z]*$')).to_list()).to(equal(['apple', 'anchor']))

    def test_grep_if_param_regex_object_and_func_is_lambda(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep(re.compile('^a[a-z]*$'), lambda x: x * 2).to_list()).to(equal(['appleapple', 'anchoranchor']))

    def test_grep_if_param_not_matching(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep(re.compile('^[0-9]')).to_list()).to(equal([]))

    def test_grep_if_param_is_non_regex_object_nor_string(self):
        e = List([])
        expect(lambda: e.grep(1)).to(raise_error(TypeError))



