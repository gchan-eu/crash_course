class User():
    """A model for user objects."""

    def __init__(self, first_name, last_name, gender, birth_country=''):
        """Initialize a user object."""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_country = birth_country

    def describe_user(self):
        """Describe a user."""
        print("\nUser full name is " + self.first_name.title() 
              + " " + self.last_name.title() + ".")
        if self.birth_country:
            if self.gender == 'f':
                print("She was born in " + self.birth_country.title() + ".")
            elif self.gender == 'm':
                print("He was born in " + self.birth_country.title() + ".")

    def greet_user(self):
        """Greet a user."""
        print("Hello " + self.first_name.title() 
              + " " + self.last_name.title() + ".")
        
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


admin = Admin('anna', 'polina', 'f', 'france')
admin.describe_user()
admin.privileges.show_privileges()

