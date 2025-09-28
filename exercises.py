"""
Exercise definitions for the Python practice platform
"""

def get_exercises():
    """Return all exercises organized by category"""
    return {
        "beginner": [
            {
                "id": "hello_world",
                "title": "Hello World",
                "difficulty": "beginner",
                "description": """
Write a program that prints "Hello, World!" to the console.

This is the traditional first program in any programming language!
                """,
                "starter_code": "# Write your code here\n",
                "example": 'print("Hello, World!")',
                "test_cases": [
                    {
                        "test": "import sys\nfrom io import StringIO\nold_stdout = sys.stdout\nsys.stdout = mystdout = StringIO()\nexec(compile(open(__file__).read(), __file__, 'exec'))\nsys.stdout = old_stdout\nprint(mystdout.getvalue().strip())",
                        "expected": "Hello, World!"
                    }
                ]
            },
            {
                "id": "variables_basic",
                "title": "Working with Variables",
                "difficulty": "beginner",
                "description": """
Create variables for the following:
- A string variable `name` with your name
- An integer variable `age` with your age
- A float variable `height` with your height in meters

Then print each variable on a separate line.
                """,
                "starter_code": "# Create your variables here\nname = \nage = \nheight = \n\n# Print them here\n",
                "hint": "Use print() function to display each variable. Example: print(name)",
                "test_cases": [
                    {
                        "test": "assert isinstance(name, str), 'name should be a string'\nassert isinstance(age, int), 'age should be an integer'\nassert isinstance(height, float), 'height should be a float'",
                        "expected": ""
                    }
                ]
            },
            {
                "id": "basic_math",
                "title": "Basic Mathematics",
                "difficulty": "beginner",
                "description": """
Write a program that:
1. Creates two variables: `a = 10` and `b = 3`
2. Calculates and prints the sum, difference, product, and quotient
3. Each calculation should be on a separate line

Format: "Sum: [result]", "Difference: [result]", etc.
                """,
                "starter_code": "a = 10\nb = 3\n\n# Calculate and print the results\n",
                "example": """a = 10
b = 3
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")""",
                "test_cases": [
                    {
                        "test": "expected_output = 'Sum: 13\\nDifference: 7\\nProduct: 30\\nQuotient: 3.3333333333333335'",
                        "expected": "Sum: 13\nDifference: 7\nProduct: 30\nQuotient: 3.3333333333333335"
                    }
                ]
            },
            {
                "id": "string_operations",
                "title": "String Operations",
                "difficulty": "beginner",
                "description": """
Create a program that:
1. Takes a string: `message = "Python Programming"`
2. Prints the length of the string
3. Prints the string in uppercase
4. Prints the string in lowercase
5. Prints whether the word "Python" is in the message

Format each output clearly.
                """,
                "starter_code": "message = \"Python Programming\"\n\n# Your code here\n",
                "hint": "Use len(), .upper(), .lower(), and the 'in' operator",
                "test_cases": [
                    {
                        "test": "assert 'Length:' in output or '18' in output",
                        "expected": "Length: 18\nPYTHON PROGRAMMING\npython programming\nTrue"
                    }
                ]
            },
            {
                "id": "simple_if_else",
                "title": "Simple If-Else",
                "difficulty": "beginner",
                "description": """
Write a program that:
1. Creates a variable `number = 15`
2. Checks if the number is even or odd
3. Prints "Even" if the number is even, "Odd" if it's odd

Hint: Use the modulo operator (%) to check if a number is divisible by 2.
                """,
                "starter_code": "number = 15\n\n# Your if-else logic here\n",
                "example": """number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")""",
                "test_cases": [
                    {
                        "test": "# Test with number = 15\nassert output.strip() == 'Odd'",
                        "expected": "Odd"
                    }
                ]
            },
            {
                "id": "simple_loop",
                "title": "Simple For Loop",
                "difficulty": "beginner",
                "description": """
Write a program that:
1. Uses a for loop to print numbers from 1 to 10
2. Each number should be on a separate line

This introduces you to loops, one of the most important concepts in programming!
                """,
                "starter_code": "# Write your for loop here\n",
                "example": """for i in range(1, 11):
    print(i)""",
                "hint": "Use range(1, 11) to get numbers from 1 to 10",
                "test_cases": [
                    {
                        "test": "expected_lines = [str(i) for i in range(1, 11)]\nactual_lines = output.strip().split('\\n')\nassert actual_lines == expected_lines",
                        "expected": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
                    }
                ]
            }
        ],
        "intermediate": [
            {
                "id": "list_operations",
                "title": "List Operations",
                "difficulty": "intermediate",
                "description": """
Create a program that:
1. Creates a list: `numbers = [1, 2, 3, 4, 5]`
2. Adds the number 6 to the end of the list
3. Inserts the number 0 at the beginning of the list
4. Prints the final list
5. Prints the sum of all numbers in the list

This exercise teaches you about Python lists and their methods.
                """,
                "starter_code": "numbers = [1, 2, 3, 4, 5]\n\n# Your code here\n",
                "hint": "Use .append() to add to the end, .insert() to add at a position, and sum() to calculate the total",
                "test_cases": [
                    {
                        "test": "# Check if the list operations are correct\nassert 0 in numbers and 6 in numbers",
                        "expected": "[0, 1, 2, 3, 4, 5, 6]\n21"
                    }
                ]
            },
            {
                "id": "dictionary_basics",
                "title": "Dictionary Basics",
                "difficulty": "intermediate",
                "description": """
Create a program that:
1. Creates a dictionary representing a student: `student = {"name": "Alice", "age": 20, "grade": "A"}`
2. Adds a new key "school" with value "Python University"
3. Updates the grade to "A+"
4. Prints all keys in the dictionary
5. Prints all values in the dictionary
6. Prints the complete dictionary

This introduces you to dictionaries, a key data structure in Python.
                """,
                "starter_code": "student = {\"name\": \"Alice\", \"age\": 20, \"grade\": \"A\"}\n\n# Your code here\n",
                "example": """student = {"name": "Alice", "age": 20}
student["school"] = "Python University"
student["age"] = 21
print(student.keys())
print(student.values())
print(student)""",
                "test_cases": [
                    {
                        "test": "assert 'school' in student and student['grade'] == 'A+'",
                        "expected": "dict_keys(['name', 'age', 'grade', 'school'])"
                    }
                ]
            },
            {
                "id": "function_basics",
                "title": "Function Basics",
                "difficulty": "intermediate",
                "description": """
Create a function called `calculate_area` that:
1. Takes two parameters: `length` and `width`
2. Returns the area (length × width)
3. Call the function with length=5 and width=3
4. Print the result

Functions help you organize code and make it reusable!
                """,
                "starter_code": "# Define your function here\ndef calculate_area():\n    pass\n\n# Call your function and print the result\n",
                "example": """def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)""",
                "hint": "Remember to use 'return' to send back the calculated value",
                "test_cases": [
                    {
                        "test": "result = calculate_area(5, 3)\nassert result == 15",
                        "expected": "15"
                    }
                ]
            },
            {
                "id": "loop_with_condition",
                "title": "Loop with Condition",
                "difficulty": "intermediate",
                "description": """
Write a program that:
1. Uses a for loop to iterate through numbers 1 to 20
2. Prints only the even numbers
3. For each even number, also print if it's divisible by 4

Example output format:
"2 is even"
"4 is even and divisible by 4"
"6 is even"
                """,
                "starter_code": "# Your loop with conditions here\nfor i in range(1, 21):\n    # Add your logic here\n    pass\n",
                "hint": "Use % operator to check divisibility. if i % 2 == 0 checks for even numbers",
                "test_cases": [
                    {
                        "test": "# Check if output contains even numbers\nassert '2 is even' in output and '4 is even and divisible by 4' in output",
                        "expected": "Contains even numbers and divisibility checks"
                    }
                ]
            },
            {
                "id": "list_comprehension",
                "title": "List Comprehension",
                "difficulty": "intermediate",
                "description": """
Use list comprehension to create the following lists:

1. `squares`: A list of squares of numbers from 1 to 10
2. `even_squares`: A list of squares of only even numbers from 1 to 10
3. Print both lists

List comprehension is a powerful Python feature that makes code more concise!
                """,
                "starter_code": "# Create squares list using list comprehension\nsquares = \n\n# Create even_squares list using list comprehension\neven_squares = \n\n# Print both lists\n",
                "example": """# List comprehension examples
numbers = [x for x in range(1, 6)]  # [1, 2, 3, 4, 5]
doubled = [x * 2 for x in range(1, 6)]  # [2, 4, 6, 8, 10]
evens = [x for x in range(1, 11) if x % 2 == 0]  # [2, 4, 6, 8, 10]""",
                "hint": "Use [expression for item in range(...)] and add 'if condition' for filtering",
                "test_cases": [
                    {
                        "test": "assert len(squares) == 10 and squares[0] == 1 and squares[9] == 100\nassert len(even_squares) == 5 and 4 in even_squares",
                        "expected": "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n[4, 16, 36, 64, 100]"
                    }
                ]
            },
            {
                "id": "error_handling",
                "title": "Error Handling",
                "difficulty": "intermediate",
                "description": """
Write a program that:
1. Asks the user to imagine they input a number (use `user_input = "42"` for testing)
2. Tries to convert it to an integer and divide 100 by that number
3. Uses try-except to handle potential errors (like division by zero or invalid input)
4. Prints the result if successful, or an appropriate error message if not

This teaches you how to handle errors gracefully in your programs.
                """,
                "starter_code": "user_input = \"42\"  # Simulate user input\n\n# Your try-except code here\ntry:\n    # Conversion and calculation\n    pass\nexcept:\n    # Error handling\n    pass\n",
                "example": """try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")""",
                "hint": "Use int() to convert string to integer, and handle ValueError and ZeroDivisionError",
                "test_cases": [
                    {
                        "test": "# Test with valid input\nassert 'Result:' in output or '2.38' in output",
                        "expected": "Result: 2.380952380952381"
                    }
                ]
            }
        ]
    }

def get_exercise_by_id(exercise_id):
    """Get a specific exercise by its ID"""
    exercises = get_exercises()
    for category in exercises.values():
        for exercise in category:
            if exercise['id'] == exercise_id:
                return exercise
    return None

def get_all_exercise_ids():
    """Get all exercise IDs"""
    exercises = get_exercises()
    ids = []
    for category in exercises.values():
        for exercise in category:
            ids.append(exercise['id'])
    return ids
