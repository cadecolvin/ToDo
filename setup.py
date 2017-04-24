import re
from setuptools import setup


setup(
    name='ToDo',
    packages=['todo'],
    entry_points={'console_scripts': ['todo = todo.todo:main']},
    version='1.1',
    description='A simple command line ToDo list',
    author='Cade Colvin',
    author_email='cade.colvin@gmail.com'
    )
