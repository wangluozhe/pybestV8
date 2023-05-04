from sys import platform
from platform import machine
import ctypes
import os

if platform == 'darwin':
	file_ext = '_mac_m.dylib' if machine() == "arm64" else '_mac_intel.dylib'
elif platform in ('win32', 'cygwin'):
	if 8 == ctypes.sizeof(ctypes.c_voidp):
		file_ext = '_win64.dll'
	else:
		file_ext = '_win32.dll'
		raise Exception("win32 system not currently supported")
else:
	if machine() == "aarch64":
		file_ext = '_arm64.so'
		raise Exception("arm64 system not currently supported")
	elif "x86" in machine():
		file_ext = '_x86.so'
		raise Exception("x86 system not currently supported")
	else:
		file_ext = '_x64.so'

root_dir = os.path.abspath(os.path.dirname(__file__))
library = ctypes.cdll.LoadLibrary(f'{root_dir}/dependencies/bestV8{file_ext}')

# extract the exposed runJs function from the shared package
runJs = library.runJs
runJs.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
