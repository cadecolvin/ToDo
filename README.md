# ToDo
ToDo is a simple command-line to do tracking application. Each item will have a name, description, created date, and 0 or more notes. Once the item is marked as complete, the date it was completed will be saved as well.

# Usage
`todo {view,add,done,note,init}`

## View
`todo view [-c] [-i ID] [-v]`
Running 'ToDo' with the 'view' verb will list the open to do items.

`todo view -c`
Will return items marked as completed.

`todo view -v`
Will return the verbose output for each item. This includes the description and any added notes.

`todo view -i [id]`
Will return the verbose output for to do item with the specified ID.

## Add
`todo add [name] [description]`
Adds a new to do item with the given name and description.

## Done
`todo done [id]`
Marks a to do item as complete.

## Note
`todo note [id] [text]`
Appends a note with the given text to the specified to do item.

## Init
`todo init`
Deletes the current list of to do items and generates a new empty one.
