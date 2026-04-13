from connect import connect

conn = connect()
cur = conn.cursor()


def search_pattern():
    pattern = input("Enter search pattern: ")

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    results = cur.fetchall()

    for row in results:
        print(row)


def insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()

    print("Done")


def get_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    results = cur.fetchall()

    for row in results:
        print(row)


def delete_user():
    value = input("Enter name or phone: ")

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    print("Deleted")


def show_all():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)


def menu():
    while True:
        print("\nPHONEBOOK (Functions & Procedures)")
        print("1. Search (function)")
        print("2. Insert or Update (procedure)")
        print("3. Pagination (function)")
        print("4. Delete (procedure)")
        print("5. Show all")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search_pattern()
        elif choice == "2":
            insert_or_update()
        elif choice == "3":
            get_paginated()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            show_all()
        elif choice == "0":
            break


menu()

cur.close()
conn.close()