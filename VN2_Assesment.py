'''
class Royal_pg_manage:
    def __init__(self, s=0, p=0, r=0, t=0, name='', address='', cindate='', rno=1):
        print("Welcome to ROYAL BOYS PG")
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.name = name
        self.address = address
        self.cindate = cindate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your Fullname:")
        self.address = input("\nEnter your address:")
        self.cindate = input("\nEnter your check in date:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):
        print("We have the following rooms for you:-")
        print("1.  Class A---->7000")
        print("2.  Class B---->6500")
        print("3.  Class C---->6000")
        print("4.  Class D---->5500")

        x = int(input("Enter the number what type of room you want ->"))
        n = int(input("For How Many Month Did You Stay:"))
        n == 30
        print("***** Monthly facilities *****")
        while (1):
            if (x == 1):
                print("you have choose room Class A")
                self.s =  500 + 500 + 500 + 500 + 500 + 1500 * n
                print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500", "3.Two Sharing---   > 500","4.TV---->500", "5. Single bathroom --->500")
                print("total rent is :",self.s)
            elif (x == 2):
                print("you have choose room Class B")
                self.s =  500 + 500 + 500 + 500 + 1500 * n
                print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500", "3.Two Sharing---   > 500","4.TV---->500")
                print("total rent is :", self.s)
            elif (x == 3):
                print("you have choose room Class C")
                self.s = 500 + 500 + 500 + 1500 * n
                print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500", "3.Two Sharing---   > 500")
                print("total rent is :", self.s)
            elif (x == 4):
                print("you have choose room Class D")
                self.s = 500 + 500 + 1500 * n
                print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500")
                print("total rent is :", self.s)
                break
            else:
                print("You've Enter an Invalid Key")

    def display(self):
        print("******complete PG bill******")
        print("Candidate details:")
        print("Candidate name:", self.name)
        print("Candidate address:", self.address)
        print("Check in date:", self.cindate)
        print("Room no.", self.rno)

def main():
    a = Royal_pg_manage()

    while (1):
        print("1.Enter Candidate Data")
        print("2.Calculate Room Rent")
        print("3.Calculate complete fasilities provides")
        print("4.Show total cost")
        print("5.EXIT")

        b = int(input("\nEnter the number of your choice:"))
        if (b == 1):
            a.inputdata()
        if (b == 2):
            a.roomrent()
        if (b == 3):
            a.display()
        if (b == 4):
            quit()
main()

'''


str = 'python is dynamic language'
a = "interpreter"
b = "dynamic"
str1 = str.replace(b,a)
print(str1)

a = "good morning"
b = "morning"
c = "evening"
d = a.replace(b,c)
print(d)

x = "my name is shinu"
b="shinu"
a="ganesh"
y=x.replace(b,a)
print(y)

str = " one, two, three, four"
str1 = str.split(',')
print(str1)

a = "1,2,3,4,5,6"
b = a.split(',')
print(b)

str = input("enter number seprated by space:")
b = str.split(",")
print(b)
for i in b:
    print(i)

str = ["apple","banana","chiku","mango"]
sep = ":"
str1 = sep.join(str)
print(str1)

str = ["mango","chiku","banana","apple"]
str1 = ";".join(str)
print(str1)


#chaning case of a string
#upper(),lower(),swascase(),title()

str = "python is high level interpreted language"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.swapcase())
print(str.title())
print(str.startswith("python"))
print(str.endswith("language"))

a = "my self ganesh topale. i am from nagpur maharashtra"
print(a.title())
print(a.endswith("maharashtra"))
print(a.startswith("my"))
print(a.swapcase())
print(a.upper())
print(a.lower())
print(a.capitalize())

#string testing methods
#methods - isalnum(), isalpha(), isdigit(), islower(), isupper(), istitle(), isspace()

a = "february4"
print(a.isalnum())
b = "february"
print(b.isalnum())

a = "abcd"
print(a.isnumeric())
print(a.isdigit())
print(a.isalpha())

