'''
Mitchell Carroll
21 Aug 2020

This module returns the path or dir of the currently running python script.
Can be used to reference local files to the directory of the script file and not the 
current working directory. 

Ensure to pass lamda:0 as the function to the defined methods.

'''

from inspect import getsourcefile
from os.path import abspath
from os import path


def get_path(func):
    return(abspath(getsourcefile(func)))


def get_dir(func):
    return(path.dirname(abspath(getsourcefile(func))))
