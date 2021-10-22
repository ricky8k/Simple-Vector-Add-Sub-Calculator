import math

# Simple Vector Addition/Subtraction Calculator
# by ricky8k

# R = A +/- B
# 2 Vectors

print("Simple Vector Addition/Subtraction Calculator")
print("\nR = A +/- B")
print("2 Vectors")
print("____________________\n")

# Input vectors for A
print("Enter vector A in Polar:")
mesA = float(input(""))
angA = float(input(""))
# Input vectors for B
print("Enter vector B in Polar:")
mesB = float(input(""))
angB = float(input(""))
# Mode selection to tell program what to do with given vectors (add or subtract)
print("\nSelect mode:")
print("Type [+] for Addition")
print("Type [-] for Subtraction")
mode = input("")

# Addition mode:
if mode == "+": # Type: +
    print("\n____________________")
    # Final input for user to double-check
    print("Input:")
    print("A = " + str(mesA) + " @ " + str(angA)) # e.g. 10 @ 60
    print("B = " + str(mesB) + " @ " + str(angB)) # e.g. 20 @ 40
    print("R = A + B") # Shows the mode selected
# Subtraction mode:
elif mode == "-": # Type: -
    print("\n____________________")
    # Final input for user to double-check
    print("Input:")
    print("A = " + str(mesA) + " @ " + str(angA)) # e.g. 10 @ 60
    print("B = " + str(mesB) + " @ " + str(angB)) # e.g. 20 @ 40
    print("R = A - B") # Shows the mode selected
# Error message if user inputs the incorrect mode
# Repeats 3 times, in-case the user mistypes [+] or [-]
else:
    mode = input("Invalid mode! Please try again: ")

if mode == "+":
    print("",end="")
elif mode == "-":
    print("",end="")
else:
    mode = input("Invalid mode! Please try again: ")

if mode == "+":
    print("",end="")
elif mode == "-":
    print("",end="")
else:
    mode = input("Invalid mode! Please try again: ")

# Vector addition table, looks something like this on paper:
# Vector          | x = mes cos ang    | y = mes sin ang    |
# A = mesA @ angA | mesA cos angA      | mesA sin angA      |
# B = mesB @ angB | mesB cos angB      | mesB sin angB      |
# R = A + B       | Rx = cos A + cos B | Ry = sin A + sin B |
if mode == "+":
    print("\nTable:")
    print(str(round((math.cos(math.radians(angA))) * mesA,4)) + " " + str(round((math.sin(math.radians(angA))) * mesA,4)))
    print(str(round((math.cos(math.radians(angB))) * mesB,4)) + " " + str(round((math.sin(math.radians(angB))) * mesB,4)))
    print("--------------------")
    print(str(round((math.cos(math.radians(angA))) * mesA,4) + round(math.cos(math.radians(angB)) * mesB,4)), end=" ")
    print(str(round((math.sin(math.radians(angA))) * mesA,4) + round(math.sin(math.radians(angB)) * mesB,4)))
# Vector subtraction table, looks something like this on paper:
# Vector          | x = mes cos ang       | y = mes sin ang       |
# A = mesA @ angA | mesA cos angA         | mesA sin angA         |
# B = mesB @ angB | mesB cos angB (-)     | mesB sin angB (-)     |
# R = A - B       | Rx = cos A + -(cos B) | Ry = sin A + -(sin B) |
elif mode == "-":
    print("\nTable:")
    print(str(round((math.cos(math.radians(angA))) * mesA,4)) + " " + str(round((math.sin(math.radians(angA))) * mesA,4)))
    print(str(round((math.cos(math.radians(angB))) * mesB,4)) + " " + str(round((math.sin(math.radians(angB))) * mesB,4)))
    print("--------------------")
    print(str(round((math.cos(math.radians(angA))) * mesA,4) - round(math.cos(math.radians(angB)) * mesB,4)), end=" ")
    print(str(round((math.sin(math.radians(angA))) * mesA,4) - round(math.sin(math.radians(angB)) * mesB,4)))
else:
    print("",end="")

