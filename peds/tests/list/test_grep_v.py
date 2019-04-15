
import re
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List 

class TestGrepV(TestCase):

    def test_grep_v_if_param_regex_string_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep_v(r'^a[a-z]*$')
        expect(next(it)).to(equal('bear'))
        expect(next(it)).to(equal('cat'))
    
    def test_grep_v_if_param_regex_object_and_func_is_none(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep_v(re.compile('^a[a-z]*$'))
        expect(next(it)).to(equal('bear'))
        expect(next(it)).to(equal('cat'))

    def test_grep_v_if_param_regex_object_and_func_is_lambda(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep_v(re.compile('^a[a-z]*$'), lambda x: x * 2)
        expect(next(it)).to(equal('bearbear'))
        expect(next(it)).to(equal('catcat'))

    def test_grep_v_if_param_not_matching(self):
        e = List(['apple', 'bear', 'cat', 'anchor'])
        it = e.grep_v(re.compile('^[0-9]'))
        expect(next(it)).to(equal('apple'))
        expect(next(it)).to(equal('bear'))
        expect(next(it)).to(equal('cat'))
        expect(next(it)).to(equal('anchor'))

    def test_grep_v_if_param_is_non_regex_object_nor_string(self):
        e = List([])
        it = e.grep_v(1)
        expect(lambda: next(it)).to(raise_error(TypeError))


