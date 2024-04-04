
import random

# Generate random number between 0 and 1
print(random.random())

# Generate random number between 1 and 10
print(random.randint(1,10))

# Generate random floating number between given number
print(random.uniform(3.4,7.5))

# Generate random fruits name in the list
fruits = ['apple','orange','kiwi','banana']
print(random.choice(fruits))

# Shuffle the list
print(fruits)
random.shuffle(fruits)
print(fruits)


