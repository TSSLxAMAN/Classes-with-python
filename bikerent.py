class Bikerent:
    totalbikes = 100

    def rentbikes(self, rentquantity):
        if rentquantity > Bikerent.totalbikes:
            print(
                f"We don't have that much of bikes currently we have {Bikerent.totalbikes} bikes"
            )
        elif rentquantity < Bikerent.totalbikes:
            print(
                f"Thanks for renting bikes from us \nWe will sent you {rentquantity} bikes soon!!\nThe amount will be {rentquantity*500}\nBikes remaining are {Bikerent.totalbikes - rentquantity}"
            )
            self.rentbikes = rentquantity
            Bikerent.totalbikes = Bikerent.totalbikes - rentquantity

        else:
            print("Bikes no avliable")

    @classmethod
    def increse_bikes(cls, newbikes):
        Bikerent.totalbikes = Bikerent.totalbikes + newbikes


print("WELCOME TO AMAN BIKE RENT SERVICES")
while True:
    print(
        """
        1 = total no. of bikes
        2 = rent no. of bikes
        3 = increse no. of bikes
        4 = exit

    """
    )
    userinput = int(input("Enter your choice : "))
    x = Bikerent()
    if userinput == 1:
        print(f"Total bikes are : {Bikerent.totalbikes}\n")
    elif userinput == 2:
        bikes_for_rent = int(input("Enter the amount of bikes you want for rent : "))
        x.rentbikes(bikes_for_rent)

    elif userinput == 3:
        newbikes = int(input("Enter the amount of bikes you want to add : "))
        x.increse_bikes(newbikes)
    elif userinput == 4:
        break
