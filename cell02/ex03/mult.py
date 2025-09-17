fst = int(input("Enter the first number: "))
sec = int(input("Enter the second number: "))
print(f"{fst} x {sec} = {fst*sec}")
if(fst*sec > 0):
    print("The result is positive.")
elif(fst*sec < 0):
    print("The result is negative.")
else:
    print("The result is positive and negative.")