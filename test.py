import sys
print(sys.stdout.isatty())
print(sys.stdout.encoding)
print(sys.getfilesystemencoding())

import locale
print(locale.getpreferredencoding())

import os
print(os.environ.get("PYTHONIOENCODING"))

print("║")
print("║")
print("║")
print("║")
print("║")
print("║")
print("╚═══════════")
