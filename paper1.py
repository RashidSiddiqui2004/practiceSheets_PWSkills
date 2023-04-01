
# Q1.Check if armstrong number or not
#Sol:-

def isArm(num):

    cubesSum = 0

    temp =  num

    while num > 0:

        dig= num% 10

        cubesSum += pow(dig,3)

        num = num // 10
    
    if(cubesSum== temp):
        print(temp," is Armstrong number.")

    else:
        print(temp ,"is not Armstrong number.")

    return

# n = int(input("enter n :"))

# isArm(n)

#q2. ques on lists

# a= input("Enter a: ")

# l1= [2,3,4,5,6,7,a]

# l1.append("apples")

# print(l1)

# l1.extend(['banana', 'grapes' , 'orange'])

# print(l1)

# l1[6]= 'apple'

# print(l1)

# Q4. Use list comprehension to square the given list L=[2,4,7,3,6,8]

L=[2,4,7,3,6,8]

print("squares of L is:")

print([x*x for x in L])


# Q5. Create a function that takes in a tuple of integers and returns 
# the sum of the integers. Test the
# function with a tuple of your choice.

def fun2(tup1):

    sum = 0

    for i in tup1:
        sum+= i

    print("SUM IS:", sum)

t1= (45,78,12,25,63)

fun2(t1)

# Q6. Create two sets of your favourite fruits, and use the union()
#  method to combine them into a single set.
# Print the resulting set to the console.

set1= {"hello", "NSUT","IT","rashid"}

set2= {"hi","DTU"}

set3 = set1.union(set2)

for i in set3:
    print(i)


# Q7. Create a set of random words, and use the add() method to add
#  a new word to the set. Print the
# resulting set to the console.

set1= {"hello", "NSUT","IT","rashid"}

set1.add("CSE")

print("Updated set is: ")

for i in set1:
    print(i)

# Q9. favorite_books = {"1984", "To Kill a Mockingbird", "Pride and 
# Prejudice"}
# favorite_movies = ["The Shawshank Redemption", "The Godfather", 
# "The Dark Knight"]

# Use the zip() function to combine the book set and movie list 
# into a list of tuples representing book/
# movie pairs. Print the resulting list.





# Q10. Write a Python program to find the difference between
#  consecutive numbers in a list.

def consDiff(l1):

    l2 =[]
    for i in range(len(l1)-1):

        l2.append(l1[i+1]- l1[i])

    print("Difference b/w Consecutive Numbers in the given list is : ")
    for i in l2:
        print(i, end=" ")

lst= [78,15,255,63,25,12,50,23,85,96]

consDiff(lst)

# Q12. Write a function called word_count(text) that takes a string as input 
# and returns a dictionary where
# each key is a word in the text and its value is the number of times 
# that word appears in the text. For
# example, word_count("hello world hello") should return 
# {"hello": 2, "world": 1}.

def wordCounter(text):

    dict = {}

    l1= text.split()

    for i in l1:

        if(dict.get(i.lower(),-1) == -1):
            dict[i.lower()] = 1
        
        else:
            dict[i.lower()] += 1

    for i in dict:
        print(i, ": ",dict[i])
    
# text= input("\n Enter text: ")

# print("WORDS: \t FREQUENCY")

# wordCounter(text)

# Q4. Create a dictionary called phone_book with the following key-value pairs:
# "Alice": "555-1234"
# "Bob": "555-5678"
# "Charlie": "555-9012"
# Then, prompt the user to enter a name and print out the
#  corresponding phone number. If the name is not
# in the phone book, print out a message saying that 
# the name was not found.

phoneBook = {"Alice": "555-1234",
"Bob": "555-5678",
"Charlie": "555-9012"}

# name= input("Enter name to search: ")

# if(phoneBook.get(name,-1)== -1):
#     print("The name was not found")

# else:
#     print(name,": ",phoneBook.get(name,-1))


# Q6. Write a program that prompts the user to enter a password.
#  If the password is "password123", print
# out "Access granted", otherwise print out "Access denied".

# pwd = input("Enter password:")

# if(pwd== 'password123'):
#     print("Access granted")

# else:
#     print("Access denied")


import matplotlib.pyplot as plt

import numpy as np

x= np.random.rand(40)

y= np.random.rand(40)

# graph= plt.scatter(x,y, c="#FA8072", alpha=0.8,marker="*")

# plt.title("RANDOM DATA - DATA SCIENCE MASTERS")
# plt.xlabel("X-Values")

# plt.ylabel("Y-Label")

# plt.show()

x1= np.linspace(0.5,10,100)

y1= np.tan(x1)

plt.plot(x1,y1,"--g")
plt.title("TAN CURVE")

plt.ylabel("Tangent values")
plt.ylabel("Angle(in Radians)")
# plt.figure(figsize=(8,2))

plt.show()


d1= ["h1","h2","h3","h4"]

val1= [45,78,69,100]

plt.barh(d1,val1)

plt.title("Horizontal Bar Chart to visualise Categorical data")

plt.grid()
plt.figure(figsize=(10,3))

plt.show()