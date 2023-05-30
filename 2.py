class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана {self.restaurant_name} Кухня: {self.cuisine_type}.")

    def open_restaurant(self):
        print("Ресторан сейчас открыт")


restaurant1 = Restaurant("Даймохк", "Чеченская")
restaurant2 = Restaurant("Жумайсынба", "Казахская")
restaurant3 = Restaurant("Лееее", "Дагестанская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()