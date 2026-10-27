from product import Product


class Inventory:
    def __init__(self, products=None):
        if products is None:
            products = list()
        self.__products = products

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self):
        if len(self.__products) == 0:
            print("Current Inventory is Empty!")
        else:
            for product in self.__products:
                product.display_information()

    def __dict__(self):
        products = []
        for product in self.__products:
            products.append(product.__dict__())
        return products
