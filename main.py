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

        elif option == '2' or option == '3':

            while True:

                note_id = int(input("Which note would You like to modify? Type id of note: "))
                if note_id <= len(notes.todo_items) + 1:
                    break
                else:
                    print("Incorrect Id! Try again!")
                    continue

                if option == '2':

                    while True:

                        new_name = input("Please type name of note (max 20 chars): ")
                        if len(new_name) <= 20 and len(new_name) > 0:
                            break
                        else:
                            print("Incorrect number of characters! Try again")
                            continue

                    notes.todo_items[note_id].change_name(new_name)

                elif option == '3':

                    while True:

                        new_description = input("Please type description of note (max 20 chars): ")
                        if len(new_description) <= 150 and len(new_description) > 0:
                            break
                        else:
                            print("Incorrect number of characters! Try again")
                            continue

                    notes.todo_items[note_id].change_description(new_description)

        elif option == '4':
            pass

        elif option == '5':
            pass

        elif option == '6':
            pass

        elif option == '7':
            pass

        elif option == '8':
            print("Good bye!")
            quit()

if __name__ == '__main__':
    main()
