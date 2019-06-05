class Employee:

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.fname,self.lname,self.pay)