"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    contract_type = ""
    salary_pay = 0
    hours = 0
    hourly_pay = 0
    commission_type = "none"
    contracts = 0
    contract_pay = 0
    bonus_pay = 0

    def __init__(self, name,
                 contract_type,
                 salary_pay,
                 hours,
                 hourly_pay,
                 commission_type,
                 contracts,
                 contract_pay,
                 bonus_pay):

        self.name = name
        self.contract_type = contract_type
        self.salary_pay = salary_pay
        self.hours = hours
        self.hourly_pay = hourly_pay
        self.commission_type = commission_type
        self.contracts = contracts
        self.contract_pay = contract_pay
        self.bonus_pay = bonus_pay

    def get_pay(self):

        contract_pay = 0

        if self.contract_type == "salary":
            contract_pay = self.salary_pay
        elif self.contract_type == "hourly":
            contract_pay = self.hours * self.hourly_pay

        commission_pay = 0

        if self.commission_type == "bonus":
            commission_pay = self.bonus_pay
        elif self.commission_type == "contracts":
            commission_pay = self.contracts * self.contract_pay

        total_pay = contract_pay + commission_pay

        return total_pay

    def __str__(self):

        final_string = ""

        if self.contract_type == "salary" and self.commission_type == "none":

            final_string = f"{self.name} works on a monthly salary of {str(self.salary_pay)}."

        elif self.contract_type == "salary" and self.commission_type == "contracts":

            final_string = f"{self.name} works on a monthly salary of {str(self.salary_pay)} and receives a commission for {str(self.contracts)} contract(s) at {str(self.contract_pay)}/contract."

        elif self.contract_type == "salary" and self.commission_type == "bonus":

            final_string = f"{self.name} works on a monthly salary of {str(self.salary_pay)} and receives a bonus commission of {self.bonus_pay}."

        elif self.contract_type == "hourly" and self.commission_type == "none":

            final_string= f"{self.name} works on a contract of {str(self.hours)} hours at {str(self.hourly_pay)}/hour."

        elif self.contract_type == "hourly" and self.commission_type == "contracts":

            final_string= f"{self.name} works on a contract of {str(self.hours)} hours at {str(self.hourly_pay)}/hour and receives a commission for {str(self.contracts)} contract(s) at {str(self.contract_pay)}/contract."

        elif self.contract_type == "hourly" and self.commission_type == "bonus":

            final_string= f"{self.name} works on a contract of {str(self.hours)} hours at {str(self.hourly_pay)}/hour and receives a bonus commission of {self.bonus_pay}."

        final_string = final_string + f" Their total pay is {str(self.get_pay())}."

        return final_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", 4000, 0, 0, "none", 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 0, 100, 25, "none", 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "salary", 3000, 0, 0, "contracts", 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 0, 150, 25, "contracts", 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", 2000, 0, 0, "bonus", 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 0, 120, 30, "bonus", 0, 0, 600)


print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))