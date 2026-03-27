#The last exercise of chapter 3.
cigarrets= int(input("How many cigarrets do you smoke by day? "))
yearsSmoking = float(input("How many years did you smoke for? "))
lifeCost = yearsSmoking * 365 * cigarrets * 10
lifeCost = lifeCost / (24 * 60)
print(f"You lost {lifeCost:.0f} days of your life.")

#I'm not pround of this code. I hate it.
