elGPA = 0

elective1 = input("What grade did you receive in the class?")
    if elective1 == "A+":
        elGPA += 4
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "A":
        elGPA += 4
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "A-":
        elGPA += 4
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "B+":
        elGPA += 3
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "B":
        elGPA += 3
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "B-":
        elGPA += 3
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "C+":
        elGPA += 2
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "C":
        elGPA += 2
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
    elif elective1 == "C-":
        elGPA += 2
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            elGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif elective1 == "D+":
        elGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif elective1 == "D":
        elGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif elective1 == "D-":
        elGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif elective1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")