class Inventory:
    def __init__(self, products=None):
        if products is None:
            products = list()
        self.__products = products

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self):
        pass

    def display_all(self):
        for product in self.__products:
            product.display_information()
