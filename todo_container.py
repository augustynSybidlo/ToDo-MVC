from todo_item import ToDo


class ToDoContainer(object):

    def __init__(self):
        self.todo_items = []

    def add_todo_item(self):
        self.todo_items.append(ToDo(name, description))
