#Contactbook GUI Code
import tkinter as tk # for GUI
from tkinter import * # for logo
from PIL import ImageTk # for logo widget
import pyglet # for fonts
import csv # for content management
from tabulate import tabulate

# fonts 
pyglet.font.add_file("./Assets/AbrilFatface-Regular.ttf")
pyglet.font.add_file("./Assets/RobotoMono-Regular.ttf")

#Colours
violet = "#7F55B1"
dpurple = "#7F55B1"
lpurple = "#9B7EBD"
pink = "#F49BAB"
beige = "#FFE1E0"


# frames

# index screen
def frame1_index():
    frame1.tkraise()
    frame1.pack_propagate(False) #doesn't allow to propagate influence of one element

    #logo widget
    logo_img = ImageTk.PhotoImage(file="./Assets/logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack()

    # other elements in frame1
	# label widget for program name
    tk.Label(
        frame1, #it is part of frame1
        text="Contactbook CLI",
        bg=beige,
        fg=dpurple,
        font=("Abril Fatface", 20)
        ).pack(pady=20)

    # add contacts button
    tk.Button(
        frame1,
        text="Add Contact",
        font=("Abril Fatface", 16, "bold"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame1), frame2_addnew())  # calls load_frame2() [lambda->when clicked]
    ).pack(pady=10)

    # view all contacts button
    tk.Button(
        frame1,
        text="View All Contacts",
        font=("Abril Fatface", 16, "bold"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame1), view_contacts(),frame4_allcontacts())  # calls load_frame2() [lambda->when clicked]
    ).pack(pady=10)

    # edit contacts button
    tk.Button(
        frame1,
        text="Search Contacts",
        font=("Abril Fatface", 16, "bold"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame1), frame5_search())  # calls load_frame2() [lambda->when clicked]
    ).pack(pady=10)
	
        # Close button
    tk.Button(
        frame1,
        text="Exit",
        font=("Abril Fatface", 12, "bold italic"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: root.destroy()
    ).pack(pady=10)

# add contacts screen
def frame2_addnew():
    frame2.tkraise()

    #logo widget
    logo_img = ImageTk.PhotoImage(file="./Assets/logo.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack()

    global name_entry
    global phone_entry
    global new_contact_added
    new_contact_added = False

    # program label
    tk.Label(
        frame2, #it is part of frame1
        text="Contactbook CLI",
        bg=beige,
        fg=dpurple,
        font=("Abril Fatface", 20)
        ).pack(pady=20)

    # Enter-name label
    tk.Label(
        frame2,
        text="Enter Name",
        bg=beige,
        fg=violet,
        font=("Roboto Mono", 12),
    ).pack(fill="both")

    # Name entry widget (store actual widget)
    name_entry = tk.Entry(frame2, width=40)
    name_entry.pack(pady=15)

    # Enter-phone label
    tk.Label(
        frame2,
        text="Enter Phone",
        bg=beige,
        fg=violet,
        font=("Roboto Mono", 12),
    ).pack(fill="both")

    # Phone entry widget (store actual widget)
    phone_entry = tk.Entry(frame2, width=40)
    phone_entry.pack(pady=15)
	
    # save button
    tk.Button(
        frame2,
        text="Save",
        font=("Abril Fatface", 16, "bold"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame2), add_new(name=name_entry.get(), phone=phone_entry.get()), frame3_saved()),
    ).pack(pady=10)

    # Back button
    tk.Button(
        frame2,
        text="Back",
        font=("Abril Fatface", 12, "bold italic"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame2), frame1_index(),),
    ).pack(pady=10)

# Saved new contact screen
def frame3_saved():
        frame3.tkraise()

        #logo widget
        logo_img = ImageTk.PhotoImage(file="./Assets/logo.png")
        logo_widget = tk.Label(frame3, image=logo_img, bg=beige)
        logo_widget.image = logo_img  # Already done but it is needed
        logo_widget.pack()
        

        # program label
        tk.Label(
        frame3,
        text="Contactbook CLI",
        bg=beige,
        fg=dpurple,
        font=("Abril Fatface", 20)
        ).pack(pady=20)

        # new contact saved or not
        tk.Label(
        frame3,
        text=frame3text,
        bg=beige,
        fg=dpurple,
        font=("Abril Fatface", 20)
        ).pack(pady=20)

        # Back button
        tk.Button(
        frame3,
        text="Back",
        font=("Abril Fatface", 12, "bold italic"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame3), frame1_index(),)
    ).pack(pady=10)

