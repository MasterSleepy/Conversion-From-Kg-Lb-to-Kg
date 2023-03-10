weight = int(input("Weight: "))
monkey = input("(K)g or (L)bs: ")

if monkey.upper() == "K": 
    print ("Your weight in Kgs is " + str(weight))
elif monkey.upper() == "L":
    print ("Your weight in Kgs is " + str(int((weight * 0.453592))))
else: 
    print ("Sorry, what you have typed is not functional, please retry again.")


