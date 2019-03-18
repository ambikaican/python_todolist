"TdM 1.0" is an application that was built to manage the To-Do Items 

This application is built in Python 2.7 programming language with the SQL lite DB backend. It runs in Windows 10 Home Edition (2018)

Features in the application helps to Add a new To-Do Item and to Edit or Delete an existing To-Do Item(excluding the TO DO item name)


Following are the data/field available in the application to track the To Do item details:

* To-Do Item 
* Description
* Priority
* ETA
* Status


To Do Item name to be added should be an Unique value and it is a mandatory field. All other fields are optional and if not provided default value will be stored
To Do Item, Description and ETA are Free form text boxes. 
ETA can be used to store data/time in any format as it is free form text box. (e.g) 5 days, 09/26/2004, 32 mins etc
Options provided for Priority are High, Medium and Low
Options provided for Status are Due, In Progress and Completed

As a next step, TdM version can be enhanced by integrating it with mail box server to assign based on the email ID and to have a To-Do created in User's Calendar


Deliverable
-------------


sql_setup.py  - contains the initial setup for sql tables(and few pre-loaded TO DO items)
todo app.py   - The main file which generates the tkinter window.

Both the files takes no inputs. 
Python needs tkinter, sqlite3 installed 


P.S: I used Python IDLE GUI to run the module. 
