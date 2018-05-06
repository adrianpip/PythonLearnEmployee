import requests

class Employee:

    min_hourly_wage = 17.91 #LAW
    weeks_per_year = 52.0 #assume full-time
    hours_per_week = 40.0 #assume full-time
    min_superannuation_percent = 9.5
    atCompanyDefault="@company.com"
    min_salary = min_hourly_wage * hours_per_week * weeks_per_year #LAW #assume full-time
    
    def __init__(self,firstName,lastName,salary_parm=min_salary): 
        self.firstName=firstName[0].upper() + firstName[1:].lower()
        self.lastName=lastName[0].upper() + lastName[1:].lower()
        self.fullName = '{} {}'.format(self.firstName,self.lastName)
#        self.email()
##        tom = self.tell_email()
        self.salary=salary_parm
              
    def apply_raise_hidden(self,percent):
        new_salary = self.salary * (1 + percent/100)
        self.min_salary = self.min_hourly_wage * self.hours_per_week * self.weeks_per_year #LAW #assume full-time
        if self.salary < self.min_salary: #LAW #assume full-time
            #assume full-time 
            self.salary = self.min_salary #LAW #assume full-time
            print( self.fullName + " is on minimum p.a. " + str(self.min_salary))
        else:
            self.salary = self.new_salary

    def apply_raise_201805():
        self.apply_raise_hidden(self,1.0)
        
    def apply_raise_201711():
        self.apply_raise_hidden(self,-1.1)

    def change_name(self,fullname): #,atCompany=self.atCompanyDefault):
        self.fullName=fullname
        self.email=name.lower().replace(" ","_") + atCompany
        fred = self.tell_email()
        print(" new email is "+self.email)

    def tell_email(self,url=f"https://www.google.com/"):
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return '_bad response!'

    @property
    def email(self): #,atCompany=self.atCompanyDefault):
        return '{}.{}'.format(self.firstName.lower(),self.lastName.lower())+"@company.com" #+atCompany

