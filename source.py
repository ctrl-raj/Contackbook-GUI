#Contactbook GUI Code
import tkinter as tk # for GUI
from PIL import ImageTk # for logo widget
import pyglet # for fonts
import csv # for content management
from tabulate import tabulate

# fonts 
pyglet.font.add_file("./AbrilFatface-Regular.ttf")
pyglet.font.add_file("./RobotoMono-Regular.ttf")

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
    clear_widgets(frame2)
    clear_widgets(frame3)
    clear_widgets(frame4)

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
        command=lambda: frame2_addnew()  # calls load_frame2() [lambda->when clicked]
    ).pack(pady=10)

    # add contacts button
    tk.Button(
        frame1,
        text="View All Contacts",
        font=("Abril Fatface", 16, "bold"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: (view_contacts(),frame4_allcontacts())  # calls load_frame2() [lambda->when clicked]
    ).pack(pady=10)

    # edit contacts button
    tk.Button(
        frame1,
        text="Edit Contacts",
        font=("Abril Fatface", 16, "bold"),
        bg=pink,
        fg=dpurple,
        cursor="hand2",
        activebackground=lpurple,
        activeforeground=dpurple,
        command=lambda: frame2_addnew()  # calls load_frame2() [lambda->when clicked]
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
    clear_widgets(frame1)

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
        command=lambda: (add_new(name=name_entry.get(), phone=phone_entry.get()), frame3_saved()),
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
        command=lambda: (frame1_index(),),
    ).pack(pady=10)

# Saved new contact screen
def frame3_saved():
        frame3.tkraise()
        clear_widgets(frame2)

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
        command=lambda: (frame1_index(),)
    ).pack(pady=10)

# view all contacts 
def frame4_allcontacts():
    frame4.tkraise()
    clear_widgets(frame1)

    tk.Label(
            frame4,
            text="All Saved Contacts:",
            bg=beige,
            fg=dpurple,
            font=("Abril Fatface", 20)
            ).pack(pady=20)
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
        command=lambda: (frame1_index())
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


# initialize app
root = tk.Tk()
root.title("Contactbook") # gives a name to the window
root.eval("tk::PlaceWindow . center")

# create frame widgets
frame1 = tk.Frame(root, width=500, height=600, bg=beige)
frame2 = tk.Frame(root, bg=beige)
frame3 = tk.Frame(root, bg=beige)
frame4 = tk.Frame(root, bg=beige)


for frame in (frame1, frame2, frame3, frame4):
	frame.grid(row=0, column=0, sticky="nesw")
	
frame1_index() # calls frame1 in the start

# run the app window
root.mainloop()