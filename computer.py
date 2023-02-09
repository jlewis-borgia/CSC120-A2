#the computer class updates computer price and operating systems
class Computer:


    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # This constructor sets all attributes
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price) -> None:
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # updates price of computer
    def update_price(self, new_price) -> int:
        self.price = new_price
        print("The price has been changed to", self.price)


    # updates the operating system
    def refurbish(self, new_OS):
        self.operating_system = new_OS
        print("The new OS system is", new_OS)
