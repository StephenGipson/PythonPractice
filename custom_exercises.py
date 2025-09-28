"""
Custom exercise builder and management for the Python practice platform
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any

class CustomExerciseManager:
    """Manages custom exercises created by users"""
    
    def __init__(self, filename="custom_exercises.json"):
        self.filename = filename
        self.custom_exercises = self.load_custom_exercises()
    
    def load_custom_exercises(self) -> Dict[str, Any]:
        """Load custom exercises from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Return default structure if file doesn't exist or is corrupted
        return {
            "exercises": [],
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
    
    def save_custom_exercises(self):
        """Save custom exercises to file"""
        try:
            self.custom_exercises["last_updated"] = datetime.now().isoformat()
            with open(self.filename, 'w') as f:
                json.dump(self.custom_exercises, f, indent=2)
        except Exception as e:
            print(f"Error saving custom exercises: {e}")
    
    def add_exercise(self, exercise_data: Dict[str, Any]) -> bool:
        """
        Add a new custom exercise
        
        Args:
            exercise_data: Dictionary containing exercise information
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Validate required fields
            required_fields = ['title', 'difficulty', 'description']
            for field in required_fields:
                if field not in exercise_data or not exercise_data[field].strip():
                    return False
            
            # Generate unique ID
            exercise_id = f"custom_{len(self.custom_exercises['exercises']) + 1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            # Create exercise with metadata
            exercise = {
                "id": exercise_id,
                "title": exercise_data['title'].strip(),
                "difficulty": exercise_data['difficulty'].lower(),
                "description": exercise_data['description'].strip(),
                "starter_code": exercise_data.get('starter_code', '# Write your code here\n'),
                "example": exercise_data.get('example', ''),
                "hint": exercise_data.get('hint', ''),
                "test_cases": exercise_data.get('test_cases', []),
                "created_at": datetime.now().isoformat(),
                "created_by": "user",
                "tags": exercise_data.get('tags', [])
            }
            
            self.custom_exercises['exercises'].append(exercise)
            self.save_custom_exercises()
            return True
            
        except Exception as e:
            print(f"Error adding exercise: {e}")
            return False
    
    def get_all_custom_exercises(self) -> List[Dict[str, Any]]:
        """Get all custom exercises"""
        return self.custom_exercises.get('exercises', [])
    
    def get_exercise_by_id(self, exercise_id: str) -> Dict[str, Any] | None:
        """Get a specific custom exercise by ID"""
        for exercise in self.custom_exercises.get('exercises', []):
            if exercise['id'] == exercise_id:
                return exercise
        return None
    
    def delete_exercise(self, exercise_id: str) -> bool:
        """Delete a custom exercise by ID"""
        try:
            exercises = self.custom_exercises.get('exercises', [])
            original_count = len(exercises)
            
            self.custom_exercises['exercises'] = [
                ex for ex in exercises if ex['id'] != exercise_id
            ]
            
            if len(self.custom_exercises['exercises']) < original_count:
                self.save_custom_exercises()
                return True
            return False
            
        except Exception as e:
            print(f"Error deleting exercise: {e}")
            return False
    
    def get_exercises_by_difficulty(self, difficulty: str) -> List[Dict[str, Any]]:
        """Get custom exercises filtered by difficulty"""
        return [
            ex for ex in self.custom_exercises.get('exercises', [])
            if ex['difficulty'].lower() == difficulty.lower()
        ]
    
    def search_exercises(self, query: str) -> List[Dict[str, Any]]:
        """Search exercises by title, description, or tags"""
        query_lower = query.lower()
        results = []
        
        for exercise in self.custom_exercises.get('exercises', []):
            # Search in title, description, and tags
            if (query_lower in exercise['title'].lower() or
                query_lower in exercise['description'].lower() or
                any(query_lower in tag.lower() for tag in exercise.get('tags', []))):
                results.append(exercise)
        
        return results

def validate_test_case(test_case_text: str) -> bool:
    """
    Validate a test case string for basic syntax
    
    Args:
        test_case_text: The test case code as a string
        
    Returns:
        True if valid, False otherwise
    """
    try:
        # Try to compile the test case to check for syntax errors
        compile(test_case_text, '<test_case>', 'exec')
        return True
    except SyntaxError:
        return False

def create_test_case(test_code: str, expected_output: str) -> Dict[str, str]:
    """
    Create a test case dictionary
    
    Args:
        test_code: Python code to test the user's solution
        expected_output: Expected output from the test
        
    Returns:
        Dictionary representing the test case
    """
    return {
        "test": test_code,
        "expected": expected_output
    }

def get_difficulty_options() -> List[str]:
    """Get available difficulty options"""
    return ["beginner", "intermediate", "advanced"]

def get_example_exercise_templates() -> Dict[str, Dict[str, Any]]:
    """Get example exercise templates to help users create exercises"""
    return {
        "basic_function": {
            "title": "Create a Calculator Function",
            "difficulty": "beginner",
            "description": """
Write a function called `calculate` that takes two numbers and an operation (+, -, *, /) and returns the result.

Example:
- calculate(5, 3, '+') should return 8
- calculate(10, 2, '/') should return 5.0
            """,
            "starter_code": "def calculate(a, b, operation):\n    # Your code here\n    pass\n\n# Test your function\nresult = calculate(5, 3, '+')\nprint(result)",
            "example": "def calculate(a, b, operation):\n    if operation == '+':\n        return a + b\n    elif operation == '-':\n        return a - b\n    elif operation == '*':\n        return a * b\n    elif operation == '/':\n        return a / b\n    else:\n        return 'Invalid operation'",
            "hint": "Use if/elif statements to check the operation type",
            "test_cases": [
                {
                    "test": "result = calculate(5, 3, '+')\nassert result == 8",
                    "expected": ""
                }
            ],
            "tags": ["functions", "conditionals", "arithmetic"]
        },
        "list_processing": {
            "title": "Find Maximum in List",
            "difficulty": "intermediate",
            "description": """
Write a function `find_max` that takes a list of numbers and returns the largest number.
Don't use the built-in max() function.

Example:
- find_max([1, 5, 3, 9, 2]) should return 9
- find_max([10]) should return 10
            """,
            "starter_code": "def find_max(numbers):\n    # Your code here\n    pass\n\n# Test your function\nresult = find_max([1, 5, 3, 9, 2])\nprint(result)",
            "example": "def find_max(numbers):\n    if not numbers:\n        return None\n    \n    max_num = numbers[0]\n    for num in numbers:\n        if num > max_num:\n            max_num = num\n    return max_num",
            "hint": "Start with the first number as the maximum, then compare each number in the list",
            "test_cases": [
                {
                    "test": "result = find_max([1, 5, 3, 9, 2])\nassert result == 9",
                    "expected": ""
                }
            ],
            "tags": ["lists", "loops", "algorithms"]
        },
        "class_example": {
            "title": "Create a Student Class",
            "difficulty": "advanced",
            "description": """
Create a class called `Student` with the following features:
1. Constructor that takes name and initial grades (list)
2. Method `add_grade(grade)` to add a new grade
3. Method `get_average()` to calculate average grade
4. Method `get_letter_grade()` to return A, B, C, D, or F based on average

Grading scale: A (90+), B (80-89), C (70-79), D (60-69), F (below 60)
            """,
            "starter_code": "class Student:\n    def __init__(self, name, grades=None):\n        # Your code here\n        pass\n    \n    def add_grade(self, grade):\n        # Your code here\n        pass\n    \n    def get_average(self):\n        # Your code here\n        pass\n    \n    def get_letter_grade(self):\n        # Your code here\n        pass\n\n# Test your class\nstudent = Student('Alice', [85, 92, 78])\nprint(student.get_average())\nprint(student.get_letter_grade())",
            "example": "class Student:\n    def __init__(self, name, grades=None):\n        self.name = name\n        self.grades = grades or []\n    \n    def add_grade(self, grade):\n        self.grades.append(grade)\n    \n    def get_average(self):\n        if not self.grades:\n            return 0\n        return sum(self.grades) / len(self.grades)\n    \n    def get_letter_grade(self):\n        avg = self.get_average()\n        if avg >= 90: return 'A'\n        elif avg >= 80: return 'B'\n        elif avg >= 70: return 'C'\n        elif avg >= 60: return 'D'\n        else: return 'F'",
            "hint": "Remember to use self for instance variables and methods",
            "test_cases": [
                {
                    "test": "student = Student('Test', [85, 92, 78])\navg = student.get_average()\nassert 84 <= avg <= 86",
                    "expected": ""
                }
            ],
            "tags": ["classes", "oop", "methods"]
        }
    }