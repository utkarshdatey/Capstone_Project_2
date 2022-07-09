# Capstone Project 2 *** TO DO LIST***

# Empty list for storing the data
bi_list = []

# Parent Class
class to_do:
    
    # __init__() Function for assign values
    def __init__(self,bi):
        self.bi = bi

    # Funtion to create/append the task in TO DO List
    def create_List(b_list): 
        
        # Take input for how many task user want in TO DO List
        t = int(input("Please enter the no. of task you want to insert :-> \n")) 
        # User enter thier today task
        print("\nPlease enter the today task in list :-> \n") 
        
        # Loop for taking no. of input task from user
        for i in range(0,t):
            # Take single input as task from user
            k = input()
            # Update/Append the task in TO DO List
            bi_list.append(k) 

    # Function to print list on promte
    def show_list():
        print("\nHere is your today task :-> \n")
        # Loop to print the TO DO List in user understand able formate
        for i in range(len(bi_list)):
            print(i+1,"->",bi_list[i])

    # Function to update the Task in the created TO DO List
    def up_list():
        t = input("\nEnter the task you want to add :-> \n\n")
        # Update/Append the task in TO DO List
        bi_list.append(t)

# Child class inherit the function from the Parent Class to_do
class ine_todo(to_do):
    # __init__() Function for assign values
    def __init__(self,d):
        self.d = d

    # Function to show the list, calling the parent class show_list() function
    def show():
        to_do.show_list()

    # Function to delete the task from TO Do List
    def re_de():
        # Take input as task to delete from list
        t = input("Enter the task you want to delete :-> ")

        # Exception Handling, if entered task is not present in TO DO List then it raise exception and print msg on prompt
        try:
            if t in bi_list:
                bi_list.remove(t)
            else:
                raise Exception
        except Exception:
            print("\nEntered task is not present in list\n")

# Program Execution Starting From Here            
print("\n")
print("*"*10," WELCOME TO YOUR TO_DO LIST ","*"*10)
print("\n\nPlease selcet the option of your choice\n")

# Funtion to print navigation menu
def menu1():
    print("1. Create Today TO_DO List\n")
    print("2. Want To Check Your TO_DO List\n")
    print("3. Want To Add Task in TO_DO List \n")
    print("4. Want To Delete The Task in TO_DO List\n")
    print("Enter Your Option Here :\n")

# Function to print navigation menu after to creating the TO DO List and performing listed option
def menu2():
    print("\n","*"*40,"\n")
    print("1. Want To Check Your TO_DO List\n")
    print("2. Want To Add Task in TO_DO List \n")
    print("3. Want To Delete The Task in TO_DO List\n")
    print("0. Want To Exit")
    print("\nEnter Your Option Here :-> \n")

# Calling navigation menu function
menu1()
# Take input from the listed menu
usr_in = int(input())

# Exception Handling, on fresh start TO DO List is empty as no opration perform except updating the task in it.
try:
    # If input value is 1 the code proceed furhter, other than 1 raise error
    if(usr_in > 1):
        raise ValueError
    # For taking input as 1
    elif(usr_in == 1):
        # Updating the empty list
        print("\nCreating Today TO_DO list : \n")
        # Parent class to_do object
        L1 = to_do
        # Child class ine_todo object
        L2 = ine_todo
        # Calling Function to update the empty list from to_do class
        L1.create_List(bi_list)
        print("\nYour TO_DO List is Created, Thank You!\n")

        # Loop for performing opertaion on created list
        while(usr_in != 0):
            # Calling the navigation menu for peforming opertaion on TO DO List
            menu2()
            # Take input from menu
            usr_in = int(input())

            # Perfrom Operation after taking input
            # For print list
            if(usr_in == 1):
                # Calling and print the ine_todo class function which inherit the parent class to_do function
                print(L2.show())
                # Update the value for next interation
                usr_in += 1
            # For update the task in list    
            elif(usr_in == 2):
                # Calling the to_do class function to update the task in TO DO List
                L1.up_list()
                # Calling and print the ine_todo class function which inherit the parent class to_do function
                print(L2.show())
                # Update the value for next interation
                usr_in += 1
            # For delete the task from list
            elif(usr_in == 3):
                # Calling the child class function to delete the task from list
                L2.re_de()
                # Update the value for next interation
                usr_in -= 1
except ValueError:
    print("\nSorry! enter option is under devlopment\n")