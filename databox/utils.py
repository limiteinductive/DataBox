# AUTOGENERATED! DO NOT EDIT! File to edit: utils.ipynb (unless otherwise specified).

__all__ = ['function', 'simplify']

# Cell
from nbdev.showdoc import *

#export
from typing import Iterable
from plum import dispatch

function = type(lambda: ())

# Cell
def simplify(x):
    @dispatch
    def _simplify(x): return x

    @dispatch
    def _simplify(fn: function):
        try:
            return fn()
        except TypeError:
            return fn

    @dispatch
    def _simplify(i: Iterable): return next(i.__iter__()) if len(i) == 1 else i

    return _simplify(x)