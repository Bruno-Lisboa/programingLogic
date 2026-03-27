area = input("Is the area? R to Residencial, C to comercial or I to industrial. ")
kwh = int(input("How many is the consume of kwh? "))

if area == "R" and kwh <= 500:
    kwhPrice = 0.40
elif area == "R" and kwh > 500:
    kwhPrice = 0.65
elif area == "C" and kwh <= 1000:
    kwhPrice = 0.55
elif area == "C" and kwh > 1000:
    kwhPrice = 0.60
elif area == "I" and kwh <= 5000:
    kwhPrice = 0.55
elif area == "I" and kwh > 5000:
    kwhPrice = 0.60
else:
    print(f"{area} really?")
print(f"kwh price: R${kwhPrice:4.2f}")
