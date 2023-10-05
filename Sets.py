from typing import Union

def menu():
    print("[1] Membership")
    print("[2] Add element")
    print("[3] Remove item")
    print("[4] Clear set")
    print("[5] Union")
    print("[6] Intersection")
    print("[7] Difference")


def first_set():
    num_elements = int(input('How many elements would you like to insert for set A: '))
    arrayA = []
    inserting_a =""
    for i in range(num_elements):
        inserting_a=int(input('Insert element:'))
        arrayA.append(inserting_a)
    global set_a
    set_a = set(arrayA)
    print = (set_a)
    return set_a
def second_set():
    first_set()
    num_elements2 = int(input('How many elements would you like to insert for set B: '))
    arrayB = []
    inserting_b = ""
    for i in range(num_elements2):
        inserting_b = int(input('Insert element:'))
        arrayB.append(inserting_b)
    global set_b
    set_b = set(arrayB)
    print = (set_b)
    return set_b


def third_set():
    second_set()
    num_elements3 = int(input('How many elements would you like to insert for set C: '))
    arrayC = []
    inserting_c = ""
    for i in range(num_elements3):
        inserting_c = int(input('Insert element:'))
        arrayC.append(inserting_c)
    global set_c
    set_c = set(arrayC)
    print = (set_c)
    return set_c


def forth_set():
    third_set()
    num_elements4 = int(input('How many elements would you like to insert for set D: '))
    arrayD = []
    inserting_d = ""
    for i in range(num_elements4):
        inserting_d = int(input('Insert element:'))
        arrayD.append(inserting_d)
    global set_d
    set_d = set(arrayD)
    print = (set_d)
    return set_d


def fifth_set():
    forth_set()
    num_elements5= int(input('How many elements would you like to insert for set E: '))
    arrayE = []
    inserting_e = ""
    for i in range(num_elements5):
        inserting_e = int(input('Insert element:'))
        arrayE.append(inserting_e)
    global set_e
    set_e = set(arrayE)
    print = (set_e)
    return set_e

def keepGoing(keep):
    while True:
        if keep == "y":
            sel = int(
                input("How many sets would you like to create? (min 1, max 5 ): ")
            )
            setSelectionFunction(sel)
        if keep == "n":
            print("Good bye!")
        break


