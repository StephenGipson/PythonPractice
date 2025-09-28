"""
Python concept explanations and educational content for the practice platform
"""

def get_concept_explanations():
    """Return detailed explanations of Python concepts organized by topic"""
    return {
        "variables_and_data_types": {
            "title": "Variables and Data Types",
            "explanation": """
## Variables and Data Types in Python

### What are Variables?
Variables in Python are like labeled containers that store data. Think of them as name tags for your data values.

### Basic Data Types:

**Strings (str)**: Text data
```python
name = "Alice"
message = 'Hello, World!'
```

**Integers (int)**: Whole numbers
```python
age = 25
year = 2023
```

**Floats (float)**: Decimal numbers
```python
height = 5.8
temperature = 98.6
```

**Booleans (bool)**: True or False values
```python
is_student = True
is_raining = False
```

### Variable Naming Rules:
- Start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (age and Age are different)
- Use descriptive names: `user_name` not `un`

### Best Practices:
- Use snake_case for variable names: `first_name`, `total_score`
- Choose meaningful names: `student_count` instead of `sc`
- Avoid Python keywords: `class`, `def`, `if`, etc.
            """,
            "examples": [
                {
                    "title": "Creating Variables",
                    "code": """# Creating different types of variables
name = "John Doe"
age = 30
height = 5.9
is_student = False

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")"""
                },
                {
                    "title": "Variable Operations",
                    "code": """# Working with variables
first_name = "Jane"
last_name = "Smith"
full_name = first_name + " " + last_name

current_year = 2023
birth_year = 1995
age = current_year - birth_year

print(f"Full name: {full_name}")
print(f"Age: {age}")"""
                }
            ],
            "common_mistakes": [
                "Using camelCase instead of snake_case",
                "Starting variable names with numbers",
                "Using reserved keywords as variable names",
                "Not using descriptive variable names"
            ]
        },
        "control_structures": {
            "title": "Control Structures (If/Else, Loops)",
            "explanation": """
## Control Structures in Python

Control structures allow you to control the flow of your program - when certain code runs and how many times.

### If/Else Statements

**Basic If Statement**:
```python
if condition:
    # Code runs if condition is True
```

**If/Else**:
```python
if condition:
    # Code runs if condition is True
else:
    # Code runs if condition is False
```

**If/Elif/Else**:
```python
if condition1:
    # Code runs if condition1 is True
elif condition2:
    # Code runs if condition2 is True
else:
    # Code runs if none of the above are True
```

### Comparison Operators:
- `==` equal to
- `!=` not equal to
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to

### For Loops
Used to repeat code a specific number of times or iterate through collections:

```python
# Loop through a range of numbers
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### While Loops
Used to repeat code while a condition is True:

```python
count = 0
while count < 5:
    print(count)
    count += 1  # Don't forget to update the condition!
```

### Best Practices:
- Use meaningful variable names in loops
- Be careful with while loops to avoid infinite loops
- Use `range()` for numeric loops
- Keep conditions simple and readable
            """,
            "examples": [
                {
                    "title": "Grade Classification",
                    "code": """score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")"""
                },
                {
                    "title": "Even Numbers with Loop",
                    "code": """# Print even numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even")"""
                }
            ],
            "common_mistakes": [
                "Forgetting the colon (:) after if/for/while statements",
                "Not indenting code blocks properly",
                "Creating infinite while loops",
                "Using = instead of == for comparison"
            ]
        },
        "functions": {
            "title": "Functions",
            "explanation": """
## Functions in Python

Functions are reusable blocks of code that perform specific tasks. They help organize code and avoid repetition.

### Basic Function Syntax:
```python
def function_name(parameters):
    \"\"\"Optional docstring\"\"\"
    # Function body
    return result  # Optional
```

### Parts of a Function:
1. **def**: Keyword to define a function
2. **function_name**: Name to call the function
3. **parameters**: Input values (optional)
4. **docstring**: Description of what the function does (optional but recommended)
5. **return**: What the function gives back (optional)

### Types of Functions:

**Functions with no parameters:**
```python
def greet():
    print("Hello, World!")

greet()  # Call the function
```

**Functions with parameters:**
```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
```

**Functions that return values:**
```python
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(sum_result)  # Prints 8
```

**Functions with default parameters:**
```python
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")  # Uses default title
greet_with_title("Smith", "Dr.")  # Uses provided title
```

### Why Use Functions?
- **Reusability**: Write once, use many times
- **Organization**: Break complex problems into smaller parts
- **Testing**: Easier to test individual pieces
- **Maintenance**: Easier to fix and update code

### Best Practices:
- Use descriptive function names: `calculate_area()` not `calc()`
- Keep functions focused on one task
- Use docstrings to describe what the function does
- Return values instead of printing when possible
            """,
            "examples": [
                {
                    "title": "Calculator Functions",
                    "code": """def add(a, b):
    \"\"\"Add two numbers and return the result\"\"\"
    return a + b

def multiply(a, b):
    \"\"\"Multiply two numbers and return the result\"\"\"
    return a * b

# Using the functions
x = 10
y = 5
sum_result = add(x, y)
product = multiply(x, y)

print(f"{x} + {y} = {sum_result}")
print(f"{x} * {y} = {product}")"""
                },
                {
                    "title": "String Processing Function",
                    "code": """def format_name(first, last):
    \"\"\"Format a name with proper capitalization\"\"\"
    formatted = f"{first.title()} {last.title()}"
    return formatted

def get_initials(first, last):
    \"\"\"Get initials from first and last name\"\"\"
    return f"{first[0].upper()}.{last[0].upper()}."

# Using the functions
name = format_name("john", "doe")
initials = get_initials("john", "doe")

print(f"Formatted name: {name}")
print(f"Initials: {initials}")"""
                }
            ],
            "common_mistakes": [
                "Forgetting to call the function with parentheses",
                "Not returning a value when you need one",
                "Using print() instead of return in calculation functions",
                "Not handling different parameter types"
            ]
        },
        "data_structures": {
            "title": "Data Structures (Lists, Dictionaries)",
            "explanation": """
## Data Structures in Python

Data structures are ways to organize and store multiple pieces of data efficiently.

### Lists
Lists store multiple items in a single variable. They are ordered, changeable, and allow duplicates.

**Creating Lists:**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]
empty_list = []
```

**Common List Operations:**
```python
# Access items by index (starts at 0)
print(fruits[0])  # "apple"
print(fruits[-1])  # "cherry" (last item)

# Modify items
fruits[1] = "blueberry"

# Add items
fruits.append("orange")  # Add to end
fruits.insert(0, "grape")  # Insert at position

# Remove items
fruits.remove("apple")  # Remove by value
popped = fruits.pop()  # Remove and return last item

# Get length
count = len(fruits)
```

### Dictionaries
Dictionaries store data in key-value pairs. They are unordered, changeable, and don't allow duplicate keys.

**Creating Dictionaries:**
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Or create empty and add items
scores = {}
scores["math"] = 95
scores["science"] = 87
```

**Common Dictionary Operations:**
```python
# Access values by key
print(student["name"])  # "Alice"
print(student.get("age"))  # 20 (safer method)

# Modify values
student["grade"] = "A+"

# Add new key-value pairs
student["school"] = "Python University"

# Remove items
del student["age"]  # Remove key-value pair
grade = student.pop("grade")  # Remove and return value

# Get all keys, values, or items
keys = student.keys()
values = student.values()
items = student.items()
```

### When to Use Each:
- **Lists**: When you need ordered data, duplicates are okay
  - Shopping lists, scores, sequences
- **Dictionaries**: When you need to look up data by a unique identifier
  - Student records, settings, mappings

### Best Practices:
- Use descriptive variable names
- Check if keys exist before accessing dictionary values
- Use list comprehensions for simple transformations
- Consider using sets for unique items only
            """,
            "examples": [
                {
                    "title": "Student Grade Manager",
                    "code": """# Using lists and dictionaries together
students = [
    {"name": "Alice", "grades": [95, 87, 92]},
    {"name": "Bob", "grades": [78, 85, 90]},
    {"name": "Charlie", "grades": [88, 92, 85]}
]

# Calculate average grade for each student
for student in students:
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{student['name']}: {average:.1f}")"""
                },
                {
                    "title": "Inventory System",
                    "code": """# Inventory tracking with dictionary
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

# Check stock
item = "apples"
if item in inventory:
    print(f"We have {inventory[item]} {item}")
else:
    print(f"Sorry, no {item} in stock")

# Update inventory
inventory["apples"] -= 10  # Sold 10 apples
inventory["grapes"] = 20   # New item

print("Current inventory:")
for item, quantity in inventory.items():
    print(f"- {item}: {quantity}")"""
                }
            ],
            "common_mistakes": [
                "Trying to access list items with strings instead of numbers",
                "Accessing dictionary keys that don't exist",
                "Confusing list indexing (starts at 0, not 1)",
                "Modifying a list while iterating through it"
            ]
        },
        "object_oriented_programming": {
            "title": "Object-Oriented Programming",
            "explanation": """
## Object-Oriented Programming (OOP) in Python

OOP is a programming paradigm that organizes code into objects - things that have properties (attributes) and behaviors (methods).

### Key Concepts:

**Class**: A blueprint for creating objects
**Object**: An instance of a class
**Attribute**: Data stored in an object
**Method**: Function that belongs to an object

### Basic Class Syntax:
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    def introduce(self):  # Method
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def birthday(self):   # Method
        self.age += 1
        return f"Happy birthday! Now I'm {self.age}"

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Using methods
print(person1.introduce())
print(person2.birthday())
```

### The `__init__` Method:
- Special method called when creating a new object
- Used to set initial values for attributes
- Always takes `self` as first parameter

### The `self` Parameter:
- Refers to the current object instance
- Must be the first parameter in all methods
- Used to access attributes and methods of the object

### Inheritance:
Classes can inherit from other classes, gaining their attributes and methods:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return f"The {self.species} makes a sound"

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name):
        super().__init__(name, "dog")  # Call parent constructor
    
    def make_sound(self):  # Override parent method
        return f"{self.name} says Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} fetches the ball"
```

### Benefits of OOP:
- **Encapsulation**: Keep related data and functions together
- **Reusability**: Create multiple objects from the same class
- **Inheritance**: Build new classes based on existing ones
- **Polymorphism**: Different objects can have methods with the same name

### Best Practices:
- Use PascalCase for class names: `StudentRecord`, not `student_record`
- Use descriptive class and method names
- Keep classes focused on a single responsibility
- Use docstrings to document classes and methods
            """,
            "examples": [
                {
                    "title": "Bank Account Class",
                    "code": """class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Using the class
account = BankAccount("Alice Johnson", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())"""
                },
                {
                    "title": "Vehicle Inheritance",
                    "code": """class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def info(self):
        return f"{super().info()} with {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def info(self):
        return f"{super().info()} with {self.engine_size}cc engine"

# Creating objects
car = Car("Honda", "Civic", 2022, 4)
bike = Motorcycle("Yamaha", "R6", 2021, 600)

print(car.info())
print(bike.info())"""
                }
            ],
            "common_mistakes": [
                "Forgetting 'self' parameter in method definitions",
                "Not calling super().__init__() in inherited classes",
                "Trying to access attributes without 'self.'",
                "Creating classes when simple functions would suffice"
            ]
        }
    }

