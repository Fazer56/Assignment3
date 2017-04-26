

class Contact:
    def __init__(self, firstName, surname, business, donation, volunteer):
        self.firstName = firstName
        self.surname = surname
        self.business = business
        self.donation = donation
        self.volunteer = volunteer


    def dispInfo(self):
        print(self.firstName + " " + self.surname + " " + self.business)
        if self.donation > 1:
            print("Thanks")
        elif self.volunteer == "y":
            print("Thanks very much")
        elif self.donation ==0:
            print("Maybe Next time")


def main():
    dude = Contact("Jerry", "Springer", "Restraunter", 2, "no")
    dude2 = Contact("Johhny", "Fortune", "Builder", 0, "no")

    dude.dispInfo()
    dude2.dispInfo()


    
if __name__ == '__main__':
    main()
