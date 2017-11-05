from pprint import pprint
from todo_item import ToDo
from todo_container import ToDoContainer


def display_item_info(item, notes, header):

    line = "=" * len(header)
    width = len(header) - 4

    print(line)
    print(header)
    print(line)
    print("|{}.|{}".format(notes.todo_items.index(item), item))
    print(line, '\n', "Description: ")
    pprint(item.description, width=width)
    print(line)


def display_items(header, notes):

    print(header)
    print(notes)


def display_menu(header, menu):

    print(header)

    for option in menu:
        print(str(menu.index(option) + 1) + "----->" + option)
