house = float(input("How much is the house price? "))
salary = float(input("How much do you earn? "))
years = int(input("How many years will you pay for the house? "))
prestação = house/(years * 12)

if prestação > salary * 0.3:
    print("We can't proced with your bought!")
else:
    print(f"Congratulation. You are able to buy the house!\nYou will pay R${prestação:.2f} for {years * 12} months.")