# view all contacts 
def frame4_allcontacts():
    frame4.tkraise()

    #logo widget
    logo_img = ImageTk.PhotoImage(file="./Assets/logo.png")
    logo_widget = tk.Label(frame4, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack()

    # all saved cont label
    tk.Label(
            frame4,
            text="All Saved Contacts:",
            bg=beige,
            fg=dpurple,
            font=("Abril Fatface", 20)
            ).pack(pady=20)
    
    # text display for contacts
    all_contacts = tk.Text(
            frame4,
            wrap="word",
            width=35,
            height=10,
            bg=violet,
            fg=beige,
            font=("Roboto Mono", 12, "bold")
      )
    all_contacts.pack(pady=10)
      
    all_contacts.config(state="normal")
    all_contacts.delete("1.0","end")
    all_contacts.insert("1.0", content)
    all_contacts.config(state="disabled")

    # Back button
    tk.Button(
        frame4,
        text="Back",
        font=("Abril Fatface", 12, "bold italic"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame4), frame1_index())
    ).pack(pady=10)

# search contacts
def frame5_search():
    frame5.tkraise()
    global search_entry

    #logo widget
    logo_img = ImageTk.PhotoImage(file="./Assets/logo.png")
    logo_widget = tk.Label(frame5, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack()

    # label widget for program name
    tk.Label(
        frame5,
        text="Contactbook CLI",
        bg=beige,
        fg=dpurple,
        font=("Abril Fatface", 20)
        ).pack(pady=20)
    
    # search label
    tk.Label(
        frame5,
        text="Enter Name",
        bg=beige,
        fg=violet,
        font=("Roboto Mono", 12),
    ).pack(fill="both")

    # search word entry
    search_entry = tk.Entry(frame5, width=40)
    search_entry.pack(pady=15)

    # search button
    tk.Button(
        frame5,
        text="Search",
        font=("Abril Fatface", 16, "bold"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (handle_search())).pack(pady=10)
    
    # Back button
    tk.Button(
        frame5,
        text="Back",
        font=("Abril Fatface", 12, "bold italic"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame5), frame1_index(),),
    ).pack(pady=10)

# search results
def frame6_search_res():
    frame6.tkraise()

    #logo widget
    logo_img = ImageTk.PhotoImage(file="./Assets/logo.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack()

    # label widget for program name
    tk.Label(
        frame6,
        text="Contactbook CLI",
        bg=beige,
        fg=dpurple,
        font=("Abril Fatface", 20)
        ).pack(pady=20)
    
    # results label
    tk.Label(
            frame6,
            text=f"Search Results: ",
            bg=beige,
            fg=dpurple,
            font=("Abril Fatface", 20)
            ).pack(pady=20)
    
    # search results
    all_contacts = tk.Text(
            frame6,
            wrap="word",
            width=35,
            height=10,
            bg=violet,
            fg=beige,
            font=("Roboto Mono", 12, "bold")
      )
    all_contacts.pack(pady=10)
      
    all_contacts.config(state="normal")
    all_contacts.delete("1.0","end")
    all_contacts.insert("1.0", search_content)
    all_contacts.config(state="disabled")

    # Back button
    tk.Button(
        frame6,
        text="Back",
        font=("Abril Fatface", 12, "bold italic"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (clear_widgets(frame6), frame1_index(),),
    ).pack(pady=10)

#--- FUNCTIONS---

# clear widgets from previous screen
def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

# add new contacts function 
def add_new(name, phone):
    global frame3text
    if name == "" or phone == "":
         frame3text = f"Name or Phone cannot be empty!"
    with open('database.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name.title(), phone])
        new_contact_added = True

    # text of frame 3
    if new_contact_added:
          frame3text = f"New contact '{name.strip().title()}' was saved\nIn ConatactBook-Database.txt"
    else:
          frame3text = f"Sorry! \nsomething wrong happened"

# view all contacts
def view_contacts():
    global content
    with open("database.csv", "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            content = tabulate(rows, headers="keys", tablefmt="grid")
    return content

# handle search
def handle_search():
     search_word = search_entry.get()
     clear_widgets(frame5)
     search_contact(search_word)
     frame6_search_res()

# search function
def search_contact(search_word):
    global search_content
    with open("database.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader) 
        contacts = rows
        found = []
        for contact in contacts:
             if search_word.title() in contact.get('Name'):
                  found.append(contact)
        if found :
             search_content = tabulate(found, headers='keys', tablefmt='grid')
        else :
             search_content = f"Sorry! the searched contact was not found in saved contacts"
        return search_content

# initialize app
root = tk.Tk()
root.title("Contactbook") # gives a name to the window
root.eval("tk::PlaceWindow . center")

# create frame widgets
frame1 = tk.Frame(root, width=500, height=600, bg=beige)
frame2 = tk.Frame(root, bg=beige)
frame3 = tk.Frame(root, bg=beige)
frame4 = tk.Frame(root, bg=beige)
frame5 = tk.Frame(root, bg=beige)
frame6 = tk.Frame(root, bg=beige)


for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
	frame.grid(row=0, column=0, sticky="nesw")

# logo for the window
logo = PhotoImage(file = './Assets/logo.png')
# Setting icon of root window
root.iconphoto(False, logo)
	
frame1_index() # calls frame1 in the start

# run the app window
root.mainloop()