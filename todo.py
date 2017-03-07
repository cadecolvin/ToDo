import argparse
import os

from todo import core

default_file = r'C:\Users\ccolvin\.todo'

def view(args):
    with(core.ItemManager(default_file)) as mgr:
        for item in mgr.items:
            print(item.name)


def add(args):
    item = core.Item(args.name, args.description)
    with(core.ItemManager(default_file)) as mgr:
        mgr.items.append(item)


parser = argparse.ArgumentParser(description='Keeps track of ToDo items')
subparsers = parser.add_subparsers()

# Build out the view options
id_help = 'The ID of a specific item to view'
completed_help = 'View only completed items'

parser_view = subparsers.add_parser('view', help='Displays the ToDo items')
parser_view.add_argument('-i', type=int, help=id_help)
parser_view.add_argument('-c', help=completed_help, action='store_true')
parser_view.set_defaults(func = view)


# Build out the add options
name_help = 'The name of the new item'
desc_help = 'The description of the new item'

parser_add = subparsers.add_parser('add', help='Adds a new ToDo item')
parser_add.add_argument('name', help=name_help)
parser_add.add_argument('description', help=desc_help)
parser_add.set_defaults(func=add)


args = parser.parse_args()
args.func(args)
