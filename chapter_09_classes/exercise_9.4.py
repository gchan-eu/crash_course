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
   

restaurant = Restaurant('abonna', 'italian')
restaurant.describe_restaurant()
print(restaurant.restaurant_name.title() + " has served " 
      + str(restaurant.number_served) + " customers today.")
restaurant.number_served = 56
print(restaurant.restaurant_name.title() + " has served " 
      + str(restaurant.number_served) + " customers today.")
restaurant.set_number_served(67)
print(restaurant.restaurant_name.title() + " has served " 
      + str(restaurant.number_served) + " customers today.")
restaurant.increment_number_served(100)
print(restaurant.restaurant_name.title() + " has served " 
      + str(restaurant.number_served) + " customers today.")