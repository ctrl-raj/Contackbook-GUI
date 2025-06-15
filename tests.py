# codes writen here are only for testing purposes only

import csv

search_word = "leo"

def edit_contacts(search_word):
    with open("database.csv", "r", newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        contacts = rows

    with open("database.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone"])

        for contact in contacts:
            if search_word.title() in contact.get("Name"):
                edited_input = input('"Name", "Phone": ')
                edited_details = edited_input.split(",")
                edited_name = edited_details[0].title()
                edited_phone = edited_details[1]
                writer.writerow([edited_name, edited_phone])
            else:
                writer.writerow([contact.get("Name"), contact.get("Phone")])

edit_contacts(search_word)