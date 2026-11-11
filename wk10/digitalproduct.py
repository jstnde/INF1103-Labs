from product import Product, Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: int, supplier: Supplier | None = None):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size}")

    def get_fulfilment_info(self) -> str:
        return "Product is delivered digitally."

    def __dict__(self) -> dict[str, str | float | int]:
        digital = super().__dict__()
        digital.update({"download_size": self.__download_size})
        return digital
