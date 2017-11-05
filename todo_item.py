class ToDo(object):

    def __init__(self, name, description):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string!")
        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError("Description must be a string!")
        self.is_done = False

    def mark(self):
        self.is_done = True

    def change_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            raise ValueError("Name must be a string!")

    def change_description(self, new_description):
        if isinstance(new_description, str):
            self.description = new_description
        else:
            raise ValueError("Description must be a string!")

    def __str__(self):
        if self.is_done is True:
            return " [x]  | {} ||".format((self.name + " " * (21 - len(self.name))))
        else:
            return " [ ]  | {} ||".format((self.name + " " * (21 - len(self.name))))
