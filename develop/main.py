class Category:
    name = str
    abuse = str
    goods = str
    def __init__(self,name,abuse,goods):
        self.name = name
        self.abuse = abuse
        self.goods = goods




class Product:
    name = str
    abuse = str
    value = float
    quantity_in_stock = int
    def __init__(self, name, abuse, value, quantity_in_stock):
        self.name = name
        self.abuse = abuse
        self.value = value
        self.quantity_in_stock = quantity_in_stock

