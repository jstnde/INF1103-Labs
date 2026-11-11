from product import Product
from canbeshipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: int):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}")

    def get_fulfilment_info(self):
        print("Product requires physical shipping.")

    def __dict__(self) -> dict[str, str | float | int]:
        physical = super().__dict__()
        physical.update({"weight": self.__weight})
        return physical

    def calculate_shipping_cost(self) -> float:
        return self.__weight * .1
