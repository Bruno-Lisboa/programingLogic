#car rent, R$60,00 by day and R$0,15 by km
days = int(input("How many day did you spent with the car? "))
km = int(input("How many kilometers did you drive for? "))
payPrice  = (days*60) + (km*0.15)
print(f"This is how much you own the company: R${payPrice:.2f}")
