#Assignment 4



# Question 1

#Program to solve the problem of tower of Hanoi

def Tower_hanoi(l , fro , mid, to):
	if l == 0:
		return
	Tower_hanoi(l-1, fro, mid, to)
	print("Move Disk ",l," from rod ",fro," to rod ",to)
	Tower_hanoi(l-1, mid, to, fro)

l = 3
Tower_hanoi(l, 'A', 'C', 'B')

#End of Program 1



# Question 2

# Program to print the Pascal's triangle for n number of rows given by user

from math import factorial, remainder
from tracemalloc import start
n = int(input("Enter the size of Pascal's triangle: "))

# Using Recursions

def pascal_triangle(n,length = n):
    if n == 0:
        return
    pascal_triangle(n-1,length)
    print('  '*(length-n), end='')
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i
    print()
pascal_triangle(n)


# Using Iterations

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")
	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	print()

#End of Program 2




# Question 3

#Program 

I1 = int(input("Enter the First Integer: "))
I2 = int(input("Enter the Second Integer: "))
#Quotient
Q = I1//I2
#Remainder
R = I1%I2

print("Quotient :", Q)
print("Remainder :", R)

#part-a

print(callable(Q))
print(callable(R))

#part-b

if (Q == 0):
    print("Quotient is zero")
if (R == 0):
    print("Reminder is zero")
if (Q != 0 and R != 0):
    print("All the values are non zero")
    
#part-c
        
list_1 = [Q + 4, R + 4, R + 5, Q + 5, R + 5, Q + 6, R + 6]
result = []
for i in range(len(list_1)):
    if list_1[i] > 4:
        result.append(list_1[i])

print(f"Filtered out values:{result}")

#part-d

set_result= set(result)
print("Set:", set_result)

#part-e

immutable_set = frozenset(set_result) 
print("Immutable set:",immutable_set)

#part-f

print("Hash value of the max value of set:", hash(max(immutable_set)))


#End of Program 3



#Question 4

#Program to create a class named Student

class Student:
  def __init__(self, name, roll_number):
    self.name = name
    self.roll_number = roll_number
  def __del__(self):
      print("Object destroyed.")
    
Stud_1 = Student("Kumar Rishi", 21104088)
print("Object created.")
print(f"The Name of the student is {Stud_1.name} and SID is {Stud_1.roll_number}.")
del Stud_1


#End of Program 4



#Question 5

#Program to store deatils of three employees

#Emp_Det stands for Employee Details
class Emp_Det:
        count=0
        def __init__(self, employee, name, salary):
            self.employee=employee
            self.name=name
            self.salary=salary
            
        
        def Details(self):
            print("Employee:", self.employee, ", Name:", self.name, ", Salary:", self.salary)

Emp1 = Emp_Det("1", "Mehak", "40000")
Emp2 = Emp_Det("2", "Ashok", "50000")
Emp3 = Emp_Det("3", "Viren", "60000")

#part-a
Emp1.salary = 70000
print(f"The updated salary of {Emp1.name} is {Emp1.salary} ")

#part-b
print("Record of Viren deleted", end='')
del Emp3

#End of Program 5


#Question 6

#Program

word_1 = input("Enter a word: ")
word_1 = word_1.lower()

word_2 = input("Enter a new word using the exact same letters: ")
word_2 = word_2.lower()

def dict_count(word):
    count = {}
    list_1 = list(word)
    l = len(list_1)
    for i in range(l):
        if list_1[i] in count:
            count[list_1[i]] += 1
        else:
            count[list_1[i]] = 1
    return count
def userinput():
    if dict_count(word_1) != dict_count(word_2):
        print("Friendship is fake.")
        return
    reply = input("Is it a meaningful word? (Y or N): ")
    if reply == 'Y':
        print("Friendship test passed.")
    elif reply == 'N':
        print("Friendship is fake.")
    else:
        print("Invalid input.")
        userinput()
userinput()

#End of Program 6







