#! /usr/bin/env python3

import argparse
import os

from todo import core


default_file = r'C:\Users\ccolvin\.todo'
term_width = os.get_terminal_size()[0]


def add(args):
    item = core.Item(args.name, args.description)
    with(core.ItemManager(default_file)) as mgr:
        mgr.items.append(item)


def init(args):
    with(core.ItemManager(default_file)) as mgr:
        mgr.initialize()


def view(args):
    with(core.ItemManager(default_file)) as mgr:
        for idx, item in enumerate(mgr.items):
            print(item.format(width = term_width, verbose = args.v))


parser = argparse.ArgumentParser(description='Keeps track of ToDo items')
subparsers = parser.add_subparsers()

# Build out the view options
completed_help = 'View only completed items'
id_help = 'The ID of a specific item to view'
verbose_help = 'Verbose output. Includes description and any notes.'

parser_view = subparsers.add_parser('view', help='Displays the ToDo items')
parser_view.add_argument('-c', help=completed_help, action='store_true')
parser_view.add_argument('-i', metavar='ID', type=int, help=id_help)
parser_view.add_argument('-v', help=verbose_help, action='store_true')
parser_view.set_defaults(func = view)


# Build out the add options
name_help = 'The name of the new item'
desc_help = 'The description of the new item'

parser_add = subparsers.add_parser('add', help='Adds a new ToDo item')
parser_add.add_argument('name', help=name_help)
parser_add.add_argument('description', help=desc_help)
parser_add.set_defaults(func=add)


# Build out the initialzie options
parser_init = subparsers.add_parser('init', help='Initializes a new ToDo list')
parser_init.set_defaults(func=init)

args = parser.parse_args()
args.func(args)
