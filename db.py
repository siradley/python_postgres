entries = []

def add_entry(entry_content, entry_date):
    # BEFORE 1.0 #
    # entry_content = input("What have you learned today?")
    # entry_date = input("Enter the date: ")

    # 1.1
    entries.append({"content": entry_content, "date": entry_date})


def get_entries():
    # BEFORE 1.0 #
    # for entry in entries:
        # print(f"{entry['date']}\n{entry['content']}\n\n") #string interpolation f"{}"

    # 1.1
    return entries