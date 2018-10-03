#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def flatten(nested):
    try:
        try:
            nested + ' '
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten(['foo', 3, 4, ['bar', ['baz']]])))
