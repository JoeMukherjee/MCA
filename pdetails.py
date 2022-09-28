class Products:
            def __init__(self):
                        self.productID=input("Enter product ID: ")
                        self.productName=input("Enter product name: ")
                        self.price=input("Enter product price: ")
                        self.quantity=input("Enter product quantity: ")
            def getPid(self):
                        return self.productID
            def displayPdetails(self):
                        print("The product name is "+self.productName+".")
                        print("The product quantity is "+self.quantity+".")
NoP=int(input("Enter number of prorducts to store: "))
e=[]
pID=[]
for i in range(0,NoP):
            e.append(Products())
            # print(str(e))
            pID.append(e[i].getPid())
viewID=input("Enter the necessary product's ID: ")
for j in range(0,NoP):
            if (pID[j]==viewID):
                        e[j].displayPdetails()
                        break
            else: 
                        print("ERROR: Product ID mismatch")
                        break
            # elif (pID[j]!=viewID):
            #             print("ERROR: Product ID mismatch")
            #             break
