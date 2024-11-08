# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = [ "kiwi" , "peach", "pineapple", "pear", "apricot"]
# TODO: Add a fruit to the end of the list
fruits.append("apple")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "grape")


# TODO: Remove a fruit from the list
fruits.remove ("pineapple")

# TODO: Print the modified list

print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
list1 = [1 , 2, 3 ,4, 5, 6]
# TODO: Create a new list with each number squared
list2 = [1, 4, 9, 25, 36]
# TODO: Find the sum and average of the original numbers
print(sum(list1))


average = sum(list1) / len(list1)
print(average)


# TODO: Print the results


#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals= {
    "South Africa": "Pretoria",
    "Zimbabwe":"Harare",
    "Japan": "Tokyo"
}
# TODO: Add a new country-capital pair
countries_capitals["Lesotho"] ="Maseru"

# TODO: Update the capital of an existing country
countries_capitals["South Africa"]= "Cape Town"
print(countries_capitals["South Africa"])

# TODO: Remove a country-capital pair
del countries_capitals["Japan"]

# TODO: Print the modified dictionary
print(countries_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors={'apple': 'green',
              'pineapple': 'yellow',
              'grape': 'purple'
}

# TODO: Print all the fruits (keys)
for fruit in fruit_colors:
    print(fruit)
print(fruit_colors.keys())

# TODO: Print all the colors (values)
print(fruit_colors.values())

# TODO: Print each fruit and its color
print(fruit_colors)

# TODO: Check if a fruit is in the dictionary and print its color
key = fruit_colors.keys()
values = fruit_colors.get("pineapple")
print(values)