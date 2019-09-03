from unittest import TestCase, skip
from expects import *

from slender import Dictionary 
from slender.command_line import main

class TestInit(TestCase):

    def setUp(self):
        self.l = Dictionary[str, int]()

    def test_dictionary_is_not_none(self):
        expect(self.l).not_to(equal(None))

    def test_dictionary_init_accepts_builtin_dict(self):
        d = Dictionary[str, int]({'a': 1, 'b': 2})
        expect(d).not_to(equal(None))

    def test_dictionary_init_accepts_dictionary(self):
        d = Dictionary[str, int](Dictionary[str, int]())
        expect(d).not_to(equal(None))
