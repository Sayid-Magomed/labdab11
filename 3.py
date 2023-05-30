class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f"Название ресторана {self.restaurant_name}кухня: {self.cuisine_type}  русская .")

    def open_restaurant(self):
        print("Ресторан сейчас открыт.")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} Был обновлен до  {self.rating}.")




restaurant1 = Restaurant("Р0", "Русская", 2)

# текущий рейтинг ресторана
print(f"Изначальный рейтинг ресторана {restaurant1.restaurant_name}   {restaurant1.rating} .")

# выводим новое значение
restaurant1.update_rating(5)
print(f"Новый, обновленный рейтинг  {restaurant1.restaurant_name} : {restaurant1.rating}.")