from wk8.product import Product


class Inventory:
    def __init__(self, products=None):
        if products is None:
            products = list()
        self.__products = products

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id, display:bool = False) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                if display:
                    product.display_information()
                return product
        if display:
            print("Product Not Found.")
        return None

    def display_all(self):
        for product in self.__products:
            product.display_information()
