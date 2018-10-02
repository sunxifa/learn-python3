#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def triangles(max):
    row = [1]
    n = 0
    while n < max:
        yield(row)
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
        n += 1


for L in triangles(10):
    print(L)
