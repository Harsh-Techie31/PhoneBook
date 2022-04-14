from tkinter import *
import sqlite3

root = Tk()
root.title("Address Book")
root.geometry("310x550")

c = sqlite3.connect("K:\\Pythonnn\\Tkinter-2\\address.db")

# creating cursor
p = c.cursor()

# creating the data

# p.execute("""CREATE TABLE  addresses(
#     first_name text,
#     last_name text ,
#     addresses text,
#     state text,
#     zipcode integers
#     )""")

# commiting the changes that we do
c.commit()

# closing the datatbases
c.close()

# fucntions
# 1.Submit

def submit():
    c = sqlite3.connect(
        "K:\\Pythonnn\\Tkinter-2\\address.db")
    p = c.cursor()

    p.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:state,:zipcode)",
              {
                  'f_name': f_name_entry.get(),
                  'l_name': l_name_entry.get(),
                  'address': address_entry.get(),
                  'state': state_entry.get(),
                  'zipcode': zipcode_entry.get()
              })

    c.commit()
    c.close()

    f_name_entry.delete(0, END)
    l_name_entry.delete(0, END)
    address_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

# 2.showing records

def show():
    global query_label , names
    c = sqlite3.connect(
        "K:\\Pythonnn\\Tkinter-2\\address.db")
    p = c.cursor()

    p.execute("SELECT *,oid FROM addresses")
    records = p.fetchall()
    records_list = ''
    for item in records:
        records_list += f"{item[0].capitalize()} {item[1].capitalize()}  {item[5]}\n\n"
   
    query_label = Label(root, text=records_list)
    query_label.grid(row=7, column=0,columnspan=2)

    c.commit()
    c.close()

# 3.Delete records
def delete():

    c = sqlite3.connect(
        "K:\\Pythonnn\\Tkinter-2\\address.db")
    p = c.cursor()

    c.execute(f"DELETE from addresses WHERE oid = {us_box.get()}")
    c.execute(f"DELETE from addresses WHERE oid = {us_box.get()}")
    query_label.grid_forget()

    c.commit()
    c.close()   

