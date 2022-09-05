import sqlite3
from SQLite_demo_employee import Employee


conn = sqlite3.connect("employee.db")

c = conn.cursor()

# c.execute("""CREATE TABLE Employees (
  #          first text,
   #         last text,
    #        pay interger
     #       )""")

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))

conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})

conn.commit()

c.execute("SELECT * FROM employees WHERE last='Doe'")

print(c.fetchall())

conn.commit()

conn.close()


