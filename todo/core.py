import datetime
import os
import pickle
from textwrap import TextWrapper


class Item():
    '''Represents a ToDo item.'''
    def __init__(self, name, description):
        print('making a new item')
        self.name = name
        self.description = description
        self.create_date = datetime.date.today()
        self.completed = False
        self.notes = list()


    def __str__(self):
        return self.name


    def format(self, width = 70, verbose = False):
        title = f'{self.create_date} -- {self.name}'

        if not verbose:
            return title

        wrapper = TextWrapper(width=width, expand_tabs=True)
        wrapper.initial_indent = '    '
        wrapper.subsequent_indent = '    '

        wrapped_desc = wrapper.fill(self.description)


        return '\n'.join([title, wrapped_desc])



class ItemManager:
    '''Saves and loads the items at the path specified'''
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = list()


    def __enter__(self):
        self.load()
        return self


    def __exit__(self, type, value, traceback):
        self.save()


    def save(self):
        with open(self.file_path, 'wb') as f:
            pickle.dump(self.items, f)


    def load(self):
        try:
            with open(self.file_path, 'rb') as f:
                self.items = pickle.load(f)
        except:
            self.initialize()

    
    def initialize(self):
        self.items = list()
        open(self.file_path, 'w').close()
