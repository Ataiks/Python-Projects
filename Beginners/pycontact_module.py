#Define an empty dictionary to store contact information as a global variable
contacts={}

#Define a function 'menu' to welcome the user and provide options on how the phonebook works
def menu():
    #Use a try except block inside the function to take care of possible wrong responses by the user
    #Define a variable 'entry' for user options
    try:
        entry =int(input("""Welcome to Py Contact Book.  
                    >>>Py Contact Book commands are: 1,2,3 or 4 <<<
                    >>>What would you like to do?<<<
                    1. Display Your existing contacts
                    2. Create a New contact
                    3. Check an entry 
                    4. Delete an entry
                    5. Exit
                    Enter (1,2,3,4) or enter [5] to exit:  """))

    #For the except block, use a valueerror exception
    #in the exception block re-define the variable 'entry', letting the users aware of what type of inputs should be in there
    except ValueError:
        entry=int(input('Wrong entry! Enter a number [1-5]'))
    #Include decision making processes using the control flow statements
    #This flow control statement will call other functions defined beneath
    if entry ==1:
        #Function for displaying contact
        DisplayAll()
    elif entry==2:
        #Function for adding contact details
        AddContact()
    elif entry==3:
        #Function for viewing contact
        ViewContact()
    elif entry ==4:
        #Function for deleting contact
        DelContact()
    else:
        #Closing statement
        print('\n\b Thanks for using the Py Contact Book')
 
