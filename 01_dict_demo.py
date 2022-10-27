my_dict = {
    "blue": "sky", 
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

# list to make testing faster
to_check = ["red", "salad", "apple", "blue"]

for item in to_check:

    # check if it's a key (ie: a colour in our dictionary)
    if item in my_dict:
        print("{} is a key in the dictonary".format(item))

        # look up the value associated with the key
        coloured_object = my_dict[item]

        # output the value and the key (eg: the sky is blue)
        print("The {} is {}".format(coloured_object, item))