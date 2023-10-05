# print("Those are the elements of your sets: ", "Set A = ", A, "\t", "Set B = ", B)
# print(A.union(B))
# Lists
A = []
B = []
C = []
D = []
E = []
selection = 0
selection = int(input("How many sets would you like to create? (min 1, max 5 ): "))
while selection > 0 and selection <= 5:
    if selection == 1:
        element_A = input("insert element for 'A': ")
        A = [element_A]
        A_set = set(A)
        print("Elements in A: ", A_set)
        operations = input("would you like to continue (y/n): ")
        if operations == "y":
            selection = int(
                input("How many sets would you like to create? (min 1, max 5 ): ")
            )
        if operations == "n":
            print("Good bye!")
            break
    elif selection == 2:

        element_A = input("insert element for 'A': ")
        A = set(element_A)
        element_B = input("insert element for 'B' set: ")
        B = set(element_B)
        print("Elements in A: ", A)
        print("Elements in B: ", B)
        operations = input("would you like to continue (y/n): ")
        if operations == "y":
            selection = int(
                input("How many sets would you like to create? (min 1, max 5 ): ")
            )
        if operations == "n":
            print("Good bye!")
            break

    elif selection == 3:
        element_A = input("insert element for 'A': ")
        A = set(element_A)
        element_B = input("insert element for 'B' set: ")
        B = set(element_B)
        element_C = input("insert element for 'C' set: ")
        C = set(element_C)
        print("Elements in A: ", A)
        print("Elements in B: ", B)
        print("Elements in C: ", C)
        operations = input("would you like to continue (y/n): ")
        if operations == "y":
            selection = int(
                input("How many sets would you like to create? (min 1, max 5 ): ")
            )
        if operations == "n":
            print("Good bye!")
            break

    elif selection == 4:
        element_A = input("insert element for 'A': ")
        A = set(element_A)
        element_B = input("insert element for 'B' set: ")
        B = set(element_B)
        element_C = input("insert element for 'C' set: ")
        C = set(element_C)
        element_D = input("insert element for 'D' set: ")
        D = set(element_D)
        print("Elements in A: ", A)
        print("Elements in B: ", B)
        print("Elements in C: ", C)
        print("Elements in D: ", D)
        operations = input("would you like to continue (y/n): ")
        if operations == "y":
            selection = int(
                input("How many sets would you like to create? (min 1, max 5 ): ")
            )
        if operations == "n":
            print("Good bye!")
            break

    elif selection == 5:
        element_A = input("insert element for 'A': ")
        A = set(element_A)
        element_B = input("insert element for 'B' set: ")
        B = set(element_B)
        element_C = input("insert element for 'C' set: ")
        C = set(element_C)
        element_D = input("insert element for 'D' set: ")
        D = set(element_D)
        element_E = input("insert element for 'E' set: ")
        E = set(element_E)
        print("Elements in A: ", A)
        print("Elements in B: ", B)
        print("Elements in C: ", C)
        print("Elements in D: ", D)
        print("Elements in E: ", E)
        operations = input("would you like to continue (y/n): ")
        if operations == "y":
            selection = int(
                input("How many sets would you like to create? (min 1, max 5 ): ")
            )
        if operations == "n":
            print("Good bye!")
            break
    else:
        break