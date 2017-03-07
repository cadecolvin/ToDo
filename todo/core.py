import datetime
import pickle


class Item():
    '''Represents a ToDo item.'''
    def __init__(self, name, description):
        print('making a new item')
        self.name = name
        self.description = description
        self.create_date = datetime.date
        self.completed = False
        self.notes = list()


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
        with open(self.file_path, 'w') as f:
            pickle.dump(self.items, f)


    def load(self):
        with open(self.file_path, 'r') as f:
            try:
                self.items = pickle.load(f)
            except:
                pass
