kmDistance = int(input("What is the distance that you want to run? "))

if kmDistance <= 200:
    ticket = kmDistance * 0.50
    print(f"Ticket price: R${ticket:.2f}")
else:
    ticket = kmDistance * 0.45
    print(f"Ticket price: R${ticket:.2f}")

