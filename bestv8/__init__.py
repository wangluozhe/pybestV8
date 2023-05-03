#!/usr/bin/env python3
# -*- coding: ascii -*-
'''r
Run JavaScript code from Python.

PyBestV8 is a porting of BestV8 from Ruby.
PyBestV8 automatically picks the best runtime available to evaluate your JavaScript program,
then returns the result to you as a Python object.

A short example:

>>> import bestv8
>>> bestv8.eval("'red yellow blue'.split(' ')")
['red', 'yellow', 'blue']
>>> ctx = bestv8.compile("""
...     function add(x, y) {
...         return x + y;
...     }
... """)
>>> ctx.call("add", 1, 2)
3
'''
from __future__ import unicode_literals, division, with_statement

from bestv8._exceptions import (
    Error,
    RuntimeError,
    ProgramError,
    RuntimeUnavailableError,
)

import bestv8._runtimes
from bestv8._external_runtime import ExternalRuntime
from bestv8._abstract_runtime import AbstractRuntime


__all__ = """
    get register runtimes get_from_environment exec_ eval compile
    ExternalRuntime
    Error RuntimeError ProgramError RuntimeUnavailableError
""".split()


register = bestv8._runtimes.register
get = bestv8._runtimes.get
runtimes = bestv8._runtimes.runtimes
get_from_environment = bestv8._runtimes.get_from_environment


def eval(source, cwd=None, recv_size=20000):
    return get().eval(source, cwd, recv_size)
eval.__doc__ = AbstractRuntime.eval.__doc__


def exec_(source, cwd=None, recv_size=20000):
    return get().exec_(source, cwd, recv_size)
exec_.__doc__ = AbstractRuntime.exec_.__doc__


def compile(source, cwd=None):
    return get().compile(source, cwd)
compile.__doc__ = AbstractRuntime.compile.__doc__