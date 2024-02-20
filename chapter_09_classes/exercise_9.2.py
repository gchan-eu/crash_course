class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize a new instance."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(self.restaurant_name.title() + " is a restaurant with " 
              + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        """Open the restaurant."""
        print(self.restaurant_name.title() + " is now open!")


restaurant = Restaurant('abonna', 'italian')
restaurant.describe_restaurant()
restaurant = Restaurant('east pearl', 'chinese')
restaurant.describe_restaurant()
restaurant = Restaurant('dos hermanos', 'mexican')
restaurant.describe_restaurant()