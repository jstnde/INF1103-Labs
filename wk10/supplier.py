class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def display_information(self) -> None:
        print(f"id: {self.__supplier_id} | name: {self.__name} | email: {self.__contact_email}")
