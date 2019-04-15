
from unittest import TestCase
from expects import expect, equal, raise_error 

from peds import List

class TestEachWithObject(TestCase):

    def test_each_with_object_if_param_is_array(self):
        e = List([1, 2, 3, 4, 5])
        it = e.each_with_object([])
        expect(next(it)).to(equal([1, []]))
        expect(next(it)).to(equal([2, []]))
        expect(next(it)).to(equal([3, []]))
        expect(next(it)).to(equal([4, []]))
        expect(next(it)).to(equal([5, []]))

    def test_each_with_object_if_param_is_string(self):
        e = List([1, 2, 3, 4, 5])
        it = e.each_with_object('a')
        expect(next(it)).to(equal([1, 'a']))
        expect(next(it)).to(equal([2, 'a']))
        expect(next(it)).to(equal([3, 'a']))
        expect(next(it)).to(equal([4, 'a']))
        expect(next(it)).to(equal([5, 'a']))

    def test_each_with_object_if_param_is_array_and_func_is_not_none(self):
        e = List([1, 2, 3, 4, 5])
        it = e.each_with_object([], lambda item, obj: (obj.append(item), obj)[-1])
        expect(next(it)).to(equal([1, [1]]))
        expect(next(it)).to(equal([2, [1, 2]]))
        expect(next(it)).to(equal([3, [1, 2, 3]]))
        expect(next(it)).to(equal([4, [1, 2, 3, 4]]))
        expect(next(it)).to(equal([5, [1, 2, 3, 4, 5]]))

    def test_each_with_object_if_func_is_different(self):
        e = List([1, 2, 3, 4])
        it = e.each_with_object([], -1)
        expect(lambda: next(it)).to(raise_error(TypeError))



