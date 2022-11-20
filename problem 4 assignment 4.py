# The main function contains the unit test list and the number list input by the user
# it then calls the functions get_number, average, minimum, maximum and then formats them within two decimal points.
def main():
    number_List = []
    unit_Test = [100, 200, 300, 400]
    print("Unit Test Below:")
    print("Number:", unit_Test)
    print("The average is : %.2f" % average(unit_Test))
    print("The minimum is : %.2f" % minimum(unit_Test))
    print("The maximum is : %.2f" % maximum(unit_Test))
    print("The standard deviation is: %.2f" % deviation(unit_Test))

    get_number(number_List)
    print("The average is : %.2f" % average(number_List))
    print("The minimum is : %.2f" % minimum(number_List))
    print("The maximum is : %.2f" % maximum(number_List))
    print("The standard deviation is: %.2f" % deviation(number_List))
# The get_number function uses a while loop with an if else ladder nested within it
# this makes it to where if done is typed it will end the if else ladder.
# And the casefold is used to make it case insesistive, the else appends the users input.
def get_number(number_List):
    while True:
        userChoice = input("Enter a number: ")
        if userChoice ==  "Done".casefold():
            print("Number:", number_List)
            break
        else:
            number_List.append(int(userChoice))

# This function returns the total and divides it by the length of the number list
def average(number_List):
    total = 0
    for i in number_List:
        total += i
    return (total/len(number_List))
# The min takes the first value input into the list and whichever one is the smallest and is returned as the min value of the list.
def minimum(number_List):
    temp = number_List[0]
    for i in number_List:
        if i < temp:
            temp = i
    return temp
# The max takes the first value input into the list and whichever one is the largest and is returned as the max value of the list.
def maximum(number_List):
    temp = number_List[0]
    for i in number_List:
        if i > temp:
            temp = i
    return temp

def deviation(number_List):
    avg = 0
    variance = 0
    total = 0
    list = []
    avg = average(number_List)
    for i in number_List:
        list.append(i-avg)
    for i in list:
        total += i*i
    variance = total/(len(list))
    return (variance**.5)

main()