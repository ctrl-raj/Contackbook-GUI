# ContactBook GUI

A simple and elegant contact management system built with Python's tkinter. This app lets you add new contacts, view saved entries, and manage your contact list — all saved locally in a CSV file.

## 📌 Features

- ✅ Add new contacts with name and phone number

- 📄 View all saved contacts in a tabular format

- ✏ Edit a saved contact via search function

- 💾 Data saved persistently in database.csv

- 🔎 Search saved contacts

- 🎨 Stylish GUI using custom fonts and colors

- 🚪 Exit and navigation buttons for smooth workflow

## 🖼️ Interface Preview

    Frame 1: Home screen with buttons to add, view, search, or edit contacts

    Frame 2: Input form for adding a new contact

    Frame 3: Confirmation screen for successful save

    Frame 4: Display all contacts in a scrollable text widget

    Frame 5: Input name to search in saved contacts

    Frame 6: Display search results based on search

    Frame 7: Edit contact window

    Frame 8: Display result of Editing of a contact

## 📁 File Structure

    project-folder/
    │
    ├── source.py                     # Main application script
    ├── database.csv                  # Stores contact records
    ├── Assets
        ├── AbrilFatface-Regular.ttf  # Custom font used in GUI
        ├── RobotoMono-Regular.ttf    # Custom font used in GUI
        ├── logo.png                  # Custom logo used in GUI
    ├── Legecy_Contactbook            # Old Contactbook files
        ├── ContactBook CLI.py
        ├── ContactBook-Database

## 🚀 Getting Started
1. Clone or download this repo:

git clone https://github.com/yourusername/contactbook-gui.git
cd contactbook-gui

2. Install required Python packages:

pip install pillow tabulate pyglet

3. Run the app:

python ContactBook.py

- Ensure you have Python 3 installed. If not, install it from python.org.

## 💾 Data Format

All contacts are stored in a simple database.csv file:

    Name,Phone
    John Doe,1234567890
    Jane Smith,9876543210

## 📦 Dependencies

    tkinter – Standard Python GUI toolkit

    pillow – For handling images and icons (used via ImageTk)

    pyglet – For adding custom fonts

    tabulate – For formatting contact list display

    csv – Built-in module for file management

## ⚠️ Known Limitations

    No input validation for names or phone numbers yet.

    No duplicate check or contact deletion feature.

## 📌 To-Do / Future Improvements

- ✅ Add contact

- ✅ View contacts

- ✅ Edit & Delete contacts

- ✅ Search functionality

- ✅ Sorting by name or phone

## 🧑‍💻 Author

Ramkrishna Raj Sinha
A passionate Python learner building tools to level up development skills.

    “Code is poetry that runs.”

