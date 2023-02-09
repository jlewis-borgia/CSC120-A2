from computer import *

# ResaleShop class adds and removes computer to the store's inventory
class ResaleShop:

    # What attributes will it need?

    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    #def buy(self):
       # 1. Call Computer(...) constructer 
       #       to create a new computer instance
       #
       # 2. Call inventory.append(...) to add the
       #    new Computer instance to the inventory

    # buys computer by adding it to inventory
    def buy_computer(self, new_computer):
        self.inventory.append(new_computer)
        print("New computer has been added to the store inventory.")
    
    # sells computer by removing to to inventory
    def sell_computer(self, new_computer):
        self.inventory.remove(new_computer)
        print("This computer has been removed from the store's inventory.")


    