#------------------------------------------------
# Libraries and Modules - Formative 1
# Cole Patton
# Oct. 26, 2022
#------------------------------------------------- 
# This program is going to take a few random numbers, and show the sum of them adding, and the sum of them from multiplying

#-------------------Imported Modules are here--------------------

# Already defined modules built into Python
import time
import random

#-------------------My Own Modules---------

# This ADDITION module comes from the library SUMS, in the same file as this main program
from sums import addition

# This MULTIPLYING module comes from the library SUMS, in the same file as this main program
from sums import multiplying

#---------------Variables Defined Here---------------------

# Here I roll each random number I am going to use
num1 = random.randint(1,100)

num2 = random.randint(1,100)

num3 = random.randint(1,100)


#--------------------Main Code-------------------

# Tells the user what numbers they got
print(f"""Your numbers rolled are:
{num1}, {num2}, and {num3}
""")

time.sleep(3)

# Prints the total sum of addtion of the three random numbers
final_sum = addition.add(num1, num2, num3)
print("These numbers added together gives you:", final_sum)

time.sleep(3)

# Prints the total from multiplying each random number together
final_multiplied = multiplying.multiply(num1, num2, num3)
print("These numbers all multiplied together gives you:", final_multiplied)





