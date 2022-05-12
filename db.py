import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    # BEFORE 1.0 #
    # entry_content = input("What have you learned today?")
    # entry_date = input("Enter the date: ")

    # 1.1
    # entries.append({"content": entry_content, "date": entry_date})

    #1.3
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
        )




def get_entries():
    # BEFORE 1.0 #
    # for entry in entries:
        # print(f"{entry['date']}\n{entry['content']}\n\n") #string interpolation f"{}"

    # 1.1
    # return entries

    # 1.2
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor