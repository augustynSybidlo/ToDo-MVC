from todo_item import ToDo


class ToDoContainer(object):

    def __init__(self):
        self.todo_items = []

    def add_todo_item(self, item):
        self.todo_items.append(item)

    def delete_item(self, index):
        self.todo_items.pop(index)

    def __str__(self):
        notes = ""

        for item in self.todo_items:
            notes += "|{}{} \n".format(self.todo_items.index(item), item.__str__())

        return notes
