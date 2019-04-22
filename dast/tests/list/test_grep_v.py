
import re
from unittest import TestCase
from expects import expect, equal, raise_error 

from dast import List 

class TestGrepV(TestCase):

    def test_grep_v_if_param_regex_string_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep_v(r'^a[a-z]*$').to_list()).to(equal(['bear', 'cat']))
    
    def test_grep_v_if_param_regex_object_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep_v(re.compile('^a[a-z]*$')).to_list()).to(equal(['bear', 'cat']))

    def test_grep_v_if_param_regex_object_and_func_is_lambda(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep_v(re.compile('^a[a-z]*$'), lambda x: x * 2).to_list()).to(equal(['bearbear', 'catcat']))

    def test_grep_v_if_param_not_matching(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        expect(e.grep_v(re.compile('^[0-9]')).to_list()).to(equal(['apple', 'bear', 'cat', 'anchor']))

    def test_grep_v_if_param_is_non_regex_object_nor_string(self):
        e = List([])
        expect(lambda: e.grep_v(1)).to(raise_error(TypeError))


