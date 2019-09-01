from unittest import TestCase, skip
from expects import *

from slender import List
from slender.command_line import main

class TestInit(TestCase):

    def setUp(self):
        self.l = List()

    def test_list_is_not_none(self):
        expect(self.l).not_to(equal(None))

    @skip
    def test_basic(self):
        main()