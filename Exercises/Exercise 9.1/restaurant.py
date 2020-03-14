class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print("The name of the Restaurant is " + self.restaurant_name.title() + ".")
        print("The most popular dish here is " + self.cuisine_type.title() + ".")

    def open_resturant(self):

        print("The restaurant is currently open.")

restaurant = Restaurant('dominos', 'pizza')

restaurant.describe_restaurant()
restaurant.open_resturant()

