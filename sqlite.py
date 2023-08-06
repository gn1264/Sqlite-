import sqlite3
a=sqlite3.connect("gaurav.db")
b=a.cursor()
a.execute(""" create table IF NOT EXISTS stud(Name datatype,regno datatype unique,marks datatype) """)
a.execute(""" insert into stud values("Gaurav", 25 ,98)""")
a.execute(""" insert into stud values("Aman", 12 ,92)""")
a.execute(""" insert into stud values("Ram", 25 ,95)""")
d= a.execute("""select * from stud where Name like "A%" """).fetchall()
print(d)