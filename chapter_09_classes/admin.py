from user import User

class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(" - " + privilege.title())


class Admin(User):
    """A model for admin, a special user."""

    def __init__(self, first_name, last_name, gender, birth_country=''):
        super().__init__(first_name, last_name, gender, birth_country)
        self.privileges = Privileges()