import statistics as stat

grades = [5, 3, 2, 1, 4, 4, 5, 3, 2, 5, 4, 3]
suma = 0
for index in grades:
    suma = index + suma
average_with_for = suma / 12
formatedAverage = format(average_with_for, (".2f"))
print("Average with for loop: ", formatedAverage)

sumFunction = sum(grades)
avgWithSumFunction = sumFunction / 12
formatSumFunction = format(avgWithSumFunction, (".2f"))
print('Average with "sum" function: ', formatSumFunction)

avgWithmean = stat.mean(grades)
formatAvgWithMean = format(avgWithmean, (".2f"))
print("Average with mean fuction: ", formatAvgWithMean)

MedianWithFuction = stat.median(grades)
print('Median with "median" function:', MedianWithFuction)


sizeOfList = len(grades)
grades.sort()  # data needs to be placed in ascending order
if sizeOfList % 2 == 0:
    medianWithoutFunc1 = grades[sizeOfList // 2]
    medianWithoutFunc2 = grades[sizeOfList // 2 - 1]
    median = (medianWithoutFunc1 + medianWithoutFunc2) / 2
else:
    median = (grades)[sizeOfList // 2]

print("Median witout function:", median)

calcMode = stat.multimode(grades)
print("The mode in the list is: ", calcMode)
