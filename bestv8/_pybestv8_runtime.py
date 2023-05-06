import json
import ctypes

from bestv8._bestv8_library import runJs
import bestv8._exceptions as exceptions
from bestv8._abstract_runtime import AbstractRuntime
from bestv8._abstract_runtime_context import AbstractRuntimeContext
from bestv8._misc import encode_unicode_codepoints

_pybestv8_available = True


class PyBestV8Runtime(AbstractRuntime):
    '''Runtime to execute codes with PyBestV8.'''

    def __init__(self):
        pass

    @property
    def name(self):
        return "PyBestV8"

    def _compile(self, source, cwd=None):
        return self.Context(source)

    def is_available(self):
        return _pybestv8_available

    class Context(AbstractRuntimeContext):
        def __init__(self, source=""):
            self._source = source

        def is_available(self):
            return _pybestv8_available

        def _exec_(self, source, recv_size=20000):
            source = '''
            (function() {{
                {0};
                {1};
            }})()'''.format(
                encode_unicode_codepoints(self._source),
                encode_unicode_codepoints(source)
            )
            source = str(source)

            # backward compatibility
            if isinstance(source, str):
                source = source.encode("utf-8")
            _string_buffer = ctypes.create_string_buffer(source)
            result = bytes(recv_size)
            runJs(_string_buffer, result)
            value = result.rstrip(b"\x00").decode("utf-8")
            return self.convert(value)

        def _eval(self, source, recv_size=20000):
            _source = source.strip().replace("\n", "")
            res = self.exec_("return JSON.stringify(eval('{source}'))".format(source=encode_unicode_codepoints(_source)), recv_size=recv_size)
            self._source += "\n" + source + ";\n"
            return res

        def _call(self, identifier, *args, recv_size=20000):
            args = json.dumps(args)
            _eval_js = "{identifier}.apply(this, {args})".format(identifier=identifier, args=args)
            res = self.eval(_eval_js, recv_size=recv_size)
            return res

        def bestv8_import(self, file_path):
            self._source += f';\nbestv8import("{file_path}")'

        @classmethod
        def convert(cls, obj):
            try:
                return json.loads(obj)
            except Exception as e:
                return obj
