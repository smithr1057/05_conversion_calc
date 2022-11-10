from time import sleep
# Functions go here

def statement_generator(text, decoration):

    # Make string with five characters 
    ends = decoration * 5

    # add decoration to start and end of statement 
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a unit to convert from and a unit to convert to")
    print()
    print("This program converts measurments of time, mass, and distance")
    print()
    print("Complete as many calculaations as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""


# checks input is a number more than given value
def num_check(question):
    # Check that users enter a number that is more than zero
    valid = False
    while not valid:
        print()
        error = "please enter an integer that is more than zero"

        try:
        
            low_num = 1
            
            # Ask user to enter a number
            response = int(input(question))
            
            # checks number is more than zero or under 200
            if low_num <= response:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)


# Checks user coice is 'weight', 'distance' or 'time'
def user_choice():

    valid = False
    while not valid:
        
        # ask user for choice and change response to lowercase
        response = input("measurement (weight / distance / time): ").lower()

        # if they choose "t" or "text" or "txt", return "text"
        weight_ok = ["weight", "w", "wt"]
        if response in weight_ok:
            return "weight"

         # if they choose "int" or "interger", return "interger"
        distance_ok = ["distance", "length", "d", "dist"]
        if response in distance_ok:
            return "distance"

         # if they choose "image" or "p" or "img", return "image"
        time_ok = ["time", "t"]
        if response in time_ok:
            return "time"


        else: 
            print("Please choose a valid measurment!")
            print()

def ask_num():

    user_num = input("Please enter the integer (more than zero) you want to convert: ")
    
    


def weight_conv():
    
    # Ask user what to convert from and to

    weight_from = input("Enter unit to convert from (mg, g, kg, t): ")
    weight_to = input("Enter unit to convert to (mg, g, kg, t): ")

        


def distance_conv():

    pass


def time_conv():

    pass


# Main Routine goes here

# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "*")

# Display instructions if user has not used the progra before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()
# Loop to allow multiple calulations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

     # For integers, ask for integer
        # (must be an integer more than / equal to 0)
    if data_type =="weight":
        weight_conv()
    
    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type =="distance":
        distance_conv()

    # For text, ask for a string
    else:
        time_conv()