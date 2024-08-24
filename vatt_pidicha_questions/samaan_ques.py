class Shop:

    products = {"tomato":70,"onion":80,"carrot":120,"potato":40,"chillie":150}

    def __init__(self):
        
        print("--------------------------------")
        for key,value in self.products.items():
            print(f"{key} : {value}")
        print("--------------------------------")

        self.quantity = int(input("Enter the quantity in kg: "))
        self.product = input("Enter the item you want to purchase: ").lower()

    def display_bill(self):
        self.price = 0
        if self.product in self.products:
            self.price = self.products[self.product]*self.quantity 
            print(f"You need to pay {self.price} rs")

        else:
            print("The product is not available")

obj1 = Shop()
obj1.display_bill()
