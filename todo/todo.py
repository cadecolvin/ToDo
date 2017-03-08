#! /usr/bin/env python3

import argparse
import os
import sys

from todo import core


__version__ = '1.0'


default_file = r'C:\Users\ccolvin\.todo'
term_width = os.get_terminal_size()[0]


def add(args):
    item = core.Item(args.name, args.description)
    with(core.ItemManager(default_file)) as mgr:
        mgr.items.append(item)


def done(args):
    with(core.ItemManager(default_file)) as mgr:
        mgr.complete(args.id)


def note(args):
    with(core.ItemManager(default_file)) as mgr:
        mgr.items[args.id].notes.append(args.text)


def init(args):
    with(core.ItemManager(default_file)) as mgr:
        mgr.initialize()


def view(args):
    with(core.ItemManager(default_file)) as mgr:
        for idx, item in enumerate(mgr.items):
            if item.completed == args.c:
                print(item.format(idx, term_width, args.v))


def main():
    parser = argparse.ArgumentParser(description='Keeps track of ToDo items')
    subparsers = parser.add_subparsers()

    # Build out the view options
    completed_help = 'View only completed items'
    id_help = 'The ID of a specific item to view'
    verbose_help = 'Verbose output. Includes description and any notes.'

    parser_view = subparsers.add_parser('view',
                                        help='Displays the ToDo items')
    parser_view.add_argument('-c', help=completed_help, action='store_true')
    parser_view.add_argument('-i', metavar='ID', type=int, help=id_help)
    parser_view.add_argument('-v', help=verbose_help, action='store_true')
    parser_view.set_defaults(func=view)

    # Build out the add options
    name_help = 'The name of the new item'
    desc_help = 'The description of the new item'

    parser_add = subparsers.add_parser('add', help='Adds a new ToDo item')
    parser_add.add_argument('name', help=name_help)
    parser_add.add_argument('description', help=desc_help)
    parser_add.set_defaults(func=add)

    # Build out the done options
    id_help = 'The id of the item to mark as complete'

    parser_done = subparsers.add_parser('done',
                                        help='Marks an item as complete')
    parser_done.add_argument('id', type=int, help=id_help)
    parser_done.set_defaults(func=done)

    # Build out the note options
    id_help = 'The id of the item to add the note to'
    text_help = 'The note to add to the item'

    parser_note = subparsers.add_parser('note', help='Adds a note to an item')
    parser_note.add_argument('id', type=int, help=id_help)
    parser_note.add_argument('text', help=text_help)
    parser_note.set_defaults(func=note)

    # Build out the initialize options
    parser_init = subparsers.add_parser('init',
                                        help='Initializes a new ToDo list')
    parser_init.set_defaults(func=init)

    # Ensure that an argument was passed
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit(1)

    args = parser.parse_args()
    args.func(args)
