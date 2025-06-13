# This exercise is about variables and data types in Python.
# You will be given a series of tasks to complete, each focusing on a different aspect of variables and data types.
# Follow the instructions carefully and make sure to test your code after each task.
# We are working on a program for ordering food online.

# Level 1 tasks
def level_1_task_1():
    # Task 1: Create a variable called 'bread' and assign it a bread type as a string. 
    # You can choose any type of bread you like. Examples are "sourdough", "ciabatta", or "baguette".
    bread = None  # Replace with the bread type you want
    # Then print the variable to the console and the type of the variable.
    # print(_)
    
def level_1_task_2():
    # Task 2: Create a variable called 'calories' and assign it an amount of calories as an integer.
    # You can choose any number you like. Examples are 200, 500, or 1000.
    calories = None  # Replace with the amount of calories you want the bread to have
    # Then print the variable to the console and the type of the variable.
    # print(_)
    
def level_1_task_3():
    # Task 3: Create two variables, one called 'height' and one called 'width', and assign the height and width of the bread in centimeters as a float, respectively.
    # You can choose any realistic numbers you like. Examples are 5.5, 7.3, or 10.0.
    height = None  # Replace with your bread height in centimeters
    width = None  # Replace with bread width in centimeters
    # Then print the variables to the console and the type of each variable.
    # print(_)
    
def level_1_task_4():
    # Task 4: Create a variable called 'is_available' and assign it a boolean value indicating whether the type of bread is available or not.
    # We will assume the bread is available for this exercise, so set it to True.
    is_available = None  # Change to True to indicate the bread is available for sale
    # Then print the variable to the console and the type of the variable.
    # print(_)
    
def level_1_task_5():
    # Task 5: Calculate the price of the bread based on its height and width.
    # Assume the price is calculated as (height * width) / 10.0.
    height = 10.0  # Example height in centimeters
    width = 5.5 # Example width in centimeters
    price_of_bread = None  # Replace with the formula to calculate the price of the bread
    # Then print the price to the console and the type of the variable.
    # print(_)

# Level 2 tasks
# In this section, we will create a list of ingredients for the bread.

def level_2_task_1():
    # Task 1: Convert the price from a string to an integer.
    # Assume the price is given as a string, e.g., "5".
    price_str = "3"  # Example string price
    price_int = None  # Replace with the conversion to integer
    # Then print the variable price_int to the console and the type of the variable.
    # print(_)

def level_2_task_2():
    # Task 2: Update the value of the price, so that it includes a VAT of 10%
    price = 10  # Example price
    # Calculate the price with VAT
    price_with_vat = price + None  # Replace with the formula to calculate the price with VAT
    # Then print the variable to the console and the type of the variable.
    # print(_)



if __name__ == "__main__":
    # Call the tasks function to execute them
    level_1_task_1()
    level_1_task_2()
    level_1_task_3()
    level_1_task_4()
    level_1_task_5()
    # Call the level 2 tasks
    level_2_task_1()
    level_2_task_2()