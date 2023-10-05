import statistics as stat

name = " "
student_name = []
gradeList = []

while True:
    name = input("Type name of the student: ")
    student_name.append(name)
    if name != "out":
        grade = int(input("Type grade: "))
        gradeList.append(grade)

        # operations
        average = stat.mean(gradeList)
        med = stat.median(gradeList)
        maxi = max(gradeList)
        mini = min(gradeList)
    else:
        student_name.remove("out")
        final = dict(zip(student_name, gradeList))
        for key, value in final.items():  # to print values next to each other
            print("{}:{}".format(key, value))
        break


operations = [("Average: ", average), ("Median:", med), ("Max: ", maxi), ("Min: ", mini)]
print(operations)
