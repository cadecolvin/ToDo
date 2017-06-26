ToDo
====
ToDo is a simple command-line ToDo tracking application. Each item has a name, description, created date, and 0 or more notes.
Once the item is marked as complete, the date it was completed will be saved as well.

Usage
=====
code-block:: bash
    $ todo {view,add,done,note,init}

View
----
Running ToDo with the 'view' verb will list the open items
code-block:: bash
    $ todo view [-c] [-i ID] [-v]

Passing the **-c** flag will return items marked as completed::
code-block:: bash
    $ todo view -c

Passing the **-v** flag will return the verbose output for each item. This includes the description as well as all notes
code-block:: bash
    $ todo view -v

Passwing the **-i** flag will return the verbose output for the item with the specified ID
code-block:: bash
    $ todo view -i [ID]

Add
---
Adds a new item with the given **name** and **description**
code-block:: bash
    $ todo add [name] [description]

Done
----
Marks an item as complete
code-block:: bash
    $ todo done [id]

Note
----
Appends a note with the given **text** to item with the specified **id**
code-block:: bash
    $ todo note [id] [text]

Init
----
Deletes the current list of items and generates a new empty one
code-block:: bash
    $ todo init
