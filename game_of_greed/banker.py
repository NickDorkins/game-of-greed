class Banker:

    def __init__(self):
        self.balance = 0
        self.shelved = 0
    
    

# Shelf_Method 
# Input - Integer (Current dice roll unbanked points)
# Output - integer (Print total unbanked points) 
    def shelf(self, points):
        self.shelved += points 
        

# Shelf_Bank Method
# input - integer (Output total of Shelf_Method)
# Output - integer (Running total of all inputs from the Shelf_Method)
    def bank(self):
        self.balance += self.shelved
        self.clear_shelf()

        

# Clear_shelf method
# Zero Total in the shelf method 
    # Banked points
    # Zero out on your turn 
    def clear_shelf(self):
        self.shelved = 0

