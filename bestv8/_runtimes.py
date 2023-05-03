import os.path
from collections import OrderedDict

import bestv8.runtime_names as runtime_names
import bestv8._external_runtime as external_runtime
import bestv8._pybestv8_runtime as pybestv8runtime
import bestv8._exceptions as exceptions


def register(name, runtime):
    '''Register a JavaScript runtime.'''
    _runtimes.append((name, runtime))


def get(name=None):
    """
    Return a appropriate JavaScript runtime.
    If name is specified, return the runtime.
    """
    if name is None:
        return get_from_environment() or _find_available_runtime()
    return _find_runtime_by_name(name)


def runtimes():
    """return a dictionary of all supported JavaScript runtimes."""
    return OrderedDict(_runtimes)


def get_from_environment():
    '''
        Return the JavaScript runtime that is specified in BESTV8_RUNTIME environment variable.
        If BESTV8_RUNTIME environment variable is empty or invalid, return None.
    '''
    name = os.environ.get("BESTV8_RUNTIME", "")
    if not name:
        return None

    try:
        return _find_runtime_by_name(name)
    except exceptions.RuntimeUnavailableError:
        return None


def _find_available_runtime():
    for _, runtime in _runtimes:
        if runtime.is_available():
            return runtime
    raise exceptions.RuntimeUnavailableError("Could not find an available JavaScript runtime.")


def _find_runtime_by_name(name):
    for runtime_name, runtime in _runtimes:
        if runtime_name.lower() == name.lower():
            break
    else:
        raise exceptions.RuntimeUnavailableError("{name} runtime is not defined".format(name=name))

    if not runtime.is_available():
        raise exceptions.RuntimeUnavailableError(
            "{name} runtime is not available on this system".format(name=runtime.name))
    return runtime


_runtimes = []

register(runtime_names.PyBestV8, pybestv8runtime.PyBestV8Runtime())
