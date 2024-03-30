class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} был добавлен {self.name}")
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален {self.name}")
    def get_price(self,item_name):
        return self.items.get(item_name)
    def update_price(self, item_name, new_prise):
        if item_name in self.items:
            self.items[item_name] = new_prise
            print(f"Цена на товар {item_name} обновлен в {self.name}")
        else:
            print(f"Товар {item_name} не найден")

shop_1 = Store("Фрукты","Набережная 20а")
shop_2 = Store("Мясо", "Вишнёвая 15/2")
shop_3 = Store("Хлеб","Южная 5")


shop_1.add_item("Яблоки", 110)
shop_2.add_item("Говядина", 500)
shop_3.add_item("Ржаной", 45)

shop_1.remove_item("Яблоки")

print(shop_1.get_price("Яблоки"))

shop_2.update_price("Говядина", 560)

















