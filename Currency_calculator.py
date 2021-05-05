###Using Python to create a currency exchange system
#Parent class

if __name__ == "__main__":
    class User():
        def __init__(self,present_curr,exchange_curr):
            self.present_curr = present_curr
            self.exchange_curr = exchange_curr

        def show_details(self):
            print("All the details entered by the user")
            print("")
            print("Your Present Currency is : ",self.present_curr)
            print("Your Exchange Currency is : ",self.exchange_curr)

        ###List of Available Currency: KWD,BHD,OMR,JOD,GBP,KYD,EUR,CHF,USD,CAD

    class Currency(User):
        def __init__(self,present_curr,exchange_curr):
            super().__init__(present_curr,exchange_curr)
            self.balance = 0
            self.kwd = 3.29
            self.bhd = 2.65
            self.omr = 2.60
            self.jod = 1.41
            self.gbp = 1.26
            self.kyd = 1.20
            self.eur = 1.14
            self.chf = 1.04
            self.usd = 1.00
            self.cad = 0.73
            self.ngn = 0.0026

        def deposit(self,amount):
            self.amount = amount
            self.balance = self.balance + self.amount
            print("Enter you desired amount in NGN: ₦",self.amount)

        def exchange(self):
            if self.exchange_curr == "kwd":
                self.balance = self.balance * self.ngn / self.kwd 
                print("Your Exchange value in KD rial is : KD", self.balance)

            elif self.exchange_curr == "bhd":
                self.balance = self.balance * self.ngn / self.bhd
                print("Your Exchange value in BD rial is : BD", self.balance)
                
            elif self.exchange_curr == "omr":
                self.balance = self.balance * self.ngn / self.omr
                print("Your Exchange value in OMR rial is : ر.ع.", self.balance)

            elif self.exchange_curr == "jod":
                self.balance = self.balance * self.ngn / self.jod
                print("Your Exchange value in JOD rial is : د.ا", self.balance)

            elif self.exchange_curr == "gbp":
                self.balance = self.balance * self.ngn / self.gbp
                print("Your Exchange value in GBP is : £", self.balance)

            elif self.exchange_curr == "kyd":
                self.balance = self.balance * self.ngn / self.kyd
                print("Your Exchange value in KYD Dollars is : $", self.balance)

            elif self.exchange_curr == "eur":
                self.balance = self.balance * self.ngn / self.eur
                print("Your Exchange value in EUR is : €", self.balance)

            elif self.exchange_curr == "chf":
                self.balance = self.balance * self.ngn / self.chf
                print("Your Exchange value in CHF is : CHF", self.balance)
                
            elif self.exchange_curr == "usd":
                self.balance = self.balance * self.ngn / self.usd
                print("Your Exchange value in USD is : $", self.balance)

            elif self.exchange_curr == "cad":
                self.balance = self.balance * self.ngn * self.usd / self.cad
                print("Your Exchange value in CAD is : C$", self.balance)

            else:
                print("Invalid Currency Entered")

        def view_transaction(self):
            self.show_details()
            print("Your Transaction is", self.balance)
            




            

                
