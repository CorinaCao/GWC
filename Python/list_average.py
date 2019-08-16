list = [2, 5, 6, 3, 8, 12, 1,9]

def greater_than(list):
    for numbers in list:


        if numbers >=5:
            print(numbers)
            continue

        else:
            list2.append(numbers)
            print(list2)

sum = 0
for number in greater_than(list):
    sum += number
print("The sum is %d" %(sum))
average = sum/len(numbers)
print("The average number is: %d" %(average))