def get_category_concepts(category):
    """Get concept explanations for a specific exercise category"""
    # Normalize category name and map synonyms
    category_normalized = category.lower().strip()
    
    # Map different difficulty levels to standard categories
    difficulty_aliases = {
        "easy": "beginner",
        "basic": "beginner",
        "simple": "beginner",
        "medium": "intermediate", 
        "moderate": "intermediate",
        "hard": "advanced",
        "expert": "advanced",
        "complex": "advanced"
    }
    
    # Use alias if found, otherwise use the normalized category
    category_key = difficulty_aliases.get(category_normalized, category_normalized)
    
    concept_map = {
        "beginner": ["variables_and_data_types", "control_structures"],
        "intermediate": ["functions", "data_structures"],
        "advanced": ["object_oriented_programming"]
    }
    
    explanations = get_concept_explanations()
    category_concepts = []
    
    for concept_key in concept_map.get(category_key, []):
        if concept_key in explanations:
            category_concepts.append(explanations[concept_key])
    
    return category_concepts

def get_enhanced_hints():
    """Return enhanced hints for common programming patterns"""
    return {
        "debugging_tips": [
            "Read error messages carefully - they often tell you exactly what's wrong",
            "Use print() statements to see what your variables contain",
            "Check your indentation - Python is very picky about this",
            "Make sure you're using the right data type for operations",
            "Break complex problems into smaller, simpler steps"
        ],
        "problem_solving_strategies": [
            "Understand the problem: Read the requirements twice",
            "Plan your approach: Write comments outlining your steps",
            "Start simple: Get basic functionality working first",
            "Test frequently: Run your code after each small change",
            "Use meaningful variable names to make code self-documenting"
        ],
        "python_specific_tips": [
            "Remember that Python lists start at index 0, not 1",
            "Use 'in' to check if an item exists: 'if item in my_list:'",
            "String methods like .upper(), .lower(), .strip() are very useful",
            "The range() function doesn't include the end number: range(1, 5) gives [1, 2, 3, 4]",
            "Use f-strings for easy string formatting: f'Hello {name}!'"
        ]
    }