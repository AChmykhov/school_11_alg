import sqlite3

con = sqlite3.connect('./dataset/first_test.db')
cursObj = con.cursor()

cursObj.executescript('''CREATE TABLE if not exists manufacter (
                id integer PRIMARY KEY AUTOINCREMENT, name text
                )''')
con.commit()

cursObj.executescript('''CREATE TABLE if not exists products (
                id integer PRIMARY KEY AUTOINCREMENT, 
                ram integer, 
                cpu text, 
                vendor_id integer, 
                price integer, 
                FOREIGN KEY (vendor_id) 
                    REFERENCES manufacter (id) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
                )''')
cursObj.executescript('''CREATE TABLE if not exists users (
                id integer PRIMARY KEY AUTOINCREMENT,
                username text
                )''')
cursObj.executescript('''CREATE TABLE if not exists orders (
                id integer PRIMARY KEY AUTOINCREMENT,
                item_id integer,
                user_id integer,
                FOREIGN KEY (item_id) 
                    REFERENCES products (id) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION,
                FOREIGN KEY (user_id) 
                    REFERENCES users (id) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
                )''')
con.commit()

mode = input()

if mode == 'create':
    cursObj.execute("INSERT INTO manufacter ('name') VALUES ('DEG')")
    cursObj.execute("INSERT INTO manufacter ('name') VALUES ('GED')")
    cursObj.execute("INSERT INTO manufacter ('name') VALUES ('TEST')")
    cursObj.execute("INSERT INTO manufacter ('name') VALUES ('Balgenos')")
    con.commit()

    cursObj.execute("INSERT INTO products (ram, cpu, vendor_id, price) VALUES (15, 'crack', 1, 1500)")
    cursObj.execute("INSERT INTO products (ram, cpu, vendor_id, price) VALUES (3, 'Elbrus', 1, 100)")
    cursObj.execute("INSERT INTO products (ram, cpu, vendor_id, price) VALUES (16, 'foo', 2, 80000)")
    cursObj.execute("INSERT INTO products (ram, cpu, vendor_id, price) VALUES (32, 'bar', 3, 5)")
    cursObj.execute("INSERT INTO products (ram, cpu, vendor_id, price) VALUES (1002, 'Elbrus', 4, 1200)")
    cursObj.execute("INSERT INTO products (ram, cpu, vendor_id, price) VALUES (0, 'chair', 3, 17)")
    cursObj.execute("INSERT INTO products (ram, cpu, vendor_id, price) VALUES (500, 'Crack', 4, 9800)")
    con.commit()
elif mode == 'selects':
    cpu = ('Elbrus',)
    cursObj.execute("SELECT * FROM products WHERE cpu=?", cpu)
    print(cursObj.fetchall())
elif mode == 'create2':
    cursObj.execute("INSERT INTO users (username) VALUES ('Katya')")
    cursObj.execute("INSERT INTO users (username) VALUES ('Vanya')")
    cursObj.execute("INSERT INTO users (username) VALUES ('Maria')")
    cursObj.execute("INSERT INTO users (username) VALUES ('Rosa')")
    cursObj.execute("INSERT INTO users (username) VALUES ('Yager')")
    con.commit()

    cursObj.execute("INSERT INTO orders (item_id, user_id) VALUES (1, 3)")
    cursObj.execute("INSERT INTO orders (item_id, user_id) VALUES (2, 3)")
    cursObj.execute("INSERT INTO orders (item_id, user_id) VALUES (6, 3)")
    cursObj.execute("INSERT INTO orders (item_id, user_id) VALUES (3, 4)")
    cursObj.execute("INSERT INTO orders (item_id, user_id) VALUES (5, 4)")
    cursObj.execute("INSERT INTO orders (item_id, user_id) VALUES (4, 2)")
    con.commit()
elif mode == "join_test":
    user = ('Rosa',)
    cursObj.execute('''SELECT * FROM orders
                            JOIN products p on p.id = orders.item_id
                            JOIN users u on u.id = orders.user_id
                            WHERE username=?
                            ''', user)
    print(cursObj.fetchall())
elif mode == "left_join":
    user = ('Yager',)
    cursObj.execute('''SELECT * FROM users
                            LEFT JOIN orders o on users.id = o.user_id
                            LEFT JOIN products p on p.id = o.item_id
                            WHERE username=?
                            ''', user)
    print(cursObj.fetchall())

con.close()
