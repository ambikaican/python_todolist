
import sys
import Tkinter
import tkMessageBox
import sqlite3

#sqlite Connect function for insert, update and delete

def sql_insert(name, desc, pri, eta, status):
    
    print name, desc, pri, eta, status
    ret=0
    try:
        conn= sqlite3.connect("todo.db")
        conn.execute('''INSERT INTO TODO_TABLE(NAME, DESC, PRIORITY, ETA, STATUS)
            VALUES(?, ?, ?, ? , ?);''', (name, desc, pri, eta, status) )
        conn.commit()
        print 'Table insert successfully'
    except:
        err = "Please enter unique TODO name"
        tkMessageBox.showerror("Error", err)
        conn.close()
        ret=1
        
    finally:   
        conn.close()
        return ret



#called from entry_update - EDIT button call
def sql_update(name, desc, pri, eta, status):
    
    conn=sqlite3.connect("todo.db")
    conn.execute('''UPDATE TODO_TABLE SET DESC = ?,
        PRIORITY = ?,ETA = ?, STATUS = ? where NAME = (?);''',
                (desc, pri, eta, status, name) )
    conn.commit()
    conn.close()


#SQL and helper function for the DELETE button
def entry_delete():
    global entry
    global top
    
    conn= sqlite3.connect("todo.db")
    conn.execute('''Delete from TODO_TABLE where NAME = (?);''', (entry.get(),))
    conn.commit()
    conn.close()
    #Re launch the window
    main_destroy()
    top = Tkinter.Tk()
    main_fn()






#Helper Functions 
def priority_status_read_conversion(pri, st):
    if(pri==1):
        priority_read='Low'
    elif (pri ==2):
        priority_read='Medium'
    else:
        priority_read='High'

    if(st ==1):
        status_read = 'Due'
    elif (st==2):
        status_read = 'In progress'
    else:
        status_read = 'Completed'
    #print priority_read, status_read
    return priority_read, status_read



        
#sets in the header frame in the window
def heading_row():
    global top    
    head_i=0 
    label = Label(top, text="TO DO Item",relief=GROOVE, bg='gray97', 
                  justify=CENTER, width=20).grid(column=head_i, row=1)
    head_i = head_i + 1
    
    label = Label(top, text="Description",relief=GROOVE, bg='gray97', 
                  justify=CENTER, width=20).grid(column=head_i, row=1)
    head_i = head_i + 1
    label = Label(top, text="Priority",relief=GROOVE, bg='gray97', 
                  justify=CENTER, width=20).grid(column=head_i, row=1)
    head_i = head_i + 1
    label = Label(top, text="ETA",relief=GROOVE, bg='gray97', 
                  justify=CENTER, width=20).grid(column=head_i, row=1)
    head_i = head_i + 1
    label = Label(top, text="Status",relief=GROOVE, bg='gray97', 
                  justify=CENTER, width=20).grid(column=head_i, row=1)
    head_i = head_i + 1



#Sql read filling in the entries
def fill_values():
    global name_list

    conn= sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute('''SELECT * from TODO_TABLE;''')
    rows = cur.fetchall()
    i=2 # Row after after the Heading line
    #name_list = [" "]
    if (rows == []):
        name_list = [" "]
    for row in rows:
        #print('{0} | {1} | {2} | {3}'.format (row [0], row[1], row[2], row[3]))
        j=0
        col=0
        if (i == 2):
            name_list = [row[0]]
        else:
            name_list.append(row[0])
        pri, st = priority_status_read_conversion(row[2], row[4])
        for j in range(0,5):
            if (j == 2):
                 var = pri
            elif (j == 4):
                var = st
            else:
                var = row[j]
            label = Label(top, text=var, width=20).grid(column=col, row=i)
            col = col + 1
        i = i+1
    return i
    print 'Table read successfully'
    print name_list
    conn.close()
    


#Bottom Line in the window - called during Add, Edit or delete
#Toggle variable acts the switch for the purpose
# Toggle -  0- Main screen/ADD
#           1 - For EDIT/DELETE option
#           2 - for ITEM select
def input_label(toggle, i, enter_val):
  
    global entry
    global describe
    global priority
    global eta
    global status
    global top
    global name_list

#Label creation
#entry name
    if (toggle == 2):
        import sqlite3
        conn= sqlite3.connect("todo.db")
        cur = conn.cursor()
        cur.execute('''SELECT * from TODO_TABLE where NAME=(?);''',
                        (enter_val,) )
        rows = cur.fetchall()
        for row in rows:
            print('{0} | {1} | {2} | {3} | {4}'.format (row [0],
                                        row[1], row[2], row[3], row[4]))
    col=0
    entry=StringVar()
    if (toggle == 0):
        txt = Entry(top, textvariable=entry, width=20)
        txt.grid(column=col, row=i)
    elif (toggle == 1):
        combo = OptionMenu(top, entry, *name_list, command=set_selected)   
        combo.grid(column=col, row=i)
        combo.config(width=20)
    else:
        combo = OptionMenu(top, entry, *name_list, command=set_selected)
        entry.set(enter_val)
        combo.grid(column=col, row=i)
        combo.config(width=20)
    col=col+1
