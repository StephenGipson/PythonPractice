"""
Specialized exercise tracks for data science and web development
"""

def get_data_science_exercises():
    """Return data science focused exercises"""
    return [
        {
            "id": "data_analysis_basics",
            "title": "Data Analysis with Lists",
            "difficulty": "intermediate",
            "description": """
You're given sales data as a list of dictionaries. Analyze this data to extract insights.

Given data structure:
```python
sales_data = [
    {"product": "Laptop", "price": 1200, "quantity": 5},
    {"product": "Mouse", "price": 25, "quantity": 50},
    {"product": "Keyboard", "price": 75, "quantity": 30}
]
```

Calculate:
1. Total revenue (price × quantity for all products)
2. Average price per product
3. Product with highest revenue
4. Return results as a dictionary with keys: 'total_revenue', 'avg_price', 'top_product'
            """,
            "starter_code": """sales_data = [
    {"product": "Laptop", "price": 1200, "quantity": 5},
    {"product": "Mouse", "price": 25, "quantity": 50},
    {"product": "Keyboard", "price": 75, "quantity": 30}
]

def analyze_sales(data):
    # Your analysis code here
    pass

# Test your function
result = analyze_sales(sales_data)
print(result)""",
            "example": """def analyze_sales(data):
    total_revenue = sum(item['price'] * item['quantity'] for item in data)
    avg_price = sum(item['price'] for item in data) / len(data)
    
    # Find product with highest revenue
    max_revenue = 0
    top_product = ""
    for item in data:
        revenue = item['price'] * item['quantity']
        if revenue > max_revenue:
            max_revenue = revenue
            top_product = item['product']
    
    return {
        'total_revenue': total_revenue,
        'avg_price': avg_price,
        'top_product': top_product
    }""",
            "hint": "Use list comprehensions for calculations and a loop to find the maximum revenue product",
            "test_cases": [
                {
                    "test": "result = analyze_sales(sales_data)\nassert result['total_revenue'] == 8500\nassert result['avg_price'] == 433.33\nassert result['top_product'] == 'Laptop'",
                    "expected": ""
                }
            ],
            "tags": ["data-science", "analysis", "dictionaries", "lists"]
        },
        {
            "id": "statistics_calculator",
            "title": "Basic Statistics Calculator",
            "difficulty": "intermediate", 
            "description": """
Create a statistics calculator that computes basic statistical measures.

Implement a function `calculate_stats(numbers)` that returns a dictionary with:
- mean: average of the numbers
- median: middle value when sorted
- mode: most frequently occurring number (return the first one if there's a tie)
- range: difference between max and min values

Example:
calculate_stats([1, 2, 2, 3, 4, 4, 5]) should return:
{'mean': 3.0, 'median': 3, 'mode': 2, 'range': 4}
            """,
            "starter_code": """def calculate_stats(numbers):
    \"\"\"Calculate basic statistics for a list of numbers\"\"\"
    # Your code here
    pass

# Test your function
test_data = [1, 2, 2, 3, 4, 4, 5]
stats = calculate_stats(test_data)
print(stats)""",
            "example": """def calculate_stats(numbers):
    if not numbers:
        return None
    
    # Mean
    mean = sum(numbers) / len(numbers)
    
    # Median
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    # Mode
    from collections import Counter
    counts = Counter(numbers)
    mode = counts.most_common(1)[0][0]
    
    # Range
    range_val = max(numbers) - min(numbers)
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'range': range_val
    }""",
            "hint": "Sort the list for median, use a dictionary to count frequencies for mode",
            "test_cases": [
                {
                    "test": "result = calculate_stats([1, 2, 2, 3, 4, 4, 5])\nassert abs(result['mean'] - 3.0) < 0.01\nassert result['median'] == 3\nassert result['range'] == 4",
                    "expected": ""
                }
            ],
            "tags": ["data-science", "statistics", "algorithms"]
        },
        {
            "id": "data_cleaning",
            "title": "Data Cleaning Pipeline",
            "difficulty": "advanced",
            "description": """
Create a data cleaning pipeline for messy user data.

You'll receive a list of user records with potential issues:
- Missing values (None or empty strings)
- Inconsistent email formats
- Age values that might be strings
- Names with extra whitespace

Implement `clean_user_data(users)` that:
1. Removes records with missing required fields (name, email)
2. Strips whitespace from names
3. Converts age to integer (skip if invalid)
4. Validates email format (must contain @ and .)
5. Returns cleaned data

Input example:
```python
users = [
    {"name": " John Doe ", "email": "john@email.com", "age": "25"},
    {"name": "", "email": "invalid-email", "age": "30"},
    {"name": "Jane Smith", "email": "jane@test.com", "age": None}
]
```
            """,
            "starter_code": """def clean_user_data(users):
    \"\"\"Clean and validate user data\"\"\"
    # Your data cleaning code here
    pass

# Test data
test_users = [
    {"name": " John Doe ", "email": "john@email.com", "age": "25"},
    {"name": "", "email": "invalid-email", "age": "30"},
    {"name": "Jane Smith", "email": "jane@test.com", "age": None},
    {"name": "Bob Wilson", "email": "bob@company.co.uk", "age": "invalid"}
]

cleaned = clean_user_data(test_users)
print(f"Cleaned {len(cleaned)} records from {len(test_users)} original records")
for user in cleaned:
    print(user)""",
            "example": """def clean_user_data(users):
    cleaned = []
    
    for user in users:
        # Check required fields
        if not user.get('name') or not user.get('email'):
            continue
        
        # Clean name
        name = user['name'].strip()
        if not name:
            continue
        
        # Validate email
        email = user['email']
        if '@' not in email or '.' not in email:
            continue
        
        # Handle age
        age = user.get('age')
        if age is not None:
            try:
                age = int(age)
            except (ValueError, TypeError):
                age = None
        
        cleaned.append({
            'name': name,
            'email': email,
            'age': age
        })
    
    return cleaned""",
            "hint": "Use strip() for whitespace, try/except for type conversion, and simple string checks for email validation",
            "test_cases": [
                {
                    "test": "result = clean_user_data(test_users)\nassert len(result) == 2\nassert result[0]['name'] == 'John Doe'\nassert result[0]['age'] == 25",
                    "expected": ""
                }
            ],
            "tags": ["data-science", "data-cleaning", "validation"]
        }
    ]

