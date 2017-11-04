from pprint import pprint
from todo_item import ToDo
from todo_container import ToDoContainer


def display_all_info(item_info):
    header = "||Status|          Name         ||"
    line = "=" * len(header)
    width = len(header) - 4
    print(line)
    print(header)
    print(line)
    print(item_info)
    print(line, '\n', "Description: ")
    pprint(item_info.description, width=width)
    print(line)

# note1 = ToDo("zrobic pranie i rozw", "pranie na dzis: kpasofiapofipsoi, aisdfpoiasdfpoiaolorowe, ciemne, rozwiesic")
# display_all_info(note1)