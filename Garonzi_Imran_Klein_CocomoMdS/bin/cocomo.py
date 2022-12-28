from os.path import exists
import cost_drivers

def BasicCocomo(dif):
    # Initialize the variables
    simpleLOC = [2.4, 1.05, 2.5, 0.38]
    intermediateLOC = [3, 1.12, 2.5, 0.35]
    complexLOC = [3.6, 1.12, 2.5, 0.32]

    # Assign value to variables
    if (dif == 1):
        difficolta = "simple" # Difficulty
        a = simpleLOC[0] # Number of rows in thousands of rows
        b = simpleLOC[1] # Economies of scale
        c = simpleLOC[2] # Value that takes into account the difficulty of the program
        d = simpleLOC[3] # Value that takes into account the difficulty of the program
    elif (dif == 2):
        difficolta = "intermediate"
        a = intermediateLOC[0]
        b = intermediateLOC[1]
        c = intermediateLOC[2]
        d = intermediateLOC[3]
    else:
        difficolta = "complex"
        a = complexLOC[0]
        b = complexLOC[1]
        c = complexLOC[2]
        d = complexLOC[3]

    # Calculate man months and development time
    manMonths = a * ((LOC / 1000)**b)
    developmentTime = c * (manMonths ** d)

    # Write the output file
    write(difficolta, developmentTime, manMonths)

def IntermediateCocomo(dif):
    # Initialize the variables
    simpleLOC = [3.2, 1.05, 2.5, 0.38]
    intermediateLOC = [3, 1.12, 2.5, 0.35]
    complexLOC = [2.8, 1.2, 2.5, 0.32]

    # Assign value to variables
    if (dif == 1):
        difficolta = "simple" # Difficulty
        a = simpleLOC[0] # Number of rows in thousands of rows
        b = simpleLOC[1] # Economies of scale
        c = simpleLOC[2] # Value that takes into account the difficulty of the program
        d = simpleLOC[3] # Value that takes into account the difficulty of the program
    elif (dif == 2):
        difficolta = "intermediate"
        a = intermediateLOC[0]
        b = intermediateLOC[1]
        c = intermediateLOC[2]
        d = intermediateLOC[3]
    else:
        difficolta = "complex"
        a = complexLOC[0]
        b = complexLOC[1]
        c = complexLOC[2]
        d = complexLOC[3]

    # Choice of cost driver
    keylist = cost_drivers.costDriver1.keys()
    print()
    for key in keylist:
        print(key)

    costD_choice = input("Enter the name of the Cost Driver: ")
    while (costD_choice not in cost_drivers.costDriver1):
        costD_choice = input("\Error! Invalid name. Re-enter Cost Driver: ")

    # Ask the difficulty
    dif = 0
    print("\nChoose from the following values:\n\n"
        "Very low = 1" + "\n"
        "Low = 2" + "\n"
        "Nominal = 3" + "\n"
        "High = 4" + "\n"
        "Very high = 5" + "\n"
        "Extra high = 6" + "\n")
    dif = int(input("Enter a value between 1 and 6: "))
    while (dif < 1 or dif > 6):
        dif = int(input("\nError! Re-enter a value between 1 and 6: "))

    costDriver = cost_drivers.assignCostDriver(dif)

    # Calculate man months and development time
    if (costDriver[costD_choice] == 0):
        manMonths = a * ((LOC / 1000) ** b)
    else:
        manMonths = a * ((LOC / 1000) ** b) * (costDriver[costD_choice] * 15)
    
    developmentTime = c * (manMonths ** d)

    # Write the output file
    write(difficolta, developmentTime, manMonths)

def write(difficolta, developmentTime, manMonths):
    # Open the file for writing
    outputFile = open("Result.txt", "w")
    outputFile.write("Results of the file '" + filepath +"'\n\n")

    # Write the output file
    if mode == 0:
        cocomo = "Basic"
    else:
        cocomo = "Intermediate"
    write = "Number of lines of code = " + str(LOC) + "\n" + "Difficulty = " + str(difficolta) + "\n" + "Months man = " + str(round(manMonths, 2)) + "\n" + "Development time = " + str(round(developmentTime, 2)) + "\n"
    outputFile.write(cocomo + " Cocomo" + ":" + "\n" + write)
    outputFile.close() #Close the file for writing

def cocomoStart(fp):
    # Get the filepath
    global filepath
    global content
    
    # Open the file for reading
    filepath = fp
    file = open(filepath, 'r')
    content = file.readlines()
    file.close() # Close the file for reading
    
    # Choice of mode
    print("\nChoose from the following modes: "+ "\n\n"
        "0 = Basic Cocomo" + "\n"
        "1 = Intermediate Cocomo" + "\n")
    
    global mode
    mode = int(input("Enter the mode between 0 and 1: "))
    while (mode < 0 or mode > 1):
        mode = int(input("\nError! Re-enter a value between 0 and 1: "))

    # Counting the number of lines in the file
    global LOC
    LOC = 0
    for line in content:
        LOC += 1

    # Ask the difficulty of the file
    print("\nChoose from the following difficulties\n\n1 = simple\n2 = intermediate \n3 = complex\n")
    dif = int(input("Enter the difficulty of the program between 1 and 3: "))

    while(dif < 1 or dif > 3):
        dif = int(input("\nError! Re-enter the difficulty of the program between 1 and 3: "))
    
    # Call the Cocomo function
    if mode == 0:
        BasicCocomo(dif)
    elif mode == 1:
        IntermediateCocomo(dif) 

    print("\nWriting complete")
