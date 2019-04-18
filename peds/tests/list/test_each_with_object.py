
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestEachWithObject(TestCase):

    def test_each_with_object_if_param_is_array(self):
        e = List([1, 2, 3])
        expect(e.each_with_object(object=[]).to_list()).to(equal([[1, []], [2, []], [3, []]]))

    def test_each_with_object_if_param_is_string(self):
        e = List([1, 2, 3])
        expect(e.each_with_object(object='a').to_list()).to(equal([[1, 'a'], [2, 'a'], [3, 'a']]))

    def test_each_with_object_if_param_is_array_and_func_is_not_none(self):
        e = List([1, 2, 3])
        expect(e.each_with_object(object=[], callback=lambda item, obj: (obj.append(item), obj)[-1]).to_list()).to(equal([[1, [1]], [2, [1, 2]], [3, [1, 2, 3]]]))

    def test_each_with_object_if_func_is_different(self):
        e = List([1, 2, 3, 4])
        expect(lambda: e.each_with_object(object=[], callback=-1)).to(raise_error(TypeError))