#decription        
    describe=StringVar()
    if (toggle == 2):
        describe.set(row[1])

       
    txt = Entry(top, textvariable=describe, width=20)
    txt.grid(column=col, row=i)
    col=col+1
    priority=StringVar()
 
# Priority with options
    choices = { 'Low', 'Medium', 'High'}
    if (toggle == 2):
        temp = row[2]
        if (temp == 1):
            priority.set('Low')
        elif (temp == 2):
            priority.set('Medium')
        else:
            priority.set('High')
    else:
        priority.set('Medium') # set the default option
 
    popupMenu = OptionMenu(top, priority, *choices)

    popupMenu.grid(row = i, column =col)
    col=col+1
#ETA
    eta=StringVar()
    if (toggle == 2):
         eta.set(row[3])
    txt = Entry(top, textvariable=eta, width=20)
    txt.grid(column=col, row=i)
    col=col+1

# Status with options
    status=StringVar()
    choices = { 'Due', 'In progress', 'Completed' }
    if (toggle == 2):
        temp = row[4];
        if (temp == 1):
            status.set('Due')
        elif (temp == 2):
            status.set('In progress')
        else:
            status.set('Completed')
    else:
        status.set('Due') # set the default option
 
    popupMenu = OptionMenu(top, status, *choices)
    popupMenu.grid(row = i, column =col)
    col=col+1


#To close the window
def main_destroy():
    global top
    top.destroy()



#The main Window flow
def main_fn():
    global entry
    global describe
    global priority
    global eta
    global status
    global top
    
    #from Tkinter import *
    top.title("To-DO Manager")
    top.geometry('800x480')
                   
    scrollbar = Scrollbar(top, orient=VERTICAL, width=100)
    

    heading_row()
    row_var = fill_values()
    input_label(0, row_var, " ")

    toggle_var = 0

    btn = Button(top, text="Add", width=20, textvariable=toggle_var, command=entry_write)
    btn.grid(column=2, row=row_var+10)

    btn = Button(top, text="Edit/Delete", width=20, command=edit_delete_page)
    btn.grid(column=2, row=row_var+20)
    top.mainloop()
    

#Callback function for Add functionality
def entry_write():
    global entry
    global describe
    global priority
    global eta
    global status
    global top
    global row_var
    global name_list
    #print entry.get()
    print "SUCCESS"
    if (len(entry.get()) == 0):
        err="Please enter the To Do item name"
        
        tkMessageBox.showerror("Error", err)
        #print len(entry.get()), "Error\n"
        return #TODO
    # To accomdate empty fields. Default settings
    if (len(eta.get()) == 0):
        eta.set("5 days")

    if(len(describe.get()) == 0):
        describe.set("To Do")
    
    #priority and status conversion 
    pri = 0
    st = 0
    if(priority.get()== 'Low'):
        pri = 1
    elif (priority.get() == 'Medium'):
        pri = 2
    else:
        pri = 3
    if(status.get() == 'Due'):
        st = 1
    elif (status.get() == 'In progress'):
        st = 2
    else:
        st = 3
    #Add entry into Sql table
    ret = sql_insert(entry.get(), describe.get(), pri, eta.get(), st)
    print ret
    if (ret == 1):
        print "Captured"
        return
    #Re launch the window
    main_destroy()
    top = Tkinter.Tk()
    main_fn()

    


#Callback function for Edit/Delete in main page
def edit_delete_page():
    global top
    global row_var
    main_destroy()
    
    top = Tkinter.Tk()
    top.title("To-DO List")
    top.geometry('800x480')
    heading_row()
    row_var = fill_values()
    input_label(1, row_var, " ")
    btn = Button(top, text="Edit", width=20, command=entry_update)
    btn.grid(column=2, row=row_var+10)

    btn = Button(top, text="Delete", width=20, command=entry_delete)
    btn.grid(column=2, row=row_var+20)

    top.mainloop()
    


#callback function for Edit button in Edit/delete page
def entry_update():
    global entry
    global describe
    global priority
    global eta
    global status
    global top
    global row_var
    
    
    # To accomdate empty fields. Default settings
    if (len(eta.get()) == 0):
        eta.set("5 days")

    if(len(describe.get()) == 0):
        describe.set("To Do")
    
    #priority and status conversion 
    pri = 0
    st = 0
    if(priority.get()== 'Low'):
        pri = 1
    elif (priority.get() == 'Medium'):
        pri = 2
    else:
        pri = 3
    if(status.get() == 'Due'):
        st = 1
    elif (status.get() == 'In progress'):
        st = 2
    else:
        st = 3
    #Edit entry into Sql table
    sql_update(entry.get(), describe.get(), pri, eta.get(), st)
    #Re launch the window
    main_destroy()
    top = Tkinter.Tk()
    main_fn()




#callback function for Item name Combo Box in Edit/delete page

def set_selected(entry):
    global row_var
    print("select function")
    print row_var
    input_label(2, row_var, entry) 

#Program flow  starts here
print("start")
from Tkinter import *
    
top = Tkinter.Tk()
main_fn()
print("Closed")





















