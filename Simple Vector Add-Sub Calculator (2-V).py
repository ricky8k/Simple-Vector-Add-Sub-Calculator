import math

# Simple Vector Addition/Subtraction Calculator
# by ricky8k
ver = "0.0.2"

# R = A +/- B
# 2 Vectors

def main():
    print("Simple Vector Addition/Subtraction Calculator")
    print("\nR = A +/- B")
    print("2 Vectors\n")
    print(ver)
    print("____________________\n")

    # Input vectors for A
    print("Enter vector A in Polar:")
    mesA = float(input(""))
    angA = float(input(""))
    # Input vectors for B
    print("Enter vector B in Polar:")
    mesB = float(input(""))
    angB = float(input(""))
    # Mode selection to tell program what to do with given vectoes (add or subtract)
    print("\nSelect mode:")
    print("Type [+] for Addition")
    print("Type [-] for Subtraction")
    mode = input("")

    print("\n____________________")
    # Addition mode:
    if mode == "+": # Type: +
        # Final input for user to double-check
        print("Input:")
        print("A = " + str(mesA) + " @ " + str(angA)) # e.g. 10 @ 60
        print("B = " + str(mesB) + " @ " + str(angB)) # e.g. 20 @ 40
        print("R = A + B") # Shows the mode selected
    # Subtraction mode:
    elif mode == "-": # Type: -
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
        # Store variables
        cosA = round((math.cos(math.radians(angA))) * mesA,4)
        sinA = round((math.sin(math.radians(angA))) * mesA,4)
        cosB = round((math.cos(math.radians(angB))) * mesB,4)
        sinB = round((math.sin(math.radians(angB))) * mesB,4)
        # Output
        print(str(cosA) + " " + str(sinA))
        print(str(cosB) + " " + str(sinB))
        print("--------------------")
        # Subtract and store
        cosAB = round((cosA + cosB),4)
        sinAB = round((sinA + sinB),4)
        print(str(cosAB) + " " + str(sinAB))
    # Vector subtraction table, looks something like this on paper:
    # Vector          | x = mes cos ang       | y = mes sin ang       |
    # A = mesA @ angA | mesA cos angA         | mesA sin angA         |
    # B = mesB @ angB | mesB cos angB (-)     | mesB sin angB (-)     |
    # R = A - B       | Rx = cos A + -(cos B) | Ry = sin A + -(sin B) |
    elif mode == "-":
        print("\nTable:")
        # Store variables
        cosA = round((math.cos(math.radians(angA))) * mesA,4)
        sinA = round((math.sin(math.radians(angA))) * mesA,4)
        cosB = round((math.cos(math.radians(angB))) * mesB,4)
        sinB = round((math.sin(math.radians(angB))) * mesB,4)
        # Output
        print(str(cosA) + " " + str(sinA))
        print(str(cosB) + " " + str(sinB))
        print("--------------------")
        # Add and store
        cosAB = round((cosA - cosB),4)
        sinAB = round((sinA - sinB),4)
        print(str(cosAB) + " " + str(sinAB))
    else:
        print("",end="")

    # Addition mode:
    if mode == "+":
        # Finding polar form from rectangular
        print("\nWork:")
        # Part A: Get the measure
        # 0) Preview values
        print("R = sqrt(",end="")
        print(str(cosAB) + "^2 + " + (str(sinAB)) + "^2)")
        # 1) Square values
        cosAB = round((cosAB**2),4)
        sinAB = round((sinAB**2),4)
        print("R = sqrt(",end="")
        print(str(cosAB) + " + " + (str(sinAB)) + ")")
        # 2) Add values together
        csAB = round((cosAB + sinAB),4)
        print("R = sqrt(",end="")
        print(str(csAB) + ")")
        # 3) Square root
        csAB = round((math.sqrt(csAB)),4)
        print("R = ",end="")
        print(str(csAB))
        # Part B: Get the angle
        # 0) Preview values
        cosAB = round((cosA + cosB),4)
        sinAB = round((sinA + sinB),4)
        print("Θ = tan-1(",end="")
        print(str(sinAB) + " / " + str(cosAB) + ")")
        # 1) Divide Ry / Rx
        angAB = round((sinAB / cosAB), 4)
        print("Θ = tan-1(",end="")
        print(str(angAB) + ")")
        # 2) Get inverse tan of value
        angAB = round((math.degrees(math.atan(angAB))),4)
        print("Θ = ",end="")
        print(angAB)
    # Subtraction mode:
    elif mode == "-":
        # Finding polar form from rectangular
        print("\nWork:")
        # Part A: Get the measure
        # 0) Preview values
        print("R = sqrt(",end="")
        print(str(cosAB) + "^2 + " + (str(sinAB)) + "^2)")
        # 1) Square values
        cosAB = round((cosAB**2),4)
        sinAB = round((sinAB**2),4)
        print("R = sqrt(",end="")
        print(str(cosAB) + " + " + (str(sinAB)) + ")")
        # 2) Add values together
        csAB = round((cosAB + sinAB),4)
        print("R = sqrt(",end="")
        print(str(csAB) + ")")
        # 3) Square root
        csAB = round((math.sqrt(csAB)),4)
        print("R = ",end="")
        print(str(csAB))
        # Part B: Get the angle
        # 0) Preview values
        cosAB = round((cosA - cosB),4)
        sinAB = round((sinA - sinB),4)
        print("Θ = tan-1(",end="")
        print(str(sinAB) + " / " + str(cosAB) + ")")
        # 1) Divide Ry / Rx
        angAB = round((sinAB / cosAB), 4)
        print("Θ = tan-1(",end="")
        print(str(angAB) + ")")
        # 2) Get inverse tan of value
        angAB = round((math.degrees(math.atan(angAB))),4)
        print("Θ = ",end="")
        print(angAB)
    else:
        print("")

    # Addition/Subtraction mode:
    if mode == "+" or mode == "-":
        print("\n____________________")
        print("Solution:")
        print("--------------------")
        # 1) Solution in Rectangular Form
        print("R = ",end="")
        # Reset stored variables
        if mode == "+":
            cosAB = round((cosA + cosB),4)
            sinAB = round((sinA + sinB),4)
        elif mode == "-":
            cosAB = round((cosA - cosB),4)
            sinAB = round((sinA - sinB),4)
        print(str(cosAB) + "i" + " + " + str(sinAB) + "j")
        # 2) Solution in Polar Form (With conversion)
        print("R = ",end="")
        # R = +0i + 0j | ang = 0
        if cosAB > 0 and sinAB > 0:
            print(str(csAB) + " @ " + str(angAB))
        # R = -0i + 0j | ang = 180 + (-0)
        elif cosAB < 0 and sinAB > 0:
            angAB = 180 + angAB
            print(str(csAB) + " @ " + str(angAB))
        # R = -0i - 0j | ang = 360 + (-0)
        elif cosAB < 0 and sinAB < 0:
            angAB = 360 + angAB
            print(str(csAB) + " @ " + str(angAB))
        # R = +0i - 0j | ang = 180 + 0
        elif cosAB > 0 and sinAB < 0:
            angAB = 180 + angAB
            print(str(csAB) + " @ " + str(angAB))
        # Standard/no conversion value (debugging)
        else:
            print("Unable to convert, no conversion applied:")
            print(str(csAB) + " @ " + str(angAB))
    # Invalid mode
    else: 
        print("Couldn't determine mode. Use [+] or [-] when selecting the mode.")

    print("\nhttps://github.com/ricky8k\n")
    exit = input('Press [Enter] to exit, or type R + [Enter] to restart: ')
    if exit == "R":
        print("\n-\n")
        main()
main()

# Made by ricky8k
# https://github.com/ricky8k

# Updated as of 12/16/2021
# 0.0.2
