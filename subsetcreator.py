# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:39:43 2017

@author: admin
"""
def gensubset(L):
    if len(L) == 0:
        return [[]]
    smaller = gensubset(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(extra + small)
    return smaller + new

    