import math

# Simple Vector Addition/Subtraction Calculator
# by ricky8k
ver = "0.0.2"

# R = A +/- B
# 2 Vectors

def main():
    print("Simple Vector Addition/Subtraction Calculator")
    print("\nR = A + B + C")
    print("3 Vectors\n")
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
    # Input vectors for C
    print("Enter vector C in Polar:")
    mesC = float(input(""))
    angC = float(input(""))
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
        print("C = " + str(mesC) + " @ " + str(angC)) # e.g. 30 @ 20
        print("R = A + B + C") # Shows the mode selected
    # Subtraction mode:
    elif mode == "-": # Type: -
        # Final input for user to double-check
        print("Input:")
        print("A = " + str(mesA) + " @ " + str(angA)) # e.g. 10 @ 60
        print("B = " + str(mesB) + " @ " + str(angB)) # e.g. 20 @ 40
        print("C = " + str(mesC) + " @ " + str(angC)) # e.g. 30 @ 20 
        print("R = A - B - C") # Shows the mode selected
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
    # Vector          | x = mes cos ang            | y = mes sin ang            |
    # A = mesA @ angA | mesA cos angA              | mesA sin angA              |
    # B = mesB @ angB | mesB cos angB              | mesB sin angB              |
    # C = mesC @ angC | mesC cos angC              | mesC sin angC              |
    # R = A + B + C   | Rx = cos A + cos B + cos C | Ry = sin A + sin B + sin C |
    if mode == "+":
        print("\nTable:")
        # Store variables
        cosA = round((math.cos(math.radians(angA))) * mesA,4)
        sinA = round((math.sin(math.radians(angA))) * mesA,4)
        cosB = round((math.cos(math.radians(angB))) * mesB,4)
        sinB = round((math.sin(math.radians(angB))) * mesB,4)
        cosC = round((math.cos(math.radians(angC))) * mesC,4)
        sinC = round((math.sin(math.radians(angC))) * mesC,4)
        # Output
        print(str(cosA) + " " + str(sinA))
        print(str(cosB) + " " + str(sinB))
        print(str(cosC) + " " + str(sinC))
        print("--------------------")
        # Add and store
        cosABC = round((cosA + cosB + cosC),4)
        sinABC = round((sinA + sinB + sinC),4)
        print(str(cosABC) + " " + str(sinABC))
    # Vector subtraction table, looks something like this on paper: 
    # Vector          | x = mes cos ang                  | y = mes sin ang                  |
    # A = mesA @ angA | mesA cos angA                    | mesA sin angA                    |
    # B = mesB @ angB | mesB cos angB (-)                | mesB sin angB (-)                |
    # C = mesC @ angC | mesC cos angC (-)                | mesC sin angC (-)                |
    # R = A - B       | Rx = cos A + -(cos B) + -(cos C) | Ry = sin A + -(sin B) + -(sin C) |
    elif mode == "-":
        print("\nTable:")
        # Store variables
        cosA = round((math.cos(math.radians(angA))) * mesA,4)
        sinA = round((math.sin(math.radians(angA))) * mesA,4)
        cosB = round((math.cos(math.radians(angB))) * mesB,4)
        sinB = round((math.sin(math.radians(angB))) * mesB,4)
        cosC = round((math.cos(math.radians(angC))) * mesC,4)
        sinC = round((math.sin(math.radians(angC))) * mesC,4)
        # Output
        print(str(cosA) + " " + str(sinA))
        print(str(cosB) + " " + str(sinB))
        print(str(cosC) + " " + str(sinC))
        print("--------------------")
        # Subtract and store
        cosABC = round((cosA - cosB - cosC),4)
        sinABC = round((sinA - sinB - sinC),4)
        print(str(cosABC) + " " + str(sinABC))
    else:
        print("",end="")

    # Addition mode:
    if mode == "+":
        # Finding polar form from rectangular
        print("\nWork:")
        # Part A: Get the measure
        # 0) Preview values
        print("R = sqrt(",end="")
        print(str(cosABC) + "^2 + " + (str(sinABC)) + "^2)")
        # 1) Square values
        cosABC = round((cosABC**2),4)
        sinABC = round((sinABC**2),4)
        print("R = sqrt(",end="")
        print(str(cosABC) + " + " + (str(sinABC)) + ")")
        # 2) Add values together
        csABC = round((cosABC + sinABC),4)
        print("R = sqrt(",end="")
        print(str(csABC) + ")")
        # 3) Square root
        csABC = round((math.sqrt(csABC)),4)
        print("R = ",end="")
        print(str(csABC))
        # Part B: Get the angle
        # 0) Preview values
        cosABC = round((cosA + cosB + cosC),4)
        sinABC = round((sinA + sinB + sinC),4)
        print("?? = tan-1(",end="")
        print(str(sinABC) + " / " + str(cosABC) + ")")
        # 1) Divide Ry / Rx
        angABC = round((sinABC / cosABC), 4)
        print("?? = tan-1(",end="")
        print(str(angABC) + ")")
        # 2) Get inverse tan of value
        angABC = round((math.degrees(math.atan(angABC))),4)
        print("?? = ",end="")
        print(angABC)
    # Subtraction mode:
    elif mode == "-":
        # Finding polar form from rectangular
        print("\nWork:")
        # Part A: Get the measure
        # 0) Preview values
        print("R = sqrt(",end="")
        print(str(cosABC) + "^2 + " + (str(sinABC)) + "^2)")
        # 1) Square values
        cosABC = round((cosABC**2),4)
        sinABC = round((sinABC**2),4)
        print("R = sqrt(",end="")
        print(str(cosABC) + " + " + (str(sinABC)) + ")")
        # 2) Add values together
        csABC = round((cosABC + sinABC),4)
        print("R = sqrt(",end="")
        print(str(csABC) + ")")
        # 3) Square root
        csABC = round((math.sqrt(csABC)),4)
        print("R = ",end="")
        print(str(csABC))
        # Part B: Get the angle
        # 0) Preview values
        cosABC = round((cosA - cosB - cosC),4)
        sinABC = round((sinA - sinB - sinC),4)
        print("?? = tan-1(",end="")
        print(str(sinABC) + " / " + str(cosABC) + ")")
        # 1) Divide Ry / Rx
        angABC = round((sinABC / cosABC), 4)
        print("?? = tan-1(",end="")
        print(str(angABC) + ")")
        # 2) Get inverse tan of value
        angABC = round((math.degrees(math.atan(angABC))),4)
        print("?? = ",end="")
        print(angABC)
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
            cosABC = round((cosA + cosB + cosC),4)
            sinABC = round((sinA + sinB + cosC),4)
        elif mode == "-":
            cosABC = round((cosA - cosB - cosC),4)
            sinABC = round((sinA - sinB - cosC),4)
        print(str(cosABC) + "i" + " + " + str(sinABC) + "j")
        # 2) Solution in Polar Form (With conversion)
        print("R = ",end="")
        # R = +0i + 0j | ang = 0
        if cosABC > 0 and sinABC > 0:
            print(str(csABC) + " @ " + str(angABC))
        # R = -0i + 0j | ang = 180 + (-0)
        elif cosABC < 0 and sinABC > 0:
            angABC = 180 + angABC
            print(str(csABC) + " @ " + str(angABC))
        # R = -0i - 0j | ang = 360 + (-0)
        elif cosABC < 0 and sinABC < 0:
            angABC = 360 + angABC
            print(str(csABC) + " @ " + str(angABC))
        # R = +0i - 0j | ang = 180 + 0
        elif cosABC > 0 and sinABC < 0:
            angABC = 180 + angABC
            print(str(csABC) + " @ " + str(angABC))
        # Standard/no conversion value (debugging)
        else:
            print("Unable to convert, no conversion applied:")
            print(str(csABC) + " @ " + str(angABC))
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