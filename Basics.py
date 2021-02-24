#from typing import List


print("hello,world")

#variable
my_name = "Yuehan"
my_age = "19"
print(my_name + ":" + my_age)

# introduction = f"hello, my name is {my_name}."
# print(introduction)
price = 11.01
is_paid = True

#escape
greetings = "I say \"hi\""
print(greetings)

#str
str_sample = "good morning,mate!"
print(len(str_sample))
print(str_sample[0])#certain position
print(str_sample[0:4])#from..to..
print(str_sample[4:])#from..to the end
print(str_sample[:4])#from the start to..
print(str_sample[-1])#the end

#str functions
name_upper = my_name.upper()
print(name_upper)
find_x = my_name.find("u")
print(find_x)#-1:not found, if found, its index is return
name_change = my_name.replace("n","x")
print(name_change)

#conditional
lily_age = 19
if lily_age > 18:
    print("let's go to a bar")
if lily_age > 25:
    print("let's go to work")
elif lily_age == 19:
    print("let's go to school")
else:
    print("Let's go play ")


if lily_age > 18 and my_name == "Yuehan":
    print("hello lily, I'm Yuehan")

if is_paid:
    print("You have paid")
else:
    print("pay your price")


#falsy value
0
""
[]

#list
generate_zero = [0] * 20
print(generate_zero)
users = ["Bob","Lucy","Cathy","Pit"]
print(users[0])
print(users[:2])#same as strings
first_user = users[0]
#unpacking
print(first_user)
user1,user2,user3 = users[1:]
print(user2)
#add item
users.append("Alex")
print(users)
users.insert(2,"Ben")
user1,user2,user3,user4,user5 = users[1:]#number of unpacking needs to be the same
print(user2)
#remove
users.pop()#removing the last element
print(users)
#range
count_num = list(range(1,5))
print(count_num)

#tupples
letter = ('a','b','b','c')
#sets
unique_letter_set = {'a','b','c','d'}

#loops
#for loops
for element in users:
    print(element)
for i in range(10 ,20):
    print(i)
for letter in my_name:
    print(letter)
#while loops
age = 1 
while(age < 10):
    age += 1
    if age == 5:
        continue
    print(str(age) + " years old")

#Immutable
colors = ["blue","red","yellow"]
print(colors)
new_colors = colors
new_colors.insert(0,"pink")
print(colors)
print(new_colors)
#bool,int,str,tupples immutable
#list,set,dict->make copy, keep reference

#function
def say_hi():
    print("hi")
say_hi()
def double(i):
    return 2 * i
double_one = double(1)
print(double_one)
def add_sth(a,b = 1):#giving b a default value,used when nothing is passed in
    return a + b
plus_default = add_sth(10)
plus_two = add_sth(10,2)
print(plus_default)
print(plus_two)
def read_user_id():
    print("what's your name")
    user_name = input()
    print("welcome abroad," + user_name)
#read_user_id()

#dictionary
student_profile = {"name":"Dickenson","grade":"30","rank":"20","wrong_answer":[1,2,3,4]}
student_grade = student_profile["grade"]
print(student_grade)
student_profile["wrong_answer"][1] = 5
print(student_profile)
for item in student_profile:
    print(item)
print(student_profile.keys())
print(student_profile.items())
for key,val in student_profile.items():
    print(key)
    print(val)
if "name" in student_profile:
    print("found name")

#python library
import random
random_num = random.randint(1,10)
print(random_num)