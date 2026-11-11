from supplier import Supplier
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from inventory import Inventory
from order import Order


class Test:
    @staticmethod
    def association_test():
        print("##### Association Test #####")
        supplier1 = Supplier("supplier_id1", "supplier_name1", "supplier_email1")
        physical1 = PhysicalProduct("physical_product_id1", "physical_product_name1", 10, 100, 10, supplier1)
        digital1 = DigitalProduct("digital_product_id1", "digital_product_name1", 1, 1000, 100, supplier1)

        physical1.display_information()
        digital1.display_information()

    @staticmethod
    def aggregation_test():
        print("##### Aggregation Test #####")
        physical1 = PhysicalProduct("physical_product_id1", "physical_product_name1", 10, 100, 10)

        inventory1 = Inventory()
        inventory1.add_product(physical1)
        inventory1.show_all_product_details()
        inventory1.remove_product(physical1.product_id)

        inventory2 = Inventory()
        inventory2.add_product(physical1)
        inventory2.show_all_product_details()

    @staticmethod
    def composition_test():
        print("##### Composition Test #####")
        physical1 = PhysicalProduct("physical_product_id1", "physical_product_name1", 10, 100, 10)
        digital1 = DigitalProduct("digital_product_id1", "digital_product_name1", 1, 1000, 100)

        order1 = Order("order_id1")
        order1.add_order_line(physical1, 5)
        order1.add_order_line(digital1, 1)
        print(order1.calculate_total())

        order2 = Order("order_id2")
        order2.add_order_line(physical1, 50)
        order2.add_order_line(digital1, 10)

        del order1

    @staticmethod
    def substitutability_test():
        print("##### Substitutability Test #####")
        physical1 = PhysicalProduct("physical_product_id1", "physical_product_name1", 10, 100, 10)
        digital1 = DigitalProduct("digital_product_id1", "digital_product_name1", 1, 1000, 100)

        inventory1 = Inventory()
        inventory1.add_product(physical1)
        inventory1.add_product(digital1)
        inventory1.show_all_product_details()

    @staticmethod
    def polymorphism_test():
        print("##### Polymorphism Test #####")
        physical1 = PhysicalProduct("physical_product_id1", "physical_product_name1", 10, 100, 10)
        digital1 = DigitalProduct("digital_product_id1", "digital_product_name1", 1, 1000, 100)

        inventory1 = Inventory()
        inventory1.add_product(physical1)
        inventory1.add_product(digital1)
        inventory1.show_all_product_details()

if __name__ == "__main__":
    test = Test()
    test.association_test()
    test.aggregation_test()
    test.composition_test()
    test.substitutability_test()
    test.polymorphism_test()
