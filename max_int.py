# user_input_str varible that holds user input
# user_value_int variable will be converted and hold the user input
# total variable will hold the maximum positive integer input by a user. 
# if user_value is positive integer,  while loop will start and ask user to input another value, if it will be not positive program will stop and show maximum positive integer.


user_input_str = input("Please enter the number: ")
user_value_int = int(user_input_str)
total_int = 0


if user_value_int >= 0: 
    
    total_int = user_value_int

    while user_value_int >= 0:
        
        user_value_int = int(input("Please enter the number: "))
        
        if user_value_int >= 0:

            if user_value_int >=  total_int:

                total_int = user_value_int         
           

print("Mmaximum positive integer is: ", total_int)