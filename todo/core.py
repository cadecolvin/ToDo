import datetime
import pickle
from textwrap import TextWrapper


class Item:
    """Represents a ToDo item.
    
    Args:
        name (str): The name/title of the item
        description (str): A longer description of the item

    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.create_date = datetime.date.today()
        self.complete_date = datetime.date.today()
        self.completed = False
        self.notes = list()

    def __str__(self):
        return self.name

    def format(self, id, width, verbose):
        """Formats the todo item to fit on the screen

        Returns a string representation of the todo item that fits
        within a terminal window of `width`.

        Args:
            id (int): The id of the todo item to format
            width (int): The width of the screen to format for
            verbose (bool): 
                If True, include all `notes`
                If False, only include title

        Returns:
            str: A string formatted according to `width` and `verbose`.

        """
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
    """Saves and loads the items at the path specified
    
    Args:
        file_path (str): The path to store/load todo items

    """
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
            all_items = self.open_items + self.completed_items
            pickle.dump(all_items, f)

    def load(self):
        try:
            with open(self.file_path, 'rb') as f:
                self.items = pickle.load(f)
                self.open_items = [item for item in self.items if item.completed == False]
                self.completed_items = [item for item in self.items if item.completed == True]
        except:
            print('Unknown error. Please run \'todo -h\' for help')

    def initialize(self):
        self.items = list()
        open(self.file_path, 'w').close()

    def complete(self, id):
        self.open_items[id].complete_date = datetime.date.today()
        self.open_items[id].completed = True

        self.completed_items.append(self.open_items[id])
        del self.open_items[id]
