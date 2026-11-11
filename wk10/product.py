from abc import ABC, abstractmethod


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
