#To find hypotenuse

import math
a = int(input("please enter a:"))
b = int(input("please enter b:"))
c = math.sqrt(pow(a, a) + pow(b, b))
print (f"The hypotenuse is: {round(c, 2)}units")