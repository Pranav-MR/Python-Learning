# Bill : Take item prices and print total + GST

item1 = float(input("Enter the price of Item 1 : "))
item2 = float(input("Enter the price of Item 2 : "))
item3 = float(input("Enter the price of Item 3 : "))

billAmt = (item1 + item2 + item3)
totalBill = (billAmt * 1.18)

print("Bill Amount :", billAmt)
print("Total Bill Amount(with GST) :", totalBill)

