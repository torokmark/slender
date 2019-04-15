
import re
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List 

class TestGrep(TestCase):

    def test_grep_if_param_regex_string_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep(r'^a[a-z]*$')
        expect(next(it)).to(equal('apple'))
        expect(next(it)).to(equal('anchor'))
    
    def test_grep_if_param_regex_object_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep(re.compile('^a[a-z]*$'))
        expect(next(it)).to(equal('apple'))
        expect(next(it)).to(equal('anchor'))

    def test_grep_if_param_regex_object_and_func_is_lambda(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep(re.compile('^a[a-z]*$'), lambda x: x * 2)
        expect(next(it)).to(equal('appleapple'))
        expect(next(it)).to(equal('anchoranchor'))

    def test_grep_if_param_not_matching(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep(re.compile('^[0-9]'))
        expect(lambda: next(it)).to(raise_error(StopIteration))

    def test_grep_if_param_is_non_regex_object_nor_string(self):
        e = List([])
        it = e.grep(1)
        expect(lambda: next(it)).to(raise_error(TypeError))



