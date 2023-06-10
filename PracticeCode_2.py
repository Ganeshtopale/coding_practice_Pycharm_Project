""""
print("welcome to state bank of india")
money=10000
p = int(input("please enter your ATM pin:"))
if p in range(0,9):
    print("please enter youer pin :")
if p!= 1234:
    print("invalid")
    print("1 = withdraw")
    print("2= balance enquiry")
    print("3 = fast cash")

c= int(input("please choose transaction"))
if (c == 1):
    w = int(input("enter withdraw amount"))
    if(w<m and w% 100==0):
        print("please take your cash")
    else:
        print("invalid choose")

elif (c == 2):
    print("available amount is :",money)
elif(c == 3):
    print("1 -> 500")
    print("2 -> 1000")
    print("3 -> 2000")
    print("4 -> 5000")
    print("5 -> 10000")
    f = int(input("enter fast cash"))
    if(f == 1 and 500 < money):
        print("please take your cash")
    elif(f == 2 and 1000 < money):
        print("please take your cash")
    elif(f == 3 and 2000 < money):
        print("please take your cash")
    elif(f == 4 and 5000 < money):
        print("please take your cash")
    elif(f == 5 and 10000 < money)
        print(" please take your cash")
    else:
        print("invalid fast cash option ")

else:
    print("wrong choose")

"""
print("welcome to state bank of india")
money = 10000
p = int(input("please enter your ATM pin:"))
if p in range(0, 9):
    print("please enter your pin :")
if p == 1234:
    print("invalid")
    print("1 = withdraw")
    print("2= balance enquiry")
    print("3 = fast cash")
if p != 1234:
    print("invalid")
c = int(input("please choose transaction"))
if (c == 1):
    w = int(input("enter withdraw amount"))
    if (w < money and w % 100 == 0):
        print("please take your cash")
    else:
        print("invalid choose")

elif (c == 2):
    print("available amount is :", money)
elif (c == 3):
    print("1 -> 500")
    print("2 -> 1000")
    print("3 -> 2000")
    print("4 -> 5000")
    print("5 -> 10000")
    f = int(input("enter fast cash"))
    if (f == 1 and 500 < money):
        print("please take your cash")
    elif (f == 2 and 1000 < money):
        print("please take your cash")
    elif (f == 3 and 2000 < money):
        print("please take your cash")
    elif (f == 4 and 5000 < money):
        print("please take your cash")
    elif (f == 5 and 10000 < money):
        print(" please take your cash")
    else:
        print("invalid fast cash option ")

else:
    print("wrong choose")

#########################################################################################


print("--------------using lambda function--------------")

a = lambda x: x*2
print(a(25))

a = lambda y: y**2
print(a(5))

a = lambda z:print(z**2)
a(8)
a(12)
a(13)
a(100)

a = lambda p,r,y: print("simple intrest",p*r*y/100)
a(20000,8.10,3)


p=int(input("enter principle"))
r=int(input("enter rate of intrest"))
y= int(input("enter year"))
a = lambda p,r,y: print("simple intrest",p*r*y/100)
a(p,r,y)

p=int(input("enter principle"))
r=int(input("enter rate of intrest"))
y= int(input("enter year"))
a = lambda p,r,y: p*r*y/100
print("simple intrest",a(p,r,y))


print('-------------lambda using def funtion--------------')

def sumation(a,b,c):
    return lambda x: a*x**2+b*x+c
a=sumation(10,5,2)
print(a(20))
print(a(10))
print(a(5))
print(a(2))

print("-----------lambda function( map,filter,reduce)----------------")
print("----map-------")
a = (2,4,6,8,10)
result = map(lambda x: x+x,a)
print(list(result))

a=(1,2,3,4,5,6)
b=(1,2,3,4,5,6)
result=map(lambda x,y: x+y,a,b)
print(list(result))

a = [1,2,3,4,5]
result = map(lambda x: x,a)
print(list(result))

a = (1,2,3,4,5)
b = (9,8,7,6,5)
c = (1,2,3,4,5)
result = map(lambda x,y,z: x+y+z,a,b,c)
print(list(result))

print("==============map in list-------------------")
l = ['cat','bat','mat','rat']
result = list(map(list,l))
print(result)

print("----------map in list add two list-----------")

l = ['cat','bat','mat','rat']
m = ['hat','cat','nat','eat']
result= list(map(list,l+m))
print(result)

