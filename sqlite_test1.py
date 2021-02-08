import sqlite3

con = sqlite3.connect('first_test.db')
cursObj = con.cursor()

mode = input()
cursObj.execute("CREATE TABLE if not exists manufacter(id integer PRIMARY KEY AUTOINCREMENT, name text)")
cursObj.execute("CREATE TABLE if not exists products(id integer PRIMARY KEY AUTOINCREMENT , ram integer, cpu text, vendor_id integer FOREIGN KEY REFERENCES manufacter (id) ON DELETE CASCADE ON UPDATE NO ACTION)")
con.commit()

if mode == 'create':
    cursObj.execute("INSERT INTO manufacter VALUES (0, 'DEG')")
    cursObj.execute("INSERT INTO manufacter VALUES (1, 'GED')")
    cursObj.execute("INSERT INTO manufacter VALUES (2, 'TEST')")
    cursObj.execute("INSERT INTO manufacter VALUES (3, 'Balgenos')")
    con.commit()

    cursObj.execute("INSERT INTO products VALUES (0, 15, 'crack', 0)")
    cursObj.execute("INSERT INTO products VALUES (1, 3, 'Elbrus', 0)")
    cursObj.execute("INSERT INTO products VALUES (2, 16, 'foo', 1)")
    cursObj.execute("INSERT INTO products VALUES (3, 32, 'bar', 2)")
    cursObj.execute("INSERT INTO products VALUES (4, 1002, 'Elbrus', 3)")
    cursObj.execute("INSERT INTO products VALUES (5, 0, 'chair', 3)")
    con.commit()
elif mode == 'selects':
    cpu = ('Elbrus',)
    cursObj.execute("SELECT * FROM products WHERE cpu=?", cpu)
    print(cursObj.fetchall())

con.close()
