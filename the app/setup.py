import sys
import os
from cx_Freeze import setup , Executable

files=['logo.jpg']

target = Executable(
    script="CRUD.py",
    base='Win32GUI',
    icon='logo.jpg',
)

setup(
    name ='NASSER SWIMMING ACADIMY',
    version= '1.0',
    description = 'subscription program',
    auther = 'Mohammed S. hussen',
    options = {'build_exe': {'include_files':files}},
    executables= [target]
)
