sGPA = 0
science1 = input("What grade did you receive in the class?")
    if science1 == "A+":
        sGPA += 4
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "A":
        sGPA += 4
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "A-":
        sGPA += 4
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "B+":
        sGPA += 3
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "B":
        sGPA += 3
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "B-":
        sGPA += 3
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "C+":
        sGPA += 2
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "C":
        sGPA += 2
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
    elif science1 == "C-":
        sGPA += 2
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science1 == "D+":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science1 == "D":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science1 == "D-":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    science2 = input("What grade did you receive in the class?")
    if science2 == "A+":
        sGPA += 4
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "A":
        sGPA += 4
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "A-":
        sGPA += 4
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "B+":
        sGPA += 3
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "B":
        sGPA += 3
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "B-":
        sGPA += 3
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "C+":
        sGPA += 2
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "C":
        sGPA += 2
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
    elif science2 == "C-":
        sGPA += 2
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science2 == "D":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science2 == "D-":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science2 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    science3 = input("What grade did you receive in the class?")
    if science3 == "A+":
        sGPA += 4
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
    elif science3 == "A":
        sGPA += 4
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
    elif science3 == "A-":
        sGPA += 4
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
    elif science3 == "B+":
        sGPA += 3
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
    elif science3 == "B":
        sGPA += 3
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
    elif science3 == "C+":
        sGPA += 2
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
    elif science3 == "C":
        sGPA += 2
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
    elif science3 == "C-":
        sGPA += 2
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science3 == "D":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science3 == "D-":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science3 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    combinedScience = (sGPA / 3)
    print(combinedScience)