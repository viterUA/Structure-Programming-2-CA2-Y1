#Name: Mykhailo Hnylytskyi T00257938

#First Year Group X

#This program about creating and listing passwords.
#First contain between 8 and 15 characters inclusive
#Second begin with a symbol and end with a symbol. The symbols
#allowed in this case are   £  %  &   *   .  and #
#The first character cannot be the same as the last character
#Password contain only letters (uppercase and lowercase), digits and
#values from the following set of symbols   £  %  &   *   .  and #
#Password must be at least 1 uppercase letter,
#1 lowercase letter, 2 digits and 2 symbols in the password
#It will be illegal to have three consecutive
#characters all with the same values e.g. the substring “777” or “AAA” would be illegal,
#but the substring “AaA” would be legal – note that you will need a loop for this part

from tkinter import simpledialog, messagebox

validList = ""

password = simpledialog.askstring("Input", "Please enter a password value(return to exit)")

while(password != ""):

    valid = False

    lenght = len(password)
    
    while(not valid):

        if (lenght >= 8 and lenght <= 15):

            if (password.startswith("£") or password.startswith("%") or password.startswith("&") or password.startswith("*") or
                password.startswith("#") or password.startswith(".")):

                if (password.endswith("£") or password.endswith("%") or password.endswith("&") or password.endswith("*") or
                    password.endswith("#") or password.endswith(".")):
                   
                    if(password[0]!= password[-1]):

                        validList += str(password)
                        valid = True

                        if(password.isupper() and password.lower() and password.isdigit() and password[0:-1] == "£ % & * . #"):
                    
                            if(len(password.upper() >= 1 and password.lower() >= 1 and password.isdigit() and password[0:-1] == '£' and(password[0:-1] == '%' or password[0:-1] == '&' or password[0:-1] == '*' or password[0:-1] == '.' or password[0:-1] == '#')>=2)):

                                password = simpledialog.askstring("Input", "Please enter another password value(return to exit)")
    
                            else:
                                password = simpledialog.askstring("Invalid", "First and the last character must be different")

                        else:
                     

                            password = simpledialog.askstring("Input", "Invalid! Password must contain at least 1 uppercase letter, 1 lowercase letter and at least 2 digits and 2 symbols")
                        
                else:
                    password = simpledialog.askstring("Input", "Invalid! Password must contain letters, digits, and symbols from the set £ % & * . and #")

            else:
                
                password = simpledialog.askstring("Input", "Invalid! First and last characters must be from one of the symbols £ % & * . and #")
        else:
            
            password = simpledialog.askstring("Input", "Invalid! Password must contain 8 to 15 characters inclusive")


    messagebox.showinfo("Valid Passwords", "The valid password values entered were:\n\n" + str(validList))
        
messagebox.showinfo("Valid passwords", "No valid passwords were entered")
