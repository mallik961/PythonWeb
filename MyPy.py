import sqlite3
from EmployeeClass import Employee




conn = sqlite3.connect('MyDataBase.db')

cur = conn.cursor()

# cur.execute("""CREATE TABLE employees (
#                   first  text,
#                   last text,
#                   pay integer )""")

def insert(emp):
    with conn:
     cur.execute("INSERT INTO employees VALUES (:first,:last,:pay)",
                {'first': emp.fname, 'last': emp.lname, 'pay': emp.pay})


def select(first):
    cur.execute("SELECT * FROM employees WHERE first=:first",{'first':first})

    return cur.fetchall()

def update(emp,pay):
    with conn:
     cur.execute("""UPDATE employees SET pay =:pay WHERE first=:first AND last=:last""",{'pay':pay,'first':emp.fname,'last':emp.lname})

def delete(emp):
    with conn:
        conn.execute("""DELETE from employees WHERE first=:first AND last = :last""",{'first':emp.fname,'last':emp.lname})



emp1 = Employee('Sharma','Mallik','19000')
emp2 = Employee('Sharma','Rajagopal','19000')

#print(emp1.lname)


#insert(emp1)
# insert(emp2)
#
# update(emp2,19000)

#delete(emp2)

#cur.execute("DELETE FROM employees")



# values = select("Sharma")
# print(values)


# cur.execute("INSERT INTO employees VALUES ('Kedar','Eas','10000')")
#
# e1 = Employee("akila","deswari","9000")
# e2 = Employee("kannan","deswari","8000")
# e3 = Employee("kedar","sharma","7000")
#
# #print(e1.fname)
# cur.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':e1.fname,'last':e1.lname,'pay':e1.pay})
# cur.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':e2.fname,'last':e2.lname,'pay':e2.pay})
# cur.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':e3.fname,'last':e3.lname,'pay':e3.pay})
#
#
#
#
#
#cur.execute("DELETE FROM employees WHERE first='Sharma'")

cur.execute("SELECT * FROM employees")

print(cur.fetchall())








# conn.commit()
conn.close()