# Addition mode:
if mode == "+":
    # Finding polar form from rectangular
    print("\nWork:")
    # Part A: Get the measure
    # 0) Preview values
    print("R = sqrt(",end="")
    print(str(round(((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB),4)), end="^2 + ")
    print(str(round(((math.sin(math.radians(angA))) * mesA + math.sin(math.radians(angB)) * mesB),4)) + "^2)")
    # 1) Square values
    print("R = sqrt(",end="")
    print(str(round((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2),4)), end=" + ")
    print(str(round((((math.sin(math.radians(angA))) * mesA + math.sin(math.radians(angB)) * mesB)**2),4)) + ")")
    # 2) Add values together
    print("R = sqrt(",end="")
    print(str(round((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA + math.sin(math.radians(angB)) * mesB)**2,4)) + ")")
    # 3) Square root
    print("R = ",end="")
    print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA + math.sin(math.radians(angB)) * mesB)**2),4)))
    # Part B: Get the angle
    # 0) Preview values
    print("Θ = tan-1(",end="")
    print(str(round((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)),4)),end=" / ")
    print(str(round((((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB)),4)) + ")")
    # 1) Divide Ry / Rx
    print("Θ = tan-1(",end="")
    print(str(round((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB)),4)) + ")")
    # 2) Get inverse tan of value
    print("Θ = ",end="")
    print(str(round(math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB)))),4)))
# Subtraction mode:
elif mode == "-":
    # Finding polar form from rectangular
    print("\nWork:")
    # Part A: Get the measure
    # 0) Preview values
    print("R = sqrt(",end="")
    print(str(round(((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB),4)), end="^2 + ")
    print(str(round(((math.sin(math.radians(angA))) * mesA - math.sin(math.radians(angB)) * mesB),4)) + "^2)")
    # 1) Square values
    print("R = sqrt(",end="")
    print(str(round((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2),4)), end=" + ")
    print(str(round((((math.sin(math.radians(angA))) * mesA - math.sin(math.radians(angB)) * mesB)**2),4)) + ")")
    # 2) Add values together
    print("R = sqrt(",end="")
    print(str(round((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA - math.sin(math.radians(angB)) * mesB)**2,4)) + ")")
    # 3) Square root
    print("R = ",end="")
    print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA - math.sin(math.radians(angB)) * mesB)**2),4)))
    # Part B: Get the angle
    # 0) Preview values
    print("Θ = tan-1(",end="")
    print(str(round((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)),4)),end=" / ")
    print(str(round((((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB)),4)) + ")")
    # 1) Divide Ry / Rx
    print("Θ = tan-1(",end="")
    print(str(round((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB)),4)) + ")")
    # 2) Get inverse tan of value
    print("Θ = ",end="")
    print(str(round(math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB)))),4)))
else:
    print("")

