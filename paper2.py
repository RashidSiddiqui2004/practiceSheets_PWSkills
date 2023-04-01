
import pandas as pd

# display the longest word in a text file

ptr= open("Elon Musk.txt", "r")

words= []

wd= ""

for i in ptr.read():

    if(i==' ' or i=='$' or i== '%' or i=='#' or i=='.' or i=='\n' or i=='[' 
       or i==']' or i=='-' or i==";"):

        if(wd!= "" and wd.isnumeric()== False):
            words.append(wd)
            wd= ""
        else:
            continue
    
    else:
        wd += i

l3= words[25:100]

# print(l3)

lgt = words[0]

for i in words:

    if(len(i) > len(lgt)):
        lgt = i


print("Largest word in the given text file is: ", lgt)

ptr.close()

# Q6. Write a Python program to read a JSON file and print out the 
# value of a specified key.



# Q7. Can you provide a Python code snippet to write a list of strings 
# into a text file where each string is
# written on a new line?

#use l3 as above

f2= open("stringsWrite.txt", "w")

for i in l3:

    f2.write(i)
    f2.write("\n")

f2.close()

# Q3. Write a Python program to read a text file and 
# print out the most frequent word(s) in the file.

ptr= open("testFile.txt", "r")

words= {}

wd= ""

for i in ptr.read():

    if(i==' ' or i=='$' or i== '%' or i=='#' or i=='.' or i=='\n' or i=='[' 
       or i==']' or i=='-' or i==";"):

        if(wd!= "" and wd.isnumeric()== False):
            
            if(words.get(wd,-1)!= -1):

                words[wd] += 1
            
            else:
                words[wd] = 1

            wd= ""
        else:
            continue
    
    else:
        wd += i

listFreq= []

mostfreq= 1

for i in words:

    if(words[i] > mostfreq):
        mostfreq = words[i]

for i in words:

    if(words[i]== mostfreq):
        listFreq.append(i)

print("\nMOST FREQUENT WORDS ARE: \n")
for i in listFreq:
    print(i)

# Q2. Write a program that takes a list of strings and prints out each string
#  in reverse order using a for loop.


def revStr(lst):

    ans=[]

    for i in lst:
        s= i[::-1]
        ans.append(s)
    
    for i in ans:
        print(i)

    return

l= ["time","scholar","worth"]

revStr(l)

# Q9. Write a program that takes a list of integers as input and returns the 
# product of all the numbers in the list using a while loop.

def mult(l):

    prod= 1

    len1, i = len(l), 1

    while(i<= len1):

        prod *= l[i-1]
        i+=1

    return prod


l1= [7,4,2,3]

print(mult(l1))

# Q10. Write a program that prompts the user to enter a positive integer 
# and then prints out the factorial of
# that number using a while loop.

def fact(num):

    ans = 1
    while(num>= 1):
        
        ans*= num
        num-=1

    return ans

print(fact(5))
