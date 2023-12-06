from HW_1.cls_1 import Product


class Phone(Product):
    def __init__(self, name, price, description, model, color):
        super().__init__(name, price, description)
        self.model = model
        self.color = color

    def phone_method(self):
        return self.model, self.price, self.color


class Laptop(Phone):
    def __init__(self, name, price, description, model, color):
        super().__init__(name, price, description, model, color)

    def laptop_method(self):
        return self.model, self.price, self.color

