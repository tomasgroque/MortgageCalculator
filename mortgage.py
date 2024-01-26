class Mortgage:
    home_price = 0
    down_payment = home_price * 0.10
    loan_term = 10
    interest_rate = 8.2

    def __init__(self, home_price, down_payment, loan_term = 10, interest_rate = 8.2):
        self.home_price = home_price
        self.down_payment = down_payment
        self.loan_term = loan_term
        self.interest_rate = interest_rate 
    
    def mortgage_payment(self):
        loan_amount = self.home_price - self.down_payment
        year_interest = loan_amount * (self.interest_rate/100)
        total_payment = (loan_amount + year_interest) * self.loan_term
        return total_payment
    
    def yeraly_payment(self, total_amount):
        return total_amount / self.loan_term
    
    def monthly_payment(self, total_amount):
        return (total_amount / self.loan_term) / 12

    

calculating = True
while calculating:
    print("Hello Costumer and Welcome to the Mortgage Calculator!!!")
    home_price = input("Enter the cost of the home you wish to buy.")
    down_payment = input("What's the down payment?")
    loan_term = input("Enter the loan term in years.")
    interest_rate = input("At what interest rate is your loan?")