def main():
    from oo_resale_shop import ResaleShop
    from computer import Computer
        # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    global my_computer
    
# adds a computer to inventory
    print("Buying Computer...")
    my_computer = Computer("Mac Pro (Late 2013)", 
    "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,
    "macOS Big Sur", 2013, 1500)
    print("The store has bought this computer!")
    my_inventory = ResaleShop()
    print("Let's add this computer to the inventory.")
    my_inventory.buy_computer(my_computer)

# changes price of computer
    print("Let's change the price of the computer.")
    my_computer.update_price(1300)

# changes the operating system
    print("Now let's refurbish the computer's operating system.")
    my_computer.refurbish("macOS Monterey")

# sells computer by removing it from operating system
    print("Not let's sell this computer. This means it must be taken out of the store's inventory.")
    my_inventory.sell_computer(my_computer)

main()