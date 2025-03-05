vGPA = 0

visualArt1 = input("What grade did you receive in the class?")
if visualArt1 == "A+":
    vGPA += 4
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "A":
    vGPA += 4
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "A-":
    vGPA += 4
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "B+":
    vGPA += 3
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "B":
    vGPA += 3
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "B-":
    vGPA += 3
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "C+":
    vGPA += 2
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "C":
    vGPA += 2
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
elif visualArt1 == "C-":
    vGPA += 2
    visualArt1Honors = input("Was this an honors class?")
    if visualArt1Honors == "yes":
        vGPA += 1
    print("You cannot be admitted because your grade is lower than a C in the class.")
elif visualArt1 == "D":
    vGPA += 1
    print("You cannot be admitted because your grade is lower than a C in the class.")
elif visualArt1 == "D-":
    vGPA += 1
    print("You cannot be admitted because your grade is lower than a C in the class.")
elif visualArt1 == "F":
    print("You cannot be admitted because your grade is lower than a C in the class.")