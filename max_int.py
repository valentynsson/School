'''
Maximum number
Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.
 
Make sure that you write up the algorithm before starting to code.
Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.
 
During the design of your algorithm and your implementation, you should use git:
Initialize a local directory with git init.
Write the text of your algorithm in a file called max_int.py
Inspect the result of git status
Use git add . to move changes to the staging area.
Commit your changes with git commit -m “Algorithm written for max_int”
Then start implementing your algorithm
During your implementation, make sure you do git status, git add, and git commit regularly.
You can see a log of all your commits with git log.
When you have finished your implementation:
Create an account on github.com (if you don't already have it).
Create a public repository on github
Follow the instructions (that appear on github when you have created a new repository) under "push an existing repository from the command line"  (see also here)
Push your changes to the remote repo with: git push
Inspect your commits on github

'''


# user_input_str varible that holds user input
user_input_str = input("Please enter the number: ")

# user_value_int variable will be converted and hold the user input
user_value_int = int(user_input_str)

# total variable will hold the maximum positive integer input by a user. 
total_int = 0

# if user_value is positive integer while loop will start and ask user to input another value, if it will be not positive program will stop and show maximum positive integer.
if user_value_int >= 0: 
    
    
    total_int = user_value_int

    while user_value_int >= 0:
        
        user_value_int = int(input("Please enter the number: "))
        
        if user_value_int >= 0:

            if user_value_int >=  total_int:

                total_int = user_value_int         
           

print("Mmaximum positive integer is: ", total_int)