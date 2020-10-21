num = 0
Tot = 0

while True:
    IntValue = input("Enter a number: ")
    if IntValue == "done":
        break
    try:
      FloatValue = float(IntValue)
    except:
        print("Invalid Input")
        continue
    num = num + 1
    Tot = Tot + FloatValue
print("All done")
print("Here are you stats")
print("Total: ", Tot, "Final Number: ",  num, "Average: ", Tot/num)
