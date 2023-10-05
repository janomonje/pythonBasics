name = str(input("Insert name: "))
sex = int(input("Insert gender (0 = male), (1 = female): "))
grades = []
lengthList = 6
total = 0

for i in range(lengthList):
    score = int(input("Insert every score followed by the enter key: "))
    grades.append(score)

suma = grades[0] + grades[1] + grades[2] + grades[3] + grades[4] + grades[5]
subtraction = grades[0] - grades[1] - grades[2] - grades[3] - grades[4] - grades[5]
average = suma / 6
formatedAverage = format(average, (".2f"))
print("The addition of all your grades is: ", suma)
print("the subtraction of all your grades is: ", subtraction)
print("Your course average is: ", formatedAverage)

if sex == 0:
    print("Hi Mr ", name)
else:
    print("Hi Mrs ", name)
if average > 1:
    print(
        "Your average meets the minimun required to pass this course, congratulations!"
    )
else:
    print("You have failed this course, I'm sorry.")