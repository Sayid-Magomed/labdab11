class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана {self.restaurant_name} Кухня: {self.cuisine_type}.")

    def open_restaurant(self):
        print("Ресторан сейчас открыт")


restaurant1 = Restaurant("Hi", "странная")
restaurant2 = Restaurant("Jo", "Японская")
restaurant3 = Restaurant("Р0", "Русская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()