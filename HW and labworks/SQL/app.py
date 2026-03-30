from connect import connect
import csv

conn = connect()
cur = conn.cursor()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Contact added")

def insert_from_csv():
    filename = input("Enter CSV filename: ")
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
        conn.commit()
        print("CSV data inserted")
    except Exception as e:
        print("Error:", e)

def update_contact():
    name = input("Enter contact name: ")
    new_phone = input("Enter new phone: ")
    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE name=%s",
        (new_phone, name)
    )
    conn.commit()
    print("Contact updated")

def search_by_name():
    name = input("Enter name: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        ('%' + name + '%',)
    )
    results = cur.fetchall()
    for row in results:
        print(row)

def search_by_phone():
    prefix = input("Enter phone prefix: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + '%',)
    )
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_contact():
    value = input("Enter name or phone: ")
    cur.execute(
        "DELETE FROM phonebook WHERE name=%s OR phone=%s",
        (value, value)
    )
    conn.commit()
    print("Contact deleted")

def show_all():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

def menu():
    while True:
        print("\nPHONEBOOK")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update contact")
        print("4. Search by name")
        print("5. Search by phone")
        print("6. Delete contact")
        print("7. Show all")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            search_by_phone()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            show_all()
        elif choice == "0":
            break

menu()

cur.close()
conn.close()