# Addition mode:
if mode == "+":
    print("\n____________________")
    print("Solution:")
    print("--------------------")
    # Solution in Rectangular Form
    print("R = ",end="")
    print(str(round((math.cos(math.radians(angA))) * mesA,4) + round(math.cos(math.radians(angB)) * mesB,4)) + "i",end=" + ")
    print(str(round((math.sin(math.radians(angA))) * mesA,4) + round(math.sin(math.radians(angB)) * mesB,4)) + "j")
    # Solution in Polar Form (With conversion)
    print("R = ",end="")
    # R = +0i + 0j | ang = 0
    if round((math.cos(math.radians(angA))) * mesA,4) + round(math.cos(math.radians(angB)) * mesB,4) > 0 and round((math.sin(math.radians(angA))) * mesA,4) + round(math.sin(math.radians(angB)) * mesB,4) > 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA + math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round(math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB)))),4)))
    # R = -0i + 0j | ang = 180 + (-0)
    elif round((math.cos(math.radians(angA))) * mesA,4) + round(math.cos(math.radians(angB)) * mesB,4) < 0 and round((math.sin(math.radians(angA))) * mesA,4) + round(math.sin(math.radians(angB)) * mesB,4) > 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA + math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round((math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB))))) + 180,4)))
    # R = -0i - 0j | ang = 360 + (-0)
    elif round((math.cos(math.radians(angA))) * mesA,4) + round(math.cos(math.radians(angB)) * mesB,4) < 0 and round((math.sin(math.radians(angA))) * mesA,4) + round(math.sin(math.radians(angB)) * mesB,4) < 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA + math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round((math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB))))) + 360,4)))
    # R = +0i - 0j | ang = 180 + 0
    elif round((math.cos(math.radians(angA))) * mesA,4) + round(math.cos(math.radians(angB)) * mesB,4) > 0 and round((math.sin(math.radians(angA))) * mesA,4) + round(math.sin(math.radians(angB)) * mesB,4) < 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA + math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round((math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB))))) + 180,4)))
    # Standard/no conversion value, if somehow the program is unable to use conversions above (which is 100% impossible)
    else:
        print("Unable to convert, answer may need to be manually converted (no conversion applied):")
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA + math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA + math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round(math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) + (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) + (math.cos(math.radians(angB)) * mesB)))),4)))
# Subtraction mode:
elif mode == "-":
    print("\n____________________")
    print("Solution:")
    print("--------------------")
    # Solution in Rectangular Form
    print("R = ",end="")
    print(str(round((math.cos(math.radians(angA))) * mesA,4) - round(math.cos(math.radians(angB)) * mesB,4)) + "i",end=" + ")
    print(str(round((math.sin(math.radians(angA))) * mesA,4) - round(math.sin(math.radians(angB)) * mesB,4)) + "j")
    # Solution in Polar Form (With conversion)
    print("R = ",end="")
    # R = +0i + 0j | ang = 0
    if round((math.cos(math.radians(angA))) * mesA,4) - round(math.cos(math.radians(angB)) * mesB,4) > 0 and round((math.sin(math.radians(angA))) * mesA,4) - round(math.sin(math.radians(angB)) * mesB,4) > 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA - math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round(math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB)))),4)))
    # R = -0i + 0j | ang = 180 + (-0)
    elif round((math.cos(math.radians(angA))) * mesA,4) - round(math.cos(math.radians(angB)) * mesB,4) < 0 and round((math.sin(math.radians(angA))) * mesA,4) - round(math.sin(math.radians(angB)) * mesB,4) > 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA - math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round((math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB))))) + 180,4)))
    # R = -0i - 0j | ang = 360 + (-0)
    elif round((math.cos(math.radians(angA))) * mesA,4) - round(math.cos(math.radians(angB)) * mesB,4) < 0 and round((math.sin(math.radians(angA))) * mesA,4) - round(math.sin(math.radians(angB)) * mesB,4) < 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA - math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round((math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB))))) + 360,4)))
    # R = +0i - 0j | ang = 180 + 0
    elif round((math.cos(math.radians(angA))) * mesA,4) - round(math.cos(math.radians(angB)) * mesB,4) > 0 and round((math.sin(math.radians(angA))) * mesA,4) - round(math.sin(math.radians(angB)) * mesB,4) < 0:
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA - math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round((math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB))))) + 180,4)))
    # Standard/no conversion value, if somehow the program is unable to use conversions above (which is 100% impossible)
    else:
        print("Unable to convert, answer may need to be manually converted (no conversion applied):")
        print(str(round(math.sqrt((((math.cos(math.radians(angA))) * mesA - math.cos(math.radians(angB)) * mesB)**2) + (math.sin(math.radians(angA)) * mesA - math.sin(math.radians(angB)) * mesB)**2),4)),end=" @ ")
        print(str(round(math.degrees(math.atan((((math.sin(math.radians(angA))) * mesA) - (math.sin(math.radians(angB)) * mesB)) / (((math.cos(math.radians(angA))) * mesA) - (math.cos(math.radians(angB)) * mesB)))),4)))
# Error message if user inputs the incorrect mode
else: 
    print("Couldn't determine mode. Please use [+] or [-] when selecting your mode.")

print("\nhttps://github.com/ricky8k\n")
input('Press [Enter] to exit')
# Made by ricky8k
# https://github.com/ricky8k

# Updated as of 10/22/2021