"""
Exercise definitions for the Python practice platform
"""


def get_exercises():
    """Return all exercises organized by category"""
    return {
        "beginner": [{
            "id":
            "hello_world",
            "title":
            "Hello World",
            "difficulty":
            "beginner",
            "description":
            """
Write a program that prints "Hello, World!" to the console.

This is the traditional first program in any programming language!
                """,
            "starter_code":
            "# Write your code here\n",
            "example":
            'print("Hello, World!")',
            "test_cases": [{
                "test":
                "import sys\nfrom io import StringIO\nold_stdout = sys.stdout\nsys.stdout = mystdout = StringIO()\nexec(compile(open(__file__).read(), __file__, 'exec'))\nsys.stdout = old_stdout\nprint(mystdout.getvalue().strip())",
                "expected": "Hello, World!"
            }]
        }, {
            "id":
            "variables_basic",
            "title":
            "Working with Variables",
            "difficulty":
            "beginner",
            "description":
            """
Create variables for the following:
- A string variable `name` with your name
- An integer variable `age` with your age
- A float variable `height` with your height in meters

Then print each variable on a separate line.
                """,
            "starter_code":
            "# Create your variables here\nname = \nage = \nheight = \n\n# Print them here\n",
            "hint":
            "Use print() function to display each variable. Example: print(name)",
            "test_cases": [{
                "test":
                "assert isinstance(name, str), 'name should be a string'\nassert isinstance(age, int), 'age should be an integer'\nassert isinstance(height, float), 'height should be a float'",
                "expected": ""
            }]
        }, {
            "id":
            "basic_math",
            "title":
            "Basic Mathematics",
            "difficulty":
            "beginner",
            "description":
            """
Write a program that:
1. Creates two variables: `a = 10` and `b = 3`
2. Calculates and prints the sum, difference, product, and quotient
3. Each calculation should be on a separate line

Format: "Sum: [result]", "Difference: [result]", etc.
                """,
            "starter_code":
            "a = 10\nb = 3\n\n# Calculate and print the results\n",
            "example":
            """a = 10
b = 3
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")""",
            "test_cases": [{
                "test":
                "expected_output = 'Sum: 13\\nDifference: 7\\nProduct: 30\\nQuotient: 3.3333333333333335'",
                "expected":
                "Sum: 13\nDifference: 7\nProduct: 30\nQuotient: 3.3333333333333335"
            }]
        }, {
            "id":
            "string_operations",
            "title":
            "String Operations",
            "difficulty":
            "beginner",
            "description":
            """
Create a program that:
1. Takes a string: `message = "Python Programming"`
2. Prints the length of the string
3. Prints the string in uppercase
4. Prints the string in lowercase
5. Prints whether the word "Python" is in the message

Format each output clearly.
                """,
            "starter_code":
            "message = \"Python Programming\"\n\n# Your code here\n",
            "hint":
            "Use len(), .upper(), .lower(), and the 'in' operator",
            "test_cases": [{
                "test":
                "assert 'Length:' in output or '18' in output",
                "expected":
                "Length: 18\nPYTHON PROGRAMMING\npython programming\nTrue"
            }]
        }, {
            "id":
            "simple_if_else",
            "title":
            "Simple If-Else",
            "difficulty":
            "beginner",
            "description":
            """
Write a program that:
1. Creates a variable `number = 15`
2. Checks if the number is even or odd
3. Prints "Even" if the number is even, "Odd" if it's odd

Hint: Use the modulo operator (%) to check if a number is divisible by 2.
                """,
            "starter_code":
            "number = 15\n\n# Your if-else logic here\n",
            "example":
            """number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")""",
            "test_cases": [{
                "test":
                "# Test with number = 15\nassert output.strip() == 'Odd'",
                "expected": "Odd"
            }]
        }, {
            "id":
            "simple_loop",
            "title":
            "Simple For Loop",
            "difficulty":
            "beginner",
            "description":
            """
Write a program that:
1. Uses a for loop to print numbers from 1 to 10
2. Each number should be on a separate line

This introduces you to loops, one of the most important concepts in programming!
                """,
            "starter_code":
            "# Write your for loop here\n",
            "example":
            """for i in range(1, 11):
    print(i)""",
            "hint":
            "Use range(1, 11) to get numbers from 1 to 10",
            "test_cases": [{
                "test":
                "expected_lines = [str(i) for i in range(1, 11)]\nactual_lines = output.strip().split('\\n')\nassert actual_lines == expected_lines",
                "expected": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
            }]
        }],
        "intermediate": [{
            "id":
            "list_operations",
            "title":
            "List Operations",
            "difficulty":
            "intermediate",
            "description":
            """
Create a program that:
1. Creates a list: `numbers = [1, 2, 3, 4, 5]`
2. Adds the number 6 to the end of the list
3. Inserts the number 0 at the beginning of the list
4. Prints the final list
5. Prints the sum of all numbers in the list

This exercise teaches you about Python lists and their methods.
                """,
            "starter_code":
            "numbers = [1, 2, 3, 4, 5]\n\n# Your code here\n",
            "hint":
            "Use .append() to add to the end, .insert() to add at a position, and sum() to calculate the total",
            "test_cases": [{
                "test":
                "# Check if the list operations are correct\nassert 0 in numbers and 6 in numbers",
                "expected": "[0, 1, 2, 3, 4, 5, 6]\n21"
            }]
        }, {
            "id":
            "dictionary_basics",
            "title":
            "Dictionary Basics",
            "difficulty":
            "intermediate",
            "description":
            """
Create a program that:
1. Creates a dictionary representing a student: `student = {"name": "Alice", "age": 20, "grade": "A"}`
2. Adds a new key "school" with value "Python University"
3. Updates the grade to "A+"
4. Prints all keys in the dictionary
5. Prints all values in the dictionary
6. Prints the complete dictionary

This introduces you to dictionaries, a key data structure in Python.
                """,
            "starter_code":
            "student = {\"name\": \"Alice\", \"age\": 20, \"grade\": \"A\"}\n\n# Your code here\n",
            "example":
            """student = {"name": "Alice", "age": 20}
student["school"] = "Python University"
student["age"] = 21
print(student.keys())
print(student.values())
print(student)""",
            "test_cases": [{
                "test":
                "assert 'school' in student and student['grade'] == 'A+'",
                "expected":
                "dict_keys(['name', 'age', 'grade', 'school'])"
            }]
        }, {
            "id":
            "function_basics",
            "title":
            "Function Basics",
            "difficulty":
            "intermediate",
            "description":
            """
Create a function called `calculate_area` that:
1. Takes two parameters: `length` and `width`
2. Returns the area (length × width)
3. Call the function with length=5 and width=3
4. Print the result

Functions help you organize code and make it reusable!
                """,
            "starter_code":
            "# Define your function here\ndef calculate_area():\n    pass\n\n# Call your function and print the result\n",
            "example":
            """def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)""",
            "hint":
            "Remember to use 'return' to send back the calculated value",
            "test_cases": [{
                "test": "result = calculate_area(5, 3)\nassert result == 15",
                "expected": "15"
            }]
        }, {
            "id":
            "loop_with_condition",
            "title":
            "Loop with Condition",
            "difficulty":
            "intermediate",
            "description":
            """
Write a program that:
1. Uses a for loop to iterate through numbers 1 to 20
2. Prints only the even numbers
3. For each even number, also print if it's divisible by 4

Example output format:
"2 is even"
"4 is even and divisible by 4"
"6 is even"
                """,
            "starter_code":
            "# Your loop with conditions here\nfor i in range(1, 21):\n    # Add your logic here\n    pass\n",
            "hint":
            "Use % operator to check divisibility. if i % 2 == 0 checks for even numbers",
            "test_cases": [{
                "test":
                "# Check if output contains even numbers\nassert '2 is even' in output and '4 is even and divisible by 4' in output",
                "expected":
                "Contains even numbers and divisibility checks"
            }]
        }, {
            "id":
            "list_comprehension",
            "title":
            "List Comprehension",
            "difficulty":
            "intermediate",
            "description":
            """
Use list comprehension to create the following lists:

1. `squares`: A list of squares of numbers from 1 to 10
2. `even_squares`: A list of squares of only even numbers from 1 to 10
3. Print both lists

List comprehension is a powerful Python feature that makes code more concise!
                """,
            "starter_code":
            "# Create squares list using list comprehension\nsquares = \n\n# Create even_squares list using list comprehension\neven_squares = \n\n# Print both lists\n",
            "example":
            """# List comprehension examples
numbers = [x for x in range(1, 6)]  # [1, 2, 3, 4, 5]
doubled = [x * 2 for x in range(1, 6)]  # [2, 4, 6, 8, 10]
evens = [x for x in range(1, 11) if x % 2 == 0]  # [2, 4, 6, 8, 10]""",
            "hint":
            "Use [expression for item in range(...)] and add 'if condition' for filtering",
            "test_cases": [{
                "test":
                "assert len(squares) == 10 and squares[0] == 1 and squares[9] == 100\nassert len(even_squares) == 5 and 4 in even_squares",
                "expected":
                "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n[4, 16, 36, 64, 100]"
            }]
        }, {
            "id":
            "error_handling",
            "title":
            "Error Handling",
            "difficulty":
            "intermediate",
            "description":
            """
Write a program that:
1. Asks the user to imagine they input a number (use `user_input = "42"` for testing)
2. Tries to convert it to an integer and divide 100 by that number
3. Uses try-except to handle potential errors (like division by zero or invalid input)
4. Prints the result if successful, or an appropriate error message if not

This teaches you how to handle errors gracefully in your programs.
                """,
            "starter_code":
            "user_input = \"42\"  # Simulate user input\n\n# Your try-except code here\ntry:\n    # Conversion and calculation\n    pass\nexcept:\n    # Error handling\n    pass\n",
            "example":
            """try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")""",
            "hint":
            "Use int() to convert string to integer, and handle ValueError and ZeroDivisionError",
            "test_cases": [{
                "test":
                "# Test with valid input\nassert 'Result:' in output or '2.38' in output",
                "expected": "Result: 2.380952380952381"
            }]
        }],
        "advanced": [{
            "id":
            "class_basics",
            "title":
            "Object-Oriented Programming Basics",
            "difficulty":
            "advanced",
            "description":
            """
Create a class called `Person` that:
1. Has an `__init__` method that takes `name` and `age` parameters
2. Has a method `introduce()` that returns "Hi, I'm [name] and I'm [age] years old"
3. Has a method `birthday()` that increases age by 1 and returns "Happy birthday! Now I'm [new_age]"

Then create an instance of the Person class and call both methods.
                """,
            "starter_code":
            "class Person:\n    def __init__(self, name, age):\n        # Initialize the person\n        pass\n    \n    def introduce(self):\n        # Return introduction string\n        pass\n    \n    def birthday(self):\n        # Increase age and return birthday message\n        pass\n\n# Create a person and test the methods\nperson = Person(\"Alice\", 25)\n",
            "example":
            """class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday! Now I'm {self.age}"

person = Person("Bob", 30)
print(person.introduce())
print(person.birthday())""",
            "hint":
            "Use self.name and self.age to store instance variables. Don't forget to use 'self' as the first parameter in all methods.",
            "test_cases": [{
                "test":
                "person = Person('Test', 20)\nassert 'Test' in person.introduce() and '20' in person.introduce()\nbirthday_msg = person.birthday()\nassert '21' in birthday_msg",
                "expected": "Person class working correctly"
            }]
        }, {
            "id":
            "inheritance",
            "title":
            "Class Inheritance",
            "difficulty":
            "advanced",
            "description":
            """
Create a class hierarchy:

1. Base class `Animal` with:
   - `__init__(name, species)` method
   - `make_sound()` method that returns "The [species] makes a sound"

2. Child class `Dog` that inherits from Animal:
   - `__init__(name)` method that calls the parent with species="dog"
   - Override `make_sound()` to return "[name] says Woof!"
   - Add method `fetch()` that returns "[name] fetches the ball"

Create a Dog instance and test all methods.
                """,
            "starter_code":
            "class Animal:\n    def __init__(self, name, species):\n        # Your code here\n        pass\n    \n    def make_sound(self):\n        # Your code here\n        pass\n\nclass Dog(Animal):\n    def __init__(self, name):\n        # Your code here\n        pass\n    \n    def make_sound(self):\n        # Your code here\n        pass\n    \n    def fetch(self):\n        # Your code here\n        pass\n\n# Test your classes\ndog = Dog(\"Buddy\")\n",
            "hint":
            "Use super().__init__() to call the parent constructor. Override methods by defining them with the same name in the child class.",
            "test_cases": [{
                "test":
                "dog = Dog('Rex')\nassert 'Rex' in dog.make_sound() and 'Woof' in dog.make_sound()\nassert 'Rex' in dog.fetch() and 'ball' in dog.fetch()",
                "expected": "Inheritance working correctly"
            }]
        }, {
            "id":
            "file_handling",
            "title":
            "File Operations",
            "difficulty":
            "advanced",
            "description":
            """
Write a program that:
1. Creates a list of student data: [{"name": "Alice", "grade": 95}, {"name": "Bob", "grade": 87}]
2. Simulates writing to a file by creating a formatted string as if it were file content
3. Each line should be: "Student: [name], Grade: [grade]"
4. Print the formatted string (simulating file content)
5. Then simulate reading the file by parsing the string back into a dictionary

Note: We're simulating file operations for safety in this environment.
                """,
            "starter_code":
            "# Student data\nstudents = [{\"name\": \"Alice\", \"grade\": 95}, {\"name\": \"Bob\", \"grade\": 87}]\n\n# Simulate writing to file (create formatted string)\nfile_content = \"\"\n\n# Your code here to format the data\n\nprint(\"Simulated file content:\")\nprint(file_content)\n\n# Simulate reading from file (parse the string back)\nprint(\"\\nParsed data:\")\n# Your parsing code here\n",
            "example":
            """students = [{"name": "Alice", "grade": 95}]
file_content = ""
for student in students:
    file_content += f"Student: {student['name']}, Grade: {student['grade']}\\n"
print(file_content)

# Parse back
lines = file_content.strip().split('\\n')
for line in lines:
    # Parse each line
    parts = line.split(', ')
    name = parts[0].split(': ')[1]
    grade = int(parts[1].split(': ')[1])
    print(f"Name: {name}, Grade: {grade}")""",
            "hint":
            "Use string formatting to create file content, then use split() and string parsing to read it back.",
            "test_cases": [{
                "test":
                "assert 'Alice' in file_content and 'Bob' in file_content and 'Grade:' in file_content",
                "expected": "File simulation working"
            }]
        }, {
            "id":
            "lambda_functions",
            "title":
            "Lambda Functions and Higher-Order Functions",
            "difficulty":
            "advanced",
            "description":
            """
Use lambda functions and built-in higher-order functions:

1. Create a list of numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2. Use `filter()` with a lambda to get only even numbers
3. Use `map()` with a lambda to square all numbers in the original list
4. Use `sorted()` with a lambda to sort a list of tuples by the second element:
   [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

Print the results of each operation.
                """,
            "starter_code":
            "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nstudent_scores = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]\n\n# Use filter() with lambda to get even numbers\nevens = \n\n# Use map() with lambda to square all numbers\nsquares = \n\n# Use sorted() with lambda to sort by score\nsorted_students = \n\n# Print results\nprint(\"Even numbers:\", list(evens))\nprint(\"Squares:\", list(squares))\nprint(\"Sorted by score:\", sorted_students)\n",
            "example":
            """numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x ** 2, numbers)
scores = [('Alice', 85), ('Bob', 92)]
sorted_scores = sorted(scores, key=lambda x: x[1])
print(list(evens))
print(list(squares))
print(sorted_scores)""",
            "hint":
            "Lambda syntax: lambda parameter: expression. Use x % 2 == 0 for even numbers, x ** 2 for squares, and x[1] for second element of tuple.",
            "test_cases": [{
                "test":
                "evens_list = list(evens)\nsquares_list = list(squares)\nassert 2 in evens_list and 4 in evens_list\nassert 1 in squares_list and 25 in squares_list\nassert sorted_students[0][1] < sorted_students[1][1]",
                "expected": "Lambda functions working correctly"
            }]
        }, {
            "id":
            "decorators",
            "title":
            "Function Decorators",
            "difficulty":
            "advanced",
            "description":
            """
Create a simple decorator that measures execution time:

1. Create a decorator function `timer` that:
   - Takes a function as input
   - Returns a wrapper function that:
     - Records start time
     - Calls the original function
     - Records end time
     - Prints "Function [name] took [time] seconds"
     - Returns the original result

2. Apply the decorator to a function `slow_function()` that simulates work
3. Call the decorated function

Note: Use time.time() for timing measurements.
                """,
            "starter_code":
            "import time\n\ndef timer(func):\n    \"\"\"Decorator to measure function execution time\"\"\"\n    def wrapper(*args, **kwargs):\n        # Your decorator logic here\n        pass\n    return wrapper\n\n@timer\ndef slow_function():\n    \"\"\"Simulate a slow function\"\"\"\n    # Simulate work (use a simple loop instead of time.sleep)\n    total = 0\n    for i in range(1000000):\n        total += i\n    return total\n\n# Call the decorated function\nresult = slow_function()\nprint(f\"Result: {result}\")\n",
            "example":
            """def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def example_function():
    return sum(range(1000))

result = example_function()""",
            "hint":
            "Decorators are functions that take functions as input and return modified functions. Use func.__name__ to get the function name.",
            "test_cases": [{
                "test":
                "assert isinstance(result, int) and result > 0\n# Timer decorator should work and function should execute normally",
                "expected": "Decorator working correctly"
            }]
        }, {
            "id":
            "generators",
            "title":
            "Generators and Yield",
            "difficulty":
            "advanced",
            "description":
            """
Create generator functions:

1. Create a generator `fibonacci_generator(n)` that yields the first n Fibonacci numbers
2. Create a generator `even_squares(limit)` that yields squares of even numbers up to limit
3. Use both generators to print their values

Generators are memory-efficient ways to create sequences of values on-demand.
                """,
            "starter_code":
            "def fibonacci_generator(n):\n    \"\"\"Generate first n Fibonacci numbers\"\"\"\n    # Your generator code here\n    pass\n\ndef even_squares(limit):\n    \"\"\"Generate squares of even numbers up to limit\"\"\"\n    # Your generator code here\n    pass\n\n# Test the generators\nprint(\"First 8 Fibonacci numbers:\")\nfor num in fibonacci_generator(8):\n    print(num, end=\" \")\n\nprint(\"\\nSquares of even numbers up to 20:\")\nfor square in even_squares(20):\n    print(square, end=\" \")\n",
            "example":
            """def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)  # Prints 1, 2, 3

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1""",
            "hint":
            "Use 'yield' instead of 'return' to create generators. Fibonacci: start with a=0, b=1, then a, b = b, a+b.",
            "test_cases": [{
                "test":
                "fib_list = list(fibonacci_generator(5))\nassert fib_list[0] == 0 and fib_list[1] == 1 and fib_list[4] == 3\nsquares_list = list(even_squares(10))\nassert 4 in squares_list and 16 in squares_list",
                "expected": "Generators working correctly"
            }]
        }, {
            "id":
            "context_managers",
            "title":
            "Context Managers",
            "difficulty":
            "advanced",
            "description":
            """
Create a simple context manager using a class:

1. Create a class `Timer` that can be used with the `with` statement
2. It should have `__enter__` and `__exit__` methods
3. `__enter__` should record start time and print "Timer started"
4. `__exit__` should print "Timer stopped" and the elapsed time
5. Use it to time a simple operation

Context managers help manage resources and ensure cleanup happens.
                """,
            "starter_code":
            "import time\n\nclass Timer:\n    \"\"\"A simple timer context manager\"\"\"\n    \n    def __enter__(self):\n        # Your code here\n        pass\n    \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        # Your code here\n        pass\n\n# Use the context manager\nwith Timer():\n    # Simulate some work\n    total = sum(range(100000))\n    print(f\"Sum calculated: {total}\")\n",
            "example":
            """class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Timer started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Timer stopped. Elapsed: {elapsed:.4f} seconds")

with Timer():
    result = sum(range(1000))
    print(f"Result: {result}")""",
            "hint":
            "__enter__ is called when entering the 'with' block, __exit__ is called when leaving. Store start time in self.start.",
            "test_cases": [{
                "test":
                "# Test context manager functionality\nassert total > 0  # Sum calculation should work\n# Timer context manager should execute without errors",
                "expected": "Context manager working"
            }]
        }]
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
