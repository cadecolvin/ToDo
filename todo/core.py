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


    def format(self, id, width, verbose):
        if self.completed:
            title = f'{id}|{self.complete_date} -- {self.name}'
        else:
            title = f'{id}|{self.create_date} -- {self.name}'

        if not verbose:
            return title

        wrapper = TextWrapper(width=width, expand_tabs=True)
        wrapper.initial_indent = '   -'
        wrapper.subsequent_indent = '    '

        wrapped_desc = wrapper.fill(self.description)

        wrapped_notes = list()
        for note in self.notes:
            wrapped_notes.append(wrapper.fill(note))
        wrapped_notes = '\n'.join(wrapped_notes)

        return '\n'.join([title, wrapped_desc, wrapped_notes])


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
            print('Unknown error. Please run \'todo -h\' for help')

    
    def initialize(self):
        self.items = list()
        open(self.file_path, 'w').close()


    def complete(self, id):
        self.items[id].complete_date = datetime.date.today()
        self.items[id].completed = True
