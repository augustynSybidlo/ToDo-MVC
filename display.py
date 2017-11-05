from pprint import pprint
from todo_item import ToDo
from todo_container import ToDoContainer


def display_all_info(item, notes):

    header = "|Id| Status|          Name         ||"
    line = "=" * len(header)
    width = len(header) - 4

    print(line)
    print(header)
    print(line)
    print("|{}.|".format(notes.todo_items.index(item) + 1), item)
    print(line, '\n', "Description: ")
    pprint(item.description, width=width)
    print(line)


def display_menu(header, menu):

    print(header)

    for option in menu:
        print(str(menu.index(option) + 1) + "----->" + option)


note1 = ToDo("zrobic pranie i rozw", "pranie na dzis: kpasofiapofipsoi, aisdfpoiasdfpoiaolorowe, ciemne, rozwiesic")
temp_list = ToDoContainer()
temp_list.add_todo_item(note1)
#print(temp_list.__str__())
display_all_info(note1, temp_list)