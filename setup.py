from cx_Freeze import setup, Executable
import sys


base = None
if sys.platform == "win32":
    base = "Win32GUI"  # enlever console

build_exe_options = {
    "packages": [
        "os",
        "subprocess",
        "hashlib",
        "itertools",
        "string",
        "time",
        "random",
        "secrets",
        "bcrypt",
        "PySimpleGUI4"
    ],
    "includes": ["bcrypt"],
    "include_files": [
        ("hashcat", "hashcat")  
    ],
    "excludes": [],
    "include_msvcr": True
}

setup(
    name="PasswordSecurityTool",
    version="1.0",
    description="Outil pédagogique de génération et brute force de mots de passe avec Python et Hashcat",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "main.py",
            base=base,
            target_name="PasswordSecurityTool.exe"
        )
    ]
)

# python setup.py build