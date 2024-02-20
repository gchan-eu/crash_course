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
        
user1 = User('georgios', 'chantzopoulos', 'm', 'switzerland')
user1.describe_user()
user1.greet_user()

user2 = User('anna', 'polina', 'f')
user2.describe_user()
user2.greet_user()

user3 = User('clea', 'gaultier', 'f', 'france')
user3.describe_user()
user3.greet_user()

user4 = User('michelle', 'lowry', 'f', 'usa')
user4.describe_user()
user4.greet_user()