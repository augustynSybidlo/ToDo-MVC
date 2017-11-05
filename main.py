import os
from display import *
from todo_container import ToDoContainer
from todo_item import ToDo


def main():

    header = "|Id| Status|          Name         ||"
    header_2 = '''<===To Do App===>
    Options:\n'''

    menu = ["Add To Do item",
            "Change name of note",
            "Change description of note",
            "Delete item",
            "Mark item as done",
            "Display items list",
            "Display specific todo item's details",
            "Quit"]

    notes = ToDoContainer()

    while True:

        display_menu(header_2, menu)
        option = input("Please select an option: ")
        os.system('clear')

        if option == '1':

            display_items(header, notes)
            while True:

                name = input("Please type name of note (max 20 chars): ")
                if len(name) <= 20 and len(name) > 0:
                    break
                else:
                    print("Incorrect number of characters! Try again")
                    continue

            while True:

                description = input("Please type description of note (max 150 chars): ")
                if len(description) <= 150 and len(description) > 0:
                    break
                else:
                    print("Incorrect number of characters! Try again")
                    continue

            notes.add_todo_item(ToDo(name, description))

        elif option in ('2', '3', '4', '5', '7') and len(notes.todo_items) > 0:

            while True:

                display_items(header, notes)
                try:
                    note_id = int(input("Which note would you like to choose? Type Id of note: "))
                    if note_id <= len(notes.todo_items) - 1:
                        os.system('clear')
                        break
                    else:
                        print("Incorrect Id! Try again!")
                        continue
                except ValueError:
                    print("Must be intiger!")
                else:
                    break

            if option == '2':

                while True:

                    new_name = input("Please type new name of note (max 20 chars): ")
                    if len(new_name) <= 20 and len(new_name) > 0:
                        break
                    else:
                        print("Incorrect number of characters! Try again")
                        continue

                notes.todo_items[note_id].change_name(new_name)

            elif option == '3':

                while True:

                    new_description = input("Please type new description of note (max 150 chars): ")
                    if len(new_description) <= 150 and len(new_description) > 0:
                        break
                    else:
                        print("Incorrect number of characters! Try again")
                        continue

                notes.todo_items[note_id].change_description(new_description)

            elif option == '4':

                notes.delete_item(note_id)

            elif option == '5':

                notes.todo_items[note_id].mark()

            elif option == '7':
                item = notes.todo_items[note_id]
                display_item_info(item, notes, header)

        elif option == '6':

            display_items(header, notes)

        elif option == '8':
            print("Good bye!")
            quit()

if __name__ == '__main__':
    main()
