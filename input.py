
#Question 1
#Program to find average of 3 numbers entered by user
Num1=input("Enter First number:")
Num2=input("Enter Second number:")
Num3=input("Enter Third number:")

Average=((float(Num1)+float(Num2)+float(Num3))/3)

print("The Average of three numbers:",Average)
#End of Program 1


#Question 2
#Program to compute a person's income tax
gi=input("Enter Gross Income (to the Nearest Penny):")
dep=input("Enter number of Dependents:")

ti = int(gi)-10000-int(dep)*3000
#ti stands for taxable income
tax=int(ti)*20/100

print("Your income tax:",tax)
#End of Program 2


#Question 3
#Program to store different data type values into a list
sid=input("Enter SID:")
name=input("Enter Name:")
gender=input("Enter Gender(use M for male, F for female, U for unknown):")
cn=input("Enter Course Name:")
cgpa=float(input("Enter CGPA:"))

l=[sid,name,gender,cn,cgpa]

print("Student:",l)
#End of Program 3

#Question 4
#Program to enter marks of 5 students into a list 
stud1=input("Enter marks of 1st Student:")
stud2=input("Enter marks of 2nd Student:")
stud3=input("Enter marks of 3rd Student:")
stud4=input("Enter marks of 4th Student:")
stud5=input("Enter marks of 5th Student:")

marks=[stud1,stud2,stud3,stud4,stud5]

print("Marks of respective students:",marks)
marks.sort()
print("Sorted marks:",marks)
#End of program 4


#Question 5
#Program to print a specified list
color=['Red','Green','White','Black','Pink','Yellow']
print("List of colors:",color)
#part a
color.remove('Black')
print("color:",color)

#part b
color=['Red','Green','White','Black','Pink','Yellow']
color[3]=color[4]='Purple'
print("color:",color[0:4]+color[5:])
#End of program 5

