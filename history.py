hGPA = 0

history1 = input("What grade did you receive in the class?")
    if history1 == "A+":
        hGPA += 4
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
    elif history1 == "A":
        hGPA += 4
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
    elif history1 == "B+":
        hGPA += 3
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
    elif history1 == "B":
        hGPA += 3
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
    elif history1 == "B-":
        hGPA += 3
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
    elif history1 == "C":
        hGPA += 2
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
    elif history1 == "C-":
        hGPA += 2
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history1 == "D+":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history1 == "D":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history1 == "D-":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    history2 = input("What grade did you receive in the class?")
    if history2 == "A+":
        hGPA += 4
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "A":
        hGPA += 4
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "A-":
        hGPA += 4
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "B+":
        hGPA += 3
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "B":
        hGPA += 3
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "B-":
        hGPA += 3
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "C+":
        hGPA += 2
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "C":
        hGPA += 2
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
    elif history2 == "C-":
        hGPA += 2
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history2 == "D+":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history2 == "D":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history2 == "D-":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history2 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    combinedHistory = (hGPA / 4)
    print(combinedHistory)