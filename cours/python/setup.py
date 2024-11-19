# setup.py
import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'includes': ['tkinter'],
        'include_files': ['ass/']
    }
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Ma super application Tkinter",
    version="1.0",
    description="Une application créée avec Tkinter et cx_Freeze",
    options=options,
    executables=[Executable("app.py", base=base)]
)