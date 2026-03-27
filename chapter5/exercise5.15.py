print("[Codes: 1, 2, 3, 5, 9]")
print("Type 0, to finish the bought.")
stack = 0
while True:
    priceCalc = 0
    product = int(input("Type the product code: "))
    if product == 1:
        price = 0.50
    elif product == 2:
        price = 1.00
    elif product == 3:
        price = 4.00
    elif product == 5:
        price = 7.00
    elif product == 9:
        price = 8.00
    elif product == 0:
        print(f" Shopping value: {stack:.2f}")
        break
    else:
        print(" Invalid code!")
        break
    count = int(input("How many of this product? "))
    priceCalc = price * count
    stack += priceCalc
