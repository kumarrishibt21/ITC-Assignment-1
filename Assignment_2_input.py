#Assignemt 2


#Question 1

#input string
inp_str="Python is a case sensitive language"

#part a
#Program to find the length of input string
print(len(inp_str))

#part b
#Program to reverse the order of the string
print(inp_str[ : :-1])

#part c
#Program to store in new string
#new string
new_str=inp_str[10:26]
print(new_str)

#part d
#Program to replace
print(inp_str.replace("a case sensitive", "object oriented"))

#part e
#Program to find the index of substring
print(inp_str.find("a"))

#part f
#Program to remove white spaces
print(inp_str.replace(" ", ""))


#End of Program 1



#Question 2

#Program to store your details and print desired output

#var=variable

var1="Kumar Rishi"
var2="21104088"
var3="Electrical"
var4="9.9"

print("Hey, %s Here!"%var1)

print("My SID is %s"%var2)

print("I am from %s department and "%var3, end="")

print("my CGPA is %s"%var4)


#End of Program 2



#Question 3

#Program to calculate
a=56
b=10

#part a
print(a&b)

#part b
print(a|b)

#part c
print(a^b)

#part d
print(a<<2)
print(b<<2)

#part e
print(a>>2)
print(b>>4)


#End of Program 3



#Question 4

#Program to calculate greatest of three numbers entered by user

num1=input("Enter first number :")
num2=input("Enter second number :")
num3=input("Enter third number :")

#greatest value of three numbers
max_val=max(num1, num2, num3)

print("Greatest of three numbers is :",max_val)


#End of program 4


#Question 5

#Program to check if the word "name" is present in the string entered by user
inp_str=str(input("Enter String:"))

if "name" in inp_str:
    print("Yes")
else:
    print("No")

#End of Program 5


#Qusetion 6

#Program to check whether input lengths can form a triangle or not

#s=side
s1=int(input("Enter first side:"))
s2=int(input("Enter second side:"))
s3=int(input("Enter third side:"))

if (s1+s2>s3)&(s2+s3>s1)&(s3+s1>s2):
    print("Yes")
else:
    print("No")


#End of program 6


