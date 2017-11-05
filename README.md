# ToDo-MVC
Small "ToDo" app, with use of MVC pattern.

## The specification

### `main.py`
TODO

### `todo_item.py`

This is the file containing a todo_item logic.

### Class Todo

__Attributes__

* `name`
  - data: string
  - description: name of todo_item

* `description`
  - data: string
  - description: description of todo_item

* `is_done`
  - data: bool
  - description: contains True if TODO item is done, otherwise contains False.  Default value is False

__Instance methods__

* ##### ` __init__(self, title, deadline)`

  Constructs an ToDoItem object

* `mark(self)`

  Sets the object's * is_done * attribute to True

* `change_name(self, new_name)`

  Changes instance attribute: name
  - data: string

* `change_description(self, new_description)`

  Changes instance attribute: description
  - data: string

* `__str__(self)`

  Returns a formatted string with details about todo_item.

### `todo_container.py`

This is the file containing a logic of an todo_container.

### Class TodoContainer

__Instance Attributes__

* `todo_items`
  - data: list
  - description: list of Todo objects

__Instance methods__

* ##### ` __init__(self) `

  Constructs a *ToDoContainer* object with list of Todo objects

* `add_item(self, name, description)`

  Append *Todo* object to *todo_items*

To Be Continued...
