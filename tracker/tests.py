from .models import Item, Comment
from django.test import TestCase


class ItemTests(TestCase):

    def test_str(self):
        test_title = 'Test Title 1'
        item = Item(title=test_title)
        self.assertEqual(item.__str__(), test_title)


class CommentTests(TestCase):

    def test_str(self):
        test_text = 'This is simply a test'
        comment = Comment(text=test_text)
        self.assertEqual(comment.__str__(), test_text)
