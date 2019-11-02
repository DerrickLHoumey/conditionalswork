'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
grade = 66
if (grade > 65):
    print("student is passing")
'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
grade = 66
if (grade >= 65):
    print("student is passing")
else:
    print("student is failing")
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
age = 18
if (age >=18):
    print("can vote")
else:
    print("can't vote")
'''
#4)Create a variable called weight. Make an if statement that checks the unit of the weight. If the weight is in kilograms, convert it to pounds 
'''
weight = 3
if (type (weight) == int):
    print(weight/2.454)
'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
weight 
if (type (weight) == int):
    print(weight/0.454)
else:
    print(weight*2.454)
'''
#6)create a list (seat1 = 1, seat2 = 1, seat3 = 0, seat4 = 1), Now make an if elseif, else statement that checks if a seat is open. if the seat = 1 its closed and print that it's closed. If the seat = 0, it's open and print that it's open. If no seats are open print "There are no available seats"
''' 
seats = [1,1,0,1]
if (seats[0:3] == 1):
    print("There are no available seats")
elif (seats[0:3] == 0):
    print("There are available seats")
elif (seats[0] == 0):
    print("Seat 1 is open")
elif (seats[1] == 0):
    print("Seat 2 is open")
elif (seats[2] == 0):
    print("Seat 3 is open")
elif (seats[3] == 0):
    print("Seat 4 is open")    


    



