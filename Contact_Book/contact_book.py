import mysql.connector
from tkinter import *
from tkinter import messagebox

#Connecting mysql
def connect_to_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "anhad",
        database = "contact_book"
    )
    
def add_contact(name, number, email, address):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO contacts (name, number, email, address) VALUES (%s, %s, %s, %s)", (name, number, email, address))
    db.commit()
    db.close()
    
def get_contacts():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    db.close()
    return contacts

def find_contact(name):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    contact = cursor.fetchone()
    db.close()
    return contact

def remove_contact(name):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM contacts WHERE name = %s", (name,))
    db.commit()
    db.close()
    
    
#Setting up the GUI

#Defining the functions
def add_contact_gui():
    name = entry_name.get()
    number = entry_number.get()
    email = entry_email.get()
    address = entry_address.get()
    add_contact(name, number, email, address)
    messagebox.showinfo("Contact Book", "Contact added successfully")
    entry_name.delete(0, END)
    entry_number.delete(0, END)
    entry_email.delete(0, END)
    entry_address.delete(0, END)
    display_contacts()
    
def display_contacts():
    contacts  = get_contacts()
    listbox_contacts.delete(0,END)
    for contact in contacts:
        listbox_contacts.insert(END, contact)

def find_contact_gui():
    name = entry_name.get()
    contact = find_contact(name)
    listbox_contacts.delete(0, END)
    if contact:
        listbox_contacts.insert(END, contact)
    else:
        messagebox.showinfo("Contact Book", "Contact not found")
    
def remove_contact_gui():
    name = entry_name.get()
    remove_contact(name)
    messagebox.showinfo("Contact Book", "Contact removed successfully")
    display_contacts()
    
    
#Window
app = Tk()
app.title("Contact Book")


#Labels and entries
Label(app, text = "Name").grid(row = 0, column = 0)
entry_name = Entry(app)
entry_name.grid(row = 0, column = 1)

Label(app, text = 'Number').grid(row = 1, column = 0)
entry_number = Entry(app)
entry_number.grid(row = 1, column=1)

Label(app, text='Email').grid(row=2, column=0)
entry_email = Entry(app)
entry_email.grid(row=2, column=1)

Label(app, text='Address').grid(row=3, column=0)
entry_address = Entry(app)
entry_address.grid(row=3, column=1)

Button(app, text='Add Contact', command=add_contact_gui).grid(row = 4, column=0)
Button(app, text='Find Contact', command=find_contact_gui).grid(row = 4, column=1)
Button(app, text='Remove Contact', command=remove_contact_gui).grid(row=4, column=2)

#Listbox to display all contacts
listbox_contacts = Listbox(app)
listbox_contacts.grid(row=5, column=0, columnspan=3)

#Display all contacts initially
display_contacts()

app.mainloop()