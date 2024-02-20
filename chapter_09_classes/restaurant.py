"""A set of classes to implement a restaurant object."""

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize a new instance."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(self.restaurant_name.title() + " is a restaurant with " 
              + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        """Open the restaurant."""
        print(self.restaurant_name.title() + " is now open!")

    def set_number_served(self, served):
        """Sets the number of customers served."""
        self.number_served = served

    def increment_number_served(self, increment):
        """Increment the number of customers served."""
        self.number_served += increment
   

class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'cacao', 'strawberry', 'pistachio']

    def display_flavors(self):
        """Display available ice cream flavors."""
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(" - " + flavor.title())