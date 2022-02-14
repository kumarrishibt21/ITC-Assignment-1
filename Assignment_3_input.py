#Assignment 3



#Question 1

# Program to count the number of occurrences of each word or character in the string entered by the user

inp_str=str(input("Enter String: "))

list= inp_str.split()
dict={}

if list.__len__()==1:
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
                dict[i]=1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
    
#End of Program 1



#Question 2

#Program to print next date of input date


year = int(input("Year[1800-2025] - "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_days = 31
elif month == 2:
    if leap_year:
        month_days = 29
    else:
        month_days = 28
else:
    month_days = 30


day = int(input("Input a day [1-31]: "))

if day < month_days:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("Next Date is: %d/%d/%d" % (day,month,year))    

#End of Program 2




#Question 3

#Program to create a list of tuples 

list=[]
elements= int(input("Enter number of elements to be included in the list:"))
for ele in range(0,elements):
    element=int(input("Enter element:"))
    list.append(element)
print(list)
tuples_list=[]
for i in list:
    tuple=(i,i**2)
    tuples_list.append(tuple)
print(tuples_list)

#End of Program 3



#Question 4

#Program to prompt the user for a grade

user=int(input("Enter Grade:"))
if (4<=user<=10):
      
    if user==10:
        print("Your Grade is 'A+' and Outstanding Performance")
    elif user==9:
        print("Your Grade is 'A' and Excellent Performance")
    elif user==8:
        print("Your Grade is 'B+' and Very Good Performance")
    elif user==7:
        print("Your Grade is 'B' and Good Performance")
    elif user==6:
        print("Your Grade is 'C+' and Average Performance")
    elif user==5:
        print("Your Grade is 'C' and Below Average Performance")
    elif user==4:
        print("Your Grade is 'D' and Poor Performance")
else:
    print("Error!")
    
#End of Program 4



#Question 5

#Program to print the given pattern

inp_str="ABCDEFGHIJK"
j=0
while len(inp_str)-j*2 >= 1:
    print(" "*j + inp_str[0:len(inp_str) - j*2])
    j +=1

#End of Program 5
    



#Question 6

#Program that repeatedly ask user to enter name and SID of students

sid = int(input("Enter SID: "))
name = input("Enter Name: ")
stud_details= {sid:name}
while True:
    willingness = input("Do you want to enter name and sid of student(Y or N): ").upper()
    if willingness == 'Y' :
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        stud_details[sid]= name
    elif willingness == 'N':
        break
    else:
        print("Error!")

#part-a
print(stud_details)

#part-b
print({k:v for k,v in sorted(stud_details.items(), key = lambda x:x[1])})

#part-c
print({k:v for k,v in sorted(stud_details.items())})

#part-d
search = int(input("Enter SID of student: "))
print("Name of student with entered SID: ",stud_details[search])

#End of Program 6



#Question 7

#Program to print Fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
num_terms= int(input("Enter number of terms: "))
if (num_terms <=0):
    print("Enter a positive integer!")
else:
    print("Fibonacci sequence: ")
    sum=0
    for i in range(num_terms):
        print(fibonacci(i))
        sum=sum+fibonacci(i)
avg=float(sum/num_terms)
print("Average of the resultant Fibonacci series = ",avg)

#End of Program 7




#Question 8
#Program to write statements to given sets

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#part-a
a= (Set1 | Set2) - (Set1 & Set2)
print(a)

#part-b
b= (Set1 | Set2 | Set3) - (Set1 & Set2 & Set3) - (Set1 & Set2) - (Set2 & Set3)-(Set3 & Set1)
print(b)

#part-c
c=(Set1 | Set2 | Set3) - b
print(c)

#part-d
d= set()
for i in range(1, 11):
    if i not in Set1:
        d.add(i)
print(d)

#part-e
e = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        e.add(i)
print(e)

#End of Program 8




















    
