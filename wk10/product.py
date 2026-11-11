from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int = 0):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def product_id(self) -> str:
        return self.__product_id

    def update_stock(self, quantity: int):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def __dict__(self) -> dict[str, str | float | int]:
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass


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


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: int):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size}")

    def get_fulfilment_info(self):
        print("Product is delivered digitally.")

    def __dict__(self) -> dict[str, str | float | int]:
        digital = super().__dict__()
        digital.update({"download_size": self.__download_size})
        return digital
