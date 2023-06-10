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
        if (x == 1):
            print("you have choose room Class A")
            self.s = 1500 * n + 500 + 500+ 500 + 500 + 500
            print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500", "3.Two Sharing---   > 500", "4.TV---->500","5. Single bathroom --->500")
        elif (x == 2):
            print("you have choose room Class B")
            self.s = 1500 * n + 500 + 500+ 500 + 500
            print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500", "3.Two Sharing---   > 500", "4.TV---->500")
        elif (x == 3):
            print("you have choose room Class C")
            self.s = 1500 * n + 500 + 500+ 500
            print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500", "3.Two Sharing---   > 500")
        elif (x == 4):
            print("you have choose room Class D")
            self.s = 1500 * n + 500 + 500
            print("Facilities will be provide: 1.Wifi----->500", "2.Hot Water----->500",)
        else:
            print("please choose a room")
            print("your choosen room rent is =", self.s, "\n")

    def facilities(self):

        print("***** Monthly facilities *****")

        print("1.Wifi----->500", "2.Hot Water----->500", "3.Two Sharing---   > 500", "4.TV---->500","5. Single bathroom --->500",
              "6.Exit")

        while (1):

            c = int(input("Enter the number of your choice:"))

            if (c == 1):
                d = int(input("normal room:"))
                self.r = self.s + 500 + 500 * d
                print("Total rent is : ",self.r)

            elif (c == 2):
                d = int(input("two sharing room:"))
                self.r = self.s + 500 + 500 +500 * d
                print("Total rent is :",self.r)

            elif (c == 3):
                d = int(input("two sharing with TV room:"))
                self.r = self.s + 500 + 500 + 500 + 500 * d
                print("Total rent is : ",self.r)

            elif (c == 4):
                d = int(input("Two sharing with common bathroom:"))
                self.r = self.s + 500 + 500 + 500 + 500 + 500 * d
                print("Total rent is :",self.r)

            elif (c == 5):
                d = int(input("Two sharing single bathroom:"))
                self.r = self.s + 500 + 500+ 500 + 500 + 500 + 500 * d
                print("Total rent is :",self.r)

            elif (c == 6):
                break
            else:
                print("You've Enter an Invalid Key")

        print("Total food Cost=Rs", self.r, "\n")

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
            a.facilities()
        if (b == 4):
            a.display()
        if (b == 5):
            quit()
main()