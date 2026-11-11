from product import Product


class Inventory:
    def __init__(self, products: list[Product] | None = None):
        if products is None:
            products = list()
        self.__products: list[Product] = products

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        product = self.search_product(product_id)
        if product:
            self.__products.remove(product)

    # basically the find_product operation
    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self) -> None:
        if len(self.__products) == 0:
            print("Current Inventory is Empty!")
        else:
            for product in self.__products:
                product.display_information()

    def __dict__(self) -> list[dict]:
        products = []
        for product in self.__products:
            products.append(product.__dict__())
        return products

    @staticmethod
    def show_product_details(product: Product) -> None:
        product.display_information()
        print(product.get_fulfilment_info())

    def show_all_product_details(self) -> None:
        for product in self.__products:
            self.show_product_details(product)
