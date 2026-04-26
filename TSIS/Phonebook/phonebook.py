from connect import connect
import json


conn = connect()
cur = conn.cursor()



def filter_by_group():
    group = input("Enter group: ")

    cur.execute("""
        SELECT pb.name, pb.email
        FROM phonebook pb
        JOIN groups g ON pb.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    results = cur.fetchall()

    if not results:
        print("[INFO] No contacts found in this group")
        return

    print("\n--- Group Results ---")
    for row in results:
        print(f"Name: {row[0]} | Email: {row[1] or 'N/A'}")



def search_email():
    email = input("Enter email: ")

    cur.execute("""
        SELECT * FROM phonebook
        WHERE email ILIKE %s
    """, ('%' + email + '%',))

    results = cur.fetchall()

    if not results:
        print("[INFO] No results found")
        return

    print("\n--- Email Results ---")
    for row in results:
        print(row)



def sort_contacts():
    field = input("Sort by (name/birthday): ")

    if field not in ["name", "birthday"]:
        print("[ERROR] Invalid field")
        return

    cur.execute(f"SELECT * FROM phonebook ORDER BY {field}")

    print("\n--- Sorted Contacts ---")
    for row in cur.fetchall():
        print(row)



def paginate():
    offset = 0
    limit = 3

    while True:
        cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()

        if not rows:
            print("[INFO] No more data")
            break

        print("\n--- Page ---")
        for row in rows:
            print(row)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break



def export_json():
    cur.execute("SELECT * FROM phonebook")
    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f)

    print("[OK] Exported to contacts.json")



def import_json():
    try:
        with open("contacts.json", "r") as f:
            data = json.load(f)
    except:
        print("[ERROR] File not found")
        return

    for row in data:
        name = row[1]

        cur.execute("SELECT * FROM phonebook WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")

            if choice == "skip":
                continue

            cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))

        cur.execute(
            "INSERT INTO phonebook(name, email, birthday) VALUES (%s, %s, %s)",
            (row[1], row[2], row[3])
        )

    conn.commit()
    print("[OK] JSON imported")



def add_phone():
    name = input("Enter contact name: ")
    phone = input("Enter phone: ")
    type_ = input("Enter type (home/work/mobile): ")

    try:
        cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, type_))
        conn.commit()
        print(f"[OK] Phone added to {name}")
    except Exception as e:
        print("[ERROR]", e)



def move_group():
    name = input("Enter contact name: ")
    group = input("Enter new group: ")

    try:
        cur.execute("CALL move_to_group(%s, %s)", (name, group))
        conn.commit()
        print(f"[OK] {name} moved to {group}")
    except Exception as e:
        print("[ERROR]", e)



def search_all():
    query = input("Enter search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (query,))
    results = cur.fetchall()

    if not results:
        print("[INFO] No results")
        return

    print("\n--- Results ---")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3] or 'N/A'}")



def menu():
    while True:
        print("\nPHONEBOOK TSIS")
        print("1. Filter by group")
        print("2. Search by email")
        print("3. Sort")
        print("4. Pagination")
        print("5. Export JSON")
        print("6. Import JSON")
        print("7. Add phone")
        print("8. Move to group")
        print("9. Search all")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            filter_by_group()
        elif choice == "2":
            search_email()
        elif choice == "3":
            sort_contacts()
        elif choice == "4":
            paginate()
        elif choice == "5":
            export_json()
        elif choice == "6":
            import_json()
        elif choice == "7":
            add_phone()
        elif choice == "8":
            move_group()
        elif choice == "9":
            search_all()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice")


menu()

cur.close()
conn.close()