def get_web_development_exercises():
    """Return web development focused exercises"""
    return [
        {
            "id": "html_generator",
            "title": "HTML Generator Functions",
            "difficulty": "intermediate",
            "description": """
Create functions to generate HTML elements programmatically.

Implement these functions:
1. `create_tag(tag_name, content, attributes=None)` - Creates any HTML tag
2. `create_link(url, text)` - Creates an anchor tag
3. `create_table(headers, rows)` - Creates a table with headers and data rows

Examples:
- create_tag("h1", "Welcome", {"class": "title"}) → "<h1 class='title'>Welcome</h1>"
- create_link("https://python.org", "Python") → "<a href='https://python.org'>Python</a>"
- create_table(["Name", "Age"], [["John", 25], ["Jane", 30]]) → full table HTML
            """,
            "starter_code": """def create_tag(tag_name, content, attributes=None):
    \"\"\"Create an HTML tag with content and optional attributes\"\"\"
    # Your code here
    pass

def create_link(url, text):
    \"\"\"Create an HTML anchor tag\"\"\"
    # Your code here
    pass

def create_table(headers, rows):
    \"\"\"Create an HTML table with headers and data rows\"\"\"
    # Your code here
    pass

# Test your functions
print(create_tag("h1", "Welcome", {"class": "title"}))
print(create_link("https://python.org", "Python"))
print(create_table(["Name", "Age"], [["John", 25], ["Jane", 30]]))""",
            "example": """def create_tag(tag_name, content, attributes=None):
    attr_str = ""
    if attributes:
        attr_str = " " + " ".join([f"{k}='{v}'" for k, v in attributes.items()])
    return f"<{tag_name}{attr_str}>{content}</{tag_name}>"

def create_link(url, text):
    return f"<a href='{url}'>{text}</a>"

def create_table(headers, rows):
    header_html = "<tr>" + "".join([f"<th>{h}</th>" for h in headers]) + "</tr>"
    rows_html = ""
    for row in rows:
        rows_html += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
    return f"<table>{header_html}{rows_html}</table>" """,
            "hint": "Use string formatting and loops to build HTML strings. Don't forget opening and closing tags!",
            "test_cases": [
                {
                    "test": "result = create_tag('h1', 'Test', {'class': 'header'})\nassert '<h1' in result and 'Test' in result and '</h1>' in result",
                    "expected": ""
                }
            ],
            "tags": ["web-development", "html", "string-manipulation"]
        },
        {
            "id": "url_router",
            "title": "Simple URL Router",
            "difficulty": "advanced",
            "description": """
Create a simple URL routing system like those used in web frameworks.

Implement a `Router` class with:
1. `add_route(path, handler_function)` - Register a route
2. `match_route(url)` - Find matching route and return handler
3. Support for URL parameters like "/user/{id}"

The router should:
- Match exact paths: "/home" matches "/home"
- Handle parameters: "/user/{id}" matches "/user/123" and extracts {"id": "123"}
- Return the handler function and extracted parameters

Example usage:
```python
router = Router()
router.add_route("/home", lambda: "Home Page")
router.add_route("/user/{id}", lambda id: f"User {id}")

handler, params = router.match_route("/user/123")
result = handler(**params)  # Should return "User 123"
```
            """,
            "starter_code": """class Router:
    def __init__(self):
        # Your initialization code here
        pass
    
    def add_route(self, path, handler_function):
        \"\"\"Register a route with its handler function\"\"\"
        # Your code here
        pass
    
    def match_route(self, url):
        \"\"\"Find matching route and return (handler, params) or (None, None)\"\"\"
        # Your code here
        pass

# Test your router
router = Router()
router.add_route("/home", lambda: "Home Page")
router.add_route("/user/{id}", lambda id: f"User {id}")
router.add_route("/post/{id}/comment/{comment_id}", lambda id, comment_id: f"Post {id}, Comment {comment_id}")

# Test exact match
handler, params = router.match_route("/home")
print(f"Home: {handler() if handler else 'Not found'}")

# Test parameter match
handler, params = router.match_route("/user/123")
print(f"User: {handler(**params) if handler else 'Not found'}")""",
            "example": """class Router:
    def __init__(self):
        self.routes = []
    
    def add_route(self, path, handler_function):
        self.routes.append((path, handler_function))
    
    def match_route(self, url):
        for path, handler in self.routes:
            params = self._match_path(path, url)
            if params is not None:
                return handler, params
        return None, None
    
    def _match_path(self, pattern, url):
        pattern_parts = pattern.split('/')
        url_parts = url.split('/')
        
        if len(pattern_parts) != len(url_parts):
            return None
        
        params = {}
        for pattern_part, url_part in zip(pattern_parts, url_parts):
            if pattern_part.startswith('{') and pattern_part.endswith('}'):
                param_name = pattern_part[1:-1]
                params[param_name] = url_part
            elif pattern_part != url_part:
                return None
        
        return params""",
            "hint": "Split URLs by '/' and compare parts. Use {} to identify parameters and extract their values.",
            "test_cases": [
                {
                    "test": "router = Router()\nrouter.add_route('/user/{id}', lambda id: f'User {id}')\nhandler, params = router.match_route('/user/123')\nassert handler is not None\nassert params['id'] == '123'",
                    "expected": ""
                }
            ],
            "tags": ["web-development", "routing", "classes", "string-processing"]
        },
        {
            "id": "template_engine",
            "title": "Simple Template Engine",
            "difficulty": "advanced",
            "description": """
Create a basic template engine that can replace variables in HTML templates.

Implement `render_template(template, context)` that:
1. Replaces {{variable}} with values from context dictionary
2. Handles missing variables gracefully (replace with empty string)
3. Supports basic loops: {{#each items}}{{name}}{{/each}}

Examples:
- Template: "Hello {{name}}!" with context {"name": "World"} → "Hello World!"
- Template: "{{#each users}}{{name}} {{/each}}" with context {"users": [{"name": "John"}, {"name": "Jane"}]} → "John Jane "

Focus on the variable replacement first, then add loop support if time permits.
            """,
            "starter_code": """def render_template(template, context):
    \"\"\"Render a template with variable substitution\"\"\"
    # Your template rendering code here
    pass

# Test templates
template1 = "Hello {{name}}! Welcome to {{site}}."
context1 = {"name": "Alice", "site": "Python Practice"}

template2 = "User: {{username}}, Email: {{email}}, Age: {{age}}"
context2 = {"username": "john_doe", "email": "john@example.com"}  # Missing age

print(render_template(template1, context1))
print(render_template(template2, context2))

# Loop template (advanced)
template3 = "Users: {{#each users}}{{name}} {{/each}}"
context3 = {"users": [{"name": "John"}, {"name": "Jane"}, {"name": "Bob"}]}
print(render_template(template3, context3))""",
            "example": """import re

def render_template(template, context):
    # Replace simple variables {{variable}}
    def replace_var(match):
        var_name = match.group(1)
        return str(context.get(var_name, ''))
    
    result = re.sub(r'\\{\\{(\\w+)\\}\\}', replace_var, template)
    
    # Handle loops {{#each array}}content{{/each}}
    def replace_loop(match):
        array_name = match.group(1)
        loop_content = match.group(2)
        
        array = context.get(array_name, [])
        output = ""
        
        for item in array:
            # Replace variables in loop content with item properties
            item_content = loop_content
            for key, value in item.items():
                item_content = item_content.replace(f'{{{{ {key} }}}}', str(value))
            output += item_content
        
        return output
    
    result = re.sub(r'\\{\\{#each (\\w+)\\}\\}(.*?)\\{\\{/each\\}\\}', replace_loop, result)
    return result""",
            "hint": "Use regular expressions to find {{variable}} patterns and replace them with dictionary values",
            "test_cases": [
                {
                    "test": "result = render_template('Hello {{name}}!', {'name': 'World'})\nassert result == 'Hello World!'",
                    "expected": ""
                }
            ],
            "tags": ["web-development", "templates", "regex", "string-processing"]
        }
    ]

def get_specialized_tracks():
    """Return all specialized exercise tracks"""
    return {
        "data_science": {
            "title": "Data Science Track",
            "description": "Learn Python for data analysis, statistics, and data manipulation",
            "exercises": get_data_science_exercises(),
            "icon": "📊"
        },
        "web_development": {
            "title": "Web Development Track", 
            "description": "Build web applications with Python - HTML generation, routing, and templates",
            "exercises": get_web_development_exercises(),
            "icon": "🌐"
        }
    }