import datetime
import os
import unittest

from todo import core

class TestItem(unittest.TestCase):

    def setUp(self):
        self.name = "Test Name"
        self.desc = "Test Description"
        self.today = datetime.date.today()
        self.item = core.Item(self.name, self.desc)


    def test_create_date(self):
        self.assertEqual(self.item.create_date, self.today)


    def test_format(self):
        id = '0'
        title = f'{id}|{self.today} -- {self.name}'
        width = os.get_terminal_size()[0]
        self.assertEqual(self.item.format(id, width, False), title)


if __name__ == '__main__':
    unittest.main()
