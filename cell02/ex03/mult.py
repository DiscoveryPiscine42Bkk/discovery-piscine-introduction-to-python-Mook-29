num1 = int(input("enter the first nunber:"))
num2 = int(input("enter the second number:"))
print(f"{num1} x {num2} = {num1 * num2}")
if num1 * num2 > 0:
    print("the result is positive.")
elif num1 * num2 < 0:
    print("the result is negative.")
else:
    print("the result is positive and negative.")