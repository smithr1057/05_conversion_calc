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

first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()
# Loop to allow multiple calulations per session
keep_going = ""
while keep_going == "":