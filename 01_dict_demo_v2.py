my_dict = {
    "blue": "sky", 
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

your_num = int(input("Enter a number: "))
print()
to_do = input("double or half? ").lower()
print()

# look up value
multiply_by = my_dict[to_do]

# do math!
answer = your_num * multiply_by
print("{} x {} = {}".format(your_num, multiply_by, answer))