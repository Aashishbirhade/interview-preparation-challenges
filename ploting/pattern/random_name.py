# import random

# # List with 10 names
# names = [
#     "Aashish", "Rohit", "Priya", "Sneha", "Vikram",
#     "Anjali", "Rahul", "Kiran", "Meena", "Arjun"
# ]

# # Pick a random name
# random_name = random.choice(names)

# print("Randomly selected name:", random_name)


import random

names = [
    "Aashish", "Rohit", "Priya", "Sneha", "Vikram",
    "Anjali", "Rahul", "Kiran", "Meena", "Arjun"
]

# Pick 3 random names without repetition
random_names = random.sample(names, 3)

print("Randomly selected names:", random_names)
