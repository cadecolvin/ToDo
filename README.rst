ToDo
====
ToDo is a simple command-line ToDo tracking application. Each item has a name, description, created date, and 0 or more notes.
Once the item is marked as complete, the date it was completed will be saved as well.

Usage
=====
::

    $ todo {view,add,done,note,init}

View
----

Running ToDo with the **view** verb will list the open items::

    todo view [-c] [-i ID] [-v]

Passing the **-c** flag will return items marked as completed::

    $ todo view -c

Passing the **-v** flag will return the verbose output for each item. This includes the description as well as all notes::

    $ todo view -v

Passing the **-i** flag will return the verbose output for the item with the specified ID::

    $ todo view -i [ID]

Add
---

Adds a new item with the given **name** and **description**::

    $ todo add [name] [description]

Done
----

Marks an item as complete::

    $ todo done [id]

Note
----

Appends a note with the given **text** to item with the specified **id**::

    $ todo note [id] [text]

Init
----

Deletes the current list of items and generates a new empty one::

    $ todo init
