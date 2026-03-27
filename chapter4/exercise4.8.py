# Rewrite the program 4.4 using else

# program 4.4 rewritten

plan = input("What is your cellphone plan? ")

if plan == "talkfew":
    minutsOnPlan = 100
    extra = 0.20
    price = 50
else:
    minutsOnPlan = 500
    extra = 0.15
    price = 99

if plan != "talkfew" and plan != "talktoomuch":
    print(f"The {plan} does not exist!")
