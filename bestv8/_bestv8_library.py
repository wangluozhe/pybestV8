from sys import platform
from platform import machine
import ctypes
import os

if platform == 'darwin':
	file_ext = '_mac_m.dylib' if machine() == "arm64" else '_mac_intel.dylib'
elif platform in ('win32', 'cygwin'):
	file_ext = '_win64.dll' if 8 == ctypes.sizeof(ctypes.c_voidp) else '_win32.dll'
else:
	if machine() == "aarch64":
		file_ext = '_arm64.so'
	elif "x86" in machine():
		file_ext = '_x86.so'
	else:
		file_ext = '_x64.so'

root_dir = os.path.abspath(os.path.dirname(__file__))
library = ctypes.cdll.LoadLibrary(f'{root_dir}/dependencies/bestV8{file_ext}')

# extract the exposed runJs function from the shared package
runJs = library.runJs
runJs.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
