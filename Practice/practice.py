class Customer:
    def __init__(self,name,CID,exp):
        self.name=name
        self.name=CID
        self.exp=exp

    def dicountP(self):
        if (self.exp>5):
            print("Dicount of 50% on the items")
        elif(self.exp<5 and self.exp>=1):
            print("Discount is 25% on the products")
        else:
            print("No disocunt !!")
cust=Customer("Sam",342123,4)
cust.dicountP()