def operation(menuOption):
    if menuOption == "1":
        checkMembership = input(
            "In which set would you like to check membership (e.g. A): "
        )
        if checkMembership == "A":
            elementCheck = int(input("Type element you are looking for: "))
            ACheck = elementCheck in set_a
            if ACheck == True:
                print("This element exist in Set A")
            else:
                print("This element does not exist in Set A")

        elif checkMembership == "B":
            elementCheck = input("Type element you are looking for: ")
            ACheck = elementCheck in set_b
            if ACheck == True:
                print("This element exist in Set B")
            else:
                print("This element does not exist in Set B")

        elif checkMembership == "C":
            elementCheck = input("Type element you are looking for: ")
            ACheck = elementCheck in set_c
            if ACheck == True:
                print("This element exist in Set C")
            else:
                print("This element does not exist in Set C")

        elif checkMembership == "D":
            elementCheck = input("Type element you are looking for: ")
            ACheck = elementCheck in set_d
            if ACheck == True:
                print("This element exist in Set D")
            else:
                print("This element does not exist in Set D")

        elif checkMembership == "E":
            elementCheck = input("Type element you are looking for: ")
            ACheck = elementCheck in set_e
            if ACheck == True:
                print("This element exist in Set E")
            else:
                print("This element does not exist in Set E")

    if menuOption == "2":
        setSelection = input("To which set do you want to add element (e.g. A): ")
        if setSelection == "A":
            adding = input("Type element to add: ")
            set_a.add(adding)
            print("Your element has been added!")
            print(f"A: {set_a}")

        if setSelection == "B":
            adding = input("Type element to add: ")
            set_b.add(adding)
            print("Your element has been added!")
            print(f"B: {set_b}")

        if setSelection == "C":
            adding = input("Type element to add: ")
            set_c.add(adding)
            print("Your element has been added!")
            print(f"C: {set_c}")

        if setSelection == "D":
            adding = input("Type element to add: ")
            set_d.add(adding)
            print("Your element has been added!")
            print(f"D: {set_d}")

        if setSelection == "E":
            adding = input("Type element to add: ")
            set_e.add(adding)
            print("Your element has been added!")
            print(f"E: {set_e}")

    if menuOption == "3":
        setSelection = input("From which set do you want to remove element (e.g. A): ")
        if setSelection == "A":
            removing = int(input("Type element to remove: "))
            set_a.remove(removing)
            print("Your element has been removed!")
            print(f"A: {set_a}")

        if setSelection == "B":
            removing = int(input("Type element to remove: "))
            set_b.remove(removing)
            print("Your element has been removed!")
            print(f"B: {set_b}")

        if setSelection == "C":
            removing = int(input("Type element to remove: "))
            set_c.remove(removing)
            print("Your element has been removed!")
            print(f"C: {set_c}")

        if setSelection == "D":
            removing = int(input("Type element to remove: "))
            set_d.remove(removing)
            print("Your element has been removed!")
            print(f"D: {set_d}")

        if setSelection == "E":
            removing = int(input("Type element to remove: "))
            set_e.remove(removing)
            print("Your element has been removed!")
            print(f"E: {set_e}")

    if menuOption == "4":
        clearing = input("Which set would you like to clear (e.g. A): ")
        if clearing == "A":
            set_a.clear()
            print("A: ", set_a)

        elif clearing == "B":
            set_b.clear()
            print("B: ", set_b)

        elif clearing == "C":
            set_c.clear()
            print("C: ", set_c)

        elif clearing == "D":
            set_d.clear()
            print("D: ", set_d)

        elif clearing == "E":
            set_e.clear()
            print("E: ", set_e)

    if menuOption == "5":
        print(
            "You can only perform this opearation if you've created more than one set!"
        )
        print("This are your options. You can unify:")
        print("[1]('A & B')")
        print("[2]('A & B & C')")
        print("[3]('A & B & C & D')")
        print("[4]('A & B & C & D & E')")

        unification = input("Select one: ")
        if unification == "1":
            unity = set_a.union(set_b)
            print("A & B : ", unity)

        if unification == "2":
            unity = set_a.union(set_b, set_c)
            print("A & B & C: ", unity)

        if unification == "3":
            unity = set_a.union(set_b, set_c, set_d)
            print("A & B & C & D: ", unity)

        if unification == "4":
            unity = set_a.union(set_b, set_c, set_d, set_e)
            print("A & B & C & D & E: ", unity)

    if menuOption == "6":
        print(
            "You can only perform this opearation if you've created more than one set!"
        )
        print("This are your options. You can do intersecion of :")
        print("[1]('A ∩ B')")
        print("[2]('A ∩ B ∩ C')")
        print("[3]('A ∩ B ∩ C ∩ D')")
        print("[4]('A ∩ B ∩ C ∩ D ∩ E')")
        intersec = input("Please select one: ")

        if intersec == "1":

            result = set_a.intersection(set_b)
            print("A ∩ B: ", result)

        if intersec == "2":
            result = set_a.intersection(set_b, set_c)
            print("A ∩ B ∩ C: ", result)

        if intersec == "3":
            result = set_a.intersection(set_b, set_c, set_d)
            print("A ∩ B ∩ C ∩ D: ", result)

        if intersec == "4":
            result = set_a.intersection(set_b, set_c, set_dt, set_a)
            print("A ∩ B ∩ C ∩ D ∩ E: ", result)

    if menuOption == "7":
        setDifference = []
        In_A = set(setDifference)
        print(
            "You can only perform this opearation if you've created more than one set!"
        )
        print("This are your options. You can do intersecion of :")
        print("[1]('A - B')")
        print("[2]('C - D')")
        print("[3]('E - A')")
        print("[4]('B - C')")
        print("[5]('D - E')")
        difference = input("Please select one: ")
        if difference == "1":
            for item in set_a:
                if item not in set_b:
                    In_A.add(item)
        print(In_A)

        if difference == "2":
            result = set_c.difference(set_d)
            print(result)

        if difference == "3":
            result = set_e.difference(set_a)
            print(result)

        if difference == "4":
            result = set_b.difference(set_c)
            print(result)

        if difference == "5":
            result = set_d.difference(set_e)
            print(result)


def setSelectionFunction(selection):
    if selection == 1:
        first_set()
        print(set_a)
        menu()
        choice = input("select one operation: ")
        operation(choice)
        cont = input("would you like to continue (y/n): ")
        keepGoing(cont)

    if selection == 2:

        second_set()
        print("Elements in A :", set_a)
        print("Elements in B :", set_b)
        menu()
        choice = input("select one operation: ")
        operation(choice)
        cont = input("would you like to continue (y/n): ")
        keepGoing(cont)

    if selection == 3:

        third_set()
        print("Elements in A :", set_a)
        print("Elements in B :", set_b)
        print("Elements in C :", set_c)
        menu()
        choice = input("select one operation: ")
        operation(choice)
        cont = input("would you like to continue (y/n): ")
        keepGoing(cont)

    if selection == 4:

        forth_set()
        print("Elements in A :", set_a)
        print("Elements in B :", set_b)
        print("Elements in C :", set_c)
        print("Elements in D :", set_d)
        menu()
        choice = input("select one operation: ")
        operation(choice)
        cont = input("would you like to continue (y/n): ")
        keepGoing(cont)

    if selection == 5:

        fifth_set()
        print("Elements in A :", set_a)
        print("Elements in B :", set_b)
        print("Elements in C :", set_c)
        print("Elements in D :", set_d)
        print("Elements in E :", set_e)
        menu()
        choice = input("select one operation: ")
        operation(choice)
        cont = input("would you like to continue (y/n): ")
        keepGoing(cont)


sel = int(input("How many sets would you like to create? (min 1, max 5 ): "))
setSelectionFunction(sel)