#.updating the record
def update():
    c = sqlite3.connect(
        "K:\\Pythonnn\\Tkinter-2\\address.db")
    p = c.cursor()

    p.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        addresses = :city,
        city = :states,
        zipcode = :code

        WHERE oid = :oid""",
        
        {'first' :f_name_entry_editor.get(),
        'last':l_name_entry_editor.get(),
        'city':address_entry_editor.get(),
        'states':state_entry_editor.get(),
        'code':zipcode_entry_editor.get(),
        'oid': ed_box.get()
        })
    edity.destroy()
    c.commit()
    c.close()
    


#4.edit records
def edit():
    global edity
    edity = Tk()
    edity.title("Update a record")
    edity.geometry("308x260")

    f_name_editor = Label(edity, text="First name :", font=("ubuntu", 15)).grid(row=0, column=0, sticky=W, pady=(15, 0))
    l_name_editor = Label(edity, text="Last name :", font=("ubuntu", 15)).grid(row=1, column=0, sticky=W)
    address_editor = Label(edity, text="City :", font=("ubuntu", 15)).grid(row=2, column=0, sticky=W)
    state_editor = Label(edity, text="State :", font=("ubuntu", 15)).grid(row=3, column=0, sticky=W)
    zipcode_editor = Label(edity, text="Zipcode :", font=("ubuntu", 15)).grid(row=4, column=0, sticky=W)

    # us_la = Label(root, text="Select ID:").grid(row=8, column=0)

    # making entry boxes
    global f_name_entry_editor,l_name_entry_editor,address_entry_editor,state_entry_editor,zipcode_entry_editor
    f_name_entry_editor = Entry(edity, width=15 , font=("ubuntu", 16))
    f_name_entry_editor.grid(row=0, column=1, pady=(15, 0))
    l_name_entry_editor = Entry(edity, width=15, font=("ubuntu", 16))
    l_name_entry_editor.grid(row=1, column=1,pady=(2, 0))
    address_entry_editor = Entry(edity, width=15, font=("ubuntu", 16))
    address_entry_editor.grid(row=2, column=1,pady=(2, 0))
    state_entry_editor = Entry(edity, width=15, font=("ubuntu", 16))
    state_entry_editor.grid(row=3, column=1,pady=(2, 0))
    zipcode_entry_editor = Entry(edity, width=15, font=("ubuntu", 16))
    zipcode_entry_editor.grid(row=4, column=1,pady=(2, 0))

    save = Button(edity, text="Save", font=("Saab", 20), command=update).grid(
    row=5, ipadx=110, columnspan=2, pady=(30, 0))

    c = sqlite3.connect(
        "K:\\Pythonnn\\Tkinter-2\\address.db")
    p = c.cursor()
    p.execute(f"SELECT * FROM addresses WHERE oid = {ed_box.get()}")
    records = p.fetchall()
    for record in records:
        f_name_entry_editor.insert(0 , str(record[0].capitalize()))
        l_name_entry_editor.insert(0 , str(record[1].capitalize()))
        address_entry_editor.insert(0 , str(record[2]))
        state_entry_editor.insert(0 , str(record[3]))
        zipcode_entry_editor.insert(0 , str(record[4]))


    c.commit()
    c.close()

#detailed records
def details():
    more = Tk()
    more.title("More Details")
    more.geometry("308x260")

    c = sqlite3.connect(
         "K:\\Pythonnn\\Tkinter-2\\address.db")
    p = c.cursor()

    

    Label(more, text="First name :", font=("ubuntu", 15)).grid(row=0, column=0, sticky=W, pady=(15, 0))
    Label(more, text="Last name :", font=("ubuntu", 15)).grid(row=1, column=0, sticky=W)
    Label(more, text="City :", font=("ubuntu", 15)).grid(row=2, column=0, sticky=W)
    Label(more, text="State :", font=("ubuntu", 15)).grid(row=3, column=0, sticky=W)
    Label(more, text="Zipcode :", font=("ubuntu", 15)).grid(row=4, column=0, sticky=W)
    p.execute(f"SELECT * FROM addresses WHERE oid = {md_box.get()}")
    records = p.fetchall()
    for record in records:
        f_name_a = str(record[0].capitalize())
        l_name_a = str(record[1].capitalize())
        address_a = str(record[2])
        state_a = str(record[3])
        zipcode_a = str(record[4])
    
    Label(more,text=f"{f_name_a}" , font=("ubuntu", 16)).grid(row=0, column=1, pady=(15, 0))
    Label(more,text=f"{l_name_a}", font=("ubuntu", 16)).grid(row=1, column=1,pady=(2, 0))
    Label(more,text=f"{address_a}",font=("ubuntu", 16)).grid(row=2, column=1,pady=(2, 0))
    Label(more,text=f"{state_a}", font=("ubuntu", 16)).grid(row=3, column=1,pady=(2, 0))
    Label(more,text=f"{zipcode_a}", font=("ubuntu", 16)).grid(row=4, column=1,pady=(2, 0))

    c.commit()
    c.close()

# making labels
f_name = Label(root, text="First name :", font=("ubuntu", 15)).grid(row=0, column=0, sticky=W, pady=(15, 0))
l_name = Label(root, text="Last name :", font=("ubuntu", 15)).grid(row=1, column=0, sticky=W)
address = Label(root, text="City :", font=("ubuntu", 15)).grid(row=2, column=0, sticky=W)
state = Label(root, text="State :", font=("ubuntu", 15)).grid(row=3, column=0, sticky=W)
zipcode = Label(root, text="Zipcode :", font=("ubuntu", 15)).grid(row=4, column=0, sticky=W)
#delete label
us_la = Label(root, text="Delete ID:").grid(row=8, column=0)
#edit label
ed_la = Label(root, text="Edit ID:").grid(row=10, column=0)
#details Label
md_la = Label(root, text="Enter ID:").grid(row=12, column=0)


# making entry boxes

f_name_entry = Entry(root, width=15 , font=("ubuntu", 16))
f_name_entry.grid(row=0, column=1, pady=(15, 0))
l_name_entry = Entry(root, width=15, font=("ubuntu", 16))
l_name_entry.grid(row=1, column=1,pady=(2, 0))
address_entry = Entry(root, width=15, font=("ubuntu", 16))
address_entry.grid(row=2, column=1,pady=(2, 0))
state_entry = Entry(root, width=15, font=("ubuntu", 16))
state_entry.grid(row=3, column=1,pady=(2, 0))
zipcode_entry = Entry(root, width=15, font=("ubuntu", 16))
zipcode_entry.grid(row=4, column=1,pady=(2, 0))

#delete entrey
us_box = Entry(root, width=15)
us_box.grid(row=8, column=1)
#edit entry
ed_box = Entry(root,width=15)
ed_box.grid(row=10, column=1)
#details entry
md_box = Entry(root,width=15)
md_box.grid(row=12, column=1)




# making button

sub = Button(root, text="Submit", font=("Saab", 20), command=submit).grid(
    row=5, ipadx=90, columnspan=2, pady=(30, 0))

show1 = Button(root, text="Show Records", font=("Saab", 20), command=show).grid(
    row=6, column=0, columnspan=2, ipadx=43)

de = Button(root, text="Delete a user", font=("Saab", 20), command=delete).grid(
    row=9, column=0, ipadx=50, columnspan=2)

us = Button(root, text="Edit a user", font=("Saab", 20), command=edit).grid(
    row=11, column=0, ipadx=65, columnspan=2)

md = Button(root, text="Detailed Records", font=("Saab", 20), command=details).grid(
    row=13, column=0, ipadx=26, columnspan=2)
mainloop()
