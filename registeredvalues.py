class logincred:
    def __init__(self,uname,password,email):
        self.uname = uname
        self.password = password
        self.email = email
    def __repr__(self):
        return "logincred('{}','{}','{}')".format(self.uname,self.password,self.email)

#
# # PF-Tryout
#
# def generate_next_date(day, month, year):
#     # Start writing your code here
#     if month ==1 or month == 3 or month==5 or month==7 or month ==8 or month ==10 :
#         if day >= 1 and day <= 30:
#           next_day = day + 1
#           next_month = month
#           next_year = year
#         else:
#             next_day =1
#             next_month = month+1
#             next_year = year
#     elif month ==4 or month == 6 or month==9 or month==11:
#         if day >= 1 and day <= 29:
#           next_day = day + 1
#           next_month = month
#           next_year = year
#         else:
#             next_day = 1
#             next_month = month+1
#             next_year = year
#     elif month==2:
#         if day >= 1 and day <= 28:
#           next_day = day + 1
#           next_month = month
#           next_year = year
#         else:
#             next_day = 1
#             next_month = 3
#             next_year = year
#     else:
#         if day >= 1 and day <= 30:
#             next_day = day + 1
#             next_month = month
#             next_year = year
#         else:
#             next_day = 1
#             next_month = 1
#             next_year = year+1
#
# 
#
#
#
#
#
#
#
#
#
#     print(next_day, "-", next_month, "-", next_year)
#
#
# generate_next_date(30, 6, 2015)
