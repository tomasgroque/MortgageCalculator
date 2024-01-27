class Mortgage:
    home_price = 0
    down_payment = home_price * 0.10
    loan_term = 10
    interest_rate = 8.2

    def __init__(self, home_price, down_payment, loan_term = 10, interest_rate = 8.2):
        self.home_price = int(home_price)
        self.down_payment = int(down_payment)
        self.loan_term = int(loan_term)
        self.interest_rate = float(interest_rate) 
    
    def mortgage_payment(self):
        loan_amount = self.home_price - self.down_payment
        year_interest = loan_amount * (self.interest_rate/100)
        total_payment = loan_amount + (year_interest * self.loan_term)
        return total_payment
    
    def yeraly_payment(self, total_amount):
        return total_amount / self.loan_term
    
    def monthly_payment(self, total_amount):
        return (total_amount / self.loan_term) / 12

    def mortgage_calculation(self):
        total_payment = self.mortgage_payment()
        yearly = self.yeraly_payment(total_payment)
        monthly = self.monthly_payment(total_payment)

        print("Total amount to pay {}".format(total_payment))
        print("Year Payment {}".format(yearly))
        print("Monthly Payments {}".format(monthly))
        print('//////////////////////////////////////////////')
    
    def compare_diferent_interest(self):
        number = input("How many different interest are we going to compare? ")
        for interest in range(int(number)):
            new_rate = input("Introduce interest rate number {}.".format(int(interest)+1))
            self.interest_rate = float(new_rate)
            self.mortgage_calculation()
            print('//////////////////////////////////////////////')
       
        


# Main program 
calculating = True
print("Hello Costumer and Welcome to the Mortgage Calculator!!!")
while calculating:
    home_price = input("Enter the cost of the home you wish to buy. ")
    down_payment = input("What's the down payment? ")
    loan_term = input("Enter the loan term in years. ")
    interest_rate = input("At what interest rate is your loan? ")

    new_mortgage = Mortgage(home_price, down_payment, loan_term, interest_rate)
    new_mortgage.mortgage_calculation()

    compare = input("Would you like to compare different interest rates? Y/N. ")
    if compare.upper() == 'Y':
        new_mortgage.compare_diferent_interest()
    
    exit = input("Would you like to make a new Mortgage calculation? Y/N. ")
    if exit.upper() == 'N':
        calculating = False