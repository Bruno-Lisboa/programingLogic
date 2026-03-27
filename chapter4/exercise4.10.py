N1 = int(input(" Choose a number: "))
sign = input(" Now a sign: (+)(-)(*)(/): ")
N2 = int(input(" Choose another number: "))

if sign == "+":
    print(f"Result: {N1 + N2}")
elif sign == "-":
    print(f"Result: {N1 - N2}")
elif sign == "*":
    print(f"Result: {N1 * N2}")
elif sign == "/":
    print(f"Result: {N1 / N2}")
else:
    print(f"Error: {sign} is not supported!")