import functools

lis = [1, 3, 5, 6, 2, ]
#print("The sum of the list elements is : ", end="")

a = functools.reduce(lambda x,y: x+y,lis)
print(a)
#print(functools.reduce(lambda a, b: a + b, lis))



seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


print("//////////////////////////////////////////////////////////////////")

print("-----------------find odd/even number----------")

odd = []
even = []
for i in range(1, 101):
    if i%2 == 0:
        even.append(i)
        if len(even) == 20:
            break
    else:
        odd.append(i)
        if len(odd) == 20:
            break
print(odd, even)

print("/////////////////////////////////////////////////////////////////////////////////")

print("-------------------to check perfect square---------------------------")

import math

num = int(input("Enter number:"))
root = math.sqrt(num)
if int(root + 0.5) ** 2 == num:
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square ")

print("--------------divisible by 3 check---------------")
a = int(input("Enter your number:"))
if a % 3 == 0:
    print("divisible by 3")
else:
    print("not divisible by 3")


print("---------add/multiplication using function----------")
def add(*a):
    total=0
    for i in a:
        total=total+i
        print("sum:",total)
add(1,2,3,10,15,20,100,110)


def mult(*a):
    total=1
    for i in a:
        total=total*i
        print("summation:",total)
mult(1,2,3,10,15,20,100,110)

print("------------------------------factorial find--------------------------")

n=int(input("Enter factorial number:"))
if (n == 0 or n == 1):
    print(1)
else:
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    print(fac)


print("--------------------------------control statement-----------------------------------")
print("----------break/ continue / pass---------------")

for i in range(1,10):
    if i == 5:
        break
        print(i)

for i in range(1,10):
    if i == 6:
        continue
        print(i)
        i += 1


print("------------- *arg / non keyword arguments------------")

def myfun(*args):
    for i in args:
        print(i)
myfun("hello ","VN2 solution pvt ltd")

print("-------------- **karg / keyword arguments")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
# Driver code
myFun(first='Ganesh', mid='Subhash', last='Topale')

l = "python"
a = l.split()
print(a)

#//////////////////////////////////////////////////////////////////////

my_num = int(input("Enter a number :"))
my_factorial = 1
while(my_num>0):
   my_factorial = my_factorial*my_num
   my_num=my_num-1
print("The factorial of the number is : ")
print(my_factorial)

#/////////////////////////////////////////////////////////////////////////////////////

n= int(input("enter number"))
fact = 1
while(n>0):
    fact=fact*n
    n = n - 1
print("my factorial is:",fact)

#//////////////////////////////////////////////////////////////////////////////////////

def myfunc():
    x = 100000000
    def innerfunc():
        print(x)
    innerfunc()
myfunc()

a = {1,2,3,4,5}
a.add(6)
print(a)

a.remove(3)
print(a)

a.add(3)
print(a)

class Student:
    def __init__(self,name,age,classroom,rollno):
        self.n = name
        self.a = age
        self.c = classroom
        self.r = rollno
    def display(self):
        print("student details;---",self.n,self.a,self.c,self.r)
s=Student("johny",18,'A',22)
t=Student("john",19,'A',21)
u=Student("johnson",19,'A',23)
s.display()
t.display()
u.display()

##########################################################################################

from tkinter import *
from tkinter.ttk import *
win = Tk()
win.title("Welcom to check button is properly working")
win.geometry('400x500')
rad1 = Radiobutton(win,text='First', value=1)
rad2 = Radiobutton(win,text='Second', value=2)
rad3 = Radiobutton(win,text='Third', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=0, row=1)
rad3.grid(column=0, row=2)
win.mainloop()


#######################################################################################

'''
from tkinter import*
root = Tk()
myLabel1 = Label(root, text = "Hello World !")
myLabel2 = Label(root, text = " My name is shinu")
myLabel3 = Label(root, text= "I'm from Nagpur")
myLabel1.grid(row= 0, column = 0)
myLabel2.grid(row= 1, column = 0)
myLabel3.grid(row= 2, column = 0)

root.mainloop()

'''

from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text= "look i am click a button!")
    myLabel.pack()
myButton= Button(root, text="click me!",padx=50, pady= 50, command= myClick)
myButton.grid(row=0, column=0)
myButton.pack()
root.mainloop()


############################################################################################

