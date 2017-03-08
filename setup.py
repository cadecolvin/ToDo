import re
from setuptools import setup


with open('todo/todo.py', 'r') as f:
    version_re = '^__version__\s*=\s*\'(.*)\''
    version = re.search(version_re, f.read(), re.M).group(1)



setup(
    name = 'ToDo',
    packages = ['todo'],
    entry_points = {'console_scripts': ['todo = todo.todo:main']},
    version = version,
    description = 'A simple command line ToDo list',
    author = 'Cade Colvin',
    author_email = 'cade.colvin@gmail.com'
    )
