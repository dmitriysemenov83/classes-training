from HW_1.electr_dev import Laptop


class Boots(Laptop):
    def __init__(self, name, price, description, model, color, sizes):
        super().__init__(name, price, description, model, color)
        self.sizes = sizes

    def boots_method(self):
        return self.name, self.description, self.price

    def get_size(self):
        return self.sizes


class Jacket(Boots):
    def __init__(self, name, price, description, model, color, sizes):
        super().__init__(name, price, description, model, color, sizes)

    def get_description(self):
        return self.description

