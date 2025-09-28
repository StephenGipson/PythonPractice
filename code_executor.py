"""
Code execution functionality for the Python practice platform
"""

import sys
import io
import traceback
import contextlib
import signal
from typing import Dict, Any

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Code execution timed out")

def execute_code(code: str, timeout: int = 5) -> Dict[str, Any]:
    """
    Safely execute Python code and return the result
    
    Args:
        code: Python code to execute
        timeout: Maximum execution time in seconds
    
    Returns:
        Dictionary with success status, output, and error information
    """
    
    # Create a string buffer to capture output
    output_buffer = io.StringIO()
    error_buffer = io.StringIO()
    
    # Store original stdout and stderr
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    result = {
        "success": False,
        "output": "",
        "error": "",
        "execution_time": 0
    }
    
    try:
        # Set up timeout (only on Unix-like systems)
        if hasattr(signal, 'SIGALRM'):
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)
        
        # Redirect stdout and stderr
        sys.stdout = output_buffer
        sys.stderr = error_buffer
        
        # Create a restricted execution environment
        exec_globals = {
            '__builtins__': {
                # Safe built-ins
                'print': print,
                'len': len,
                'range': range,
                'enumerate': enumerate,
                'zip': zip,
                'map': map,
                'filter': filter,
                'sorted': sorted,
                'sum': sum,
                'min': min,
                'max': max,
                'abs': abs,
                'round': round,
                'int': int,
                'float': float,
                'str': str,
                'bool': bool,
                'list': list,
                'dict': dict,
                'tuple': tuple,
                'set': set,
                'type': type,
                'isinstance': isinstance,
                'hasattr': hasattr,
                'getattr': getattr,
                'setattr': setattr,
                'dir': dir,
                'help': help,
                'repr': repr,
                'ord': ord,
                'chr': chr,
                'any': any,
                'all': all,
                # Math operations
                'pow': pow,
                'divmod': divmod,
                # Exceptions
                'Exception': Exception,
                'ValueError': ValueError,
                'TypeError': TypeError,
                'IndexError': IndexError,
                'KeyError': KeyError,
                'AttributeError': AttributeError,
                'ZeroDivisionError': ZeroDivisionError,
                # Common modules (need to be imported explicitly)
            }
        }
        
        exec_locals = {}
        
        # Execute the code
        exec(code, exec_globals, exec_locals)
        
        result["success"] = True
        result["output"] = output_buffer.getvalue()
        
    except TimeoutException:
        result["error"] = "Code execution timed out. Make sure your code doesn't have infinite loops."
        
    except SyntaxError as e:
        result["error"] = f"Syntax Error: {str(e)}\nLine {e.lineno}: {e.text if e.text else 'N/A'}"
        
    except NameError as e:
        result["error"] = f"Name Error: {str(e)}\nMake sure all variables and functions are defined."
        
    except ZeroDivisionError as e:
        result["error"] = f"Division by Zero Error: {str(e)}\nYou cannot divide by zero."
        
    except IndexError as e:
        result["error"] = f"Index Error: {str(e)}\nYou're trying to access an index that doesn't exist."
        
    except KeyError as e:
        result["error"] = f"Key Error: {str(e)}\nThe dictionary key you're looking for doesn't exist."
        
    except TypeError as e:
        result["error"] = f"Type Error: {str(e)}\nCheck the data types you're working with."
        
    except ValueError as e:
        result["error"] = f"Value Error: {str(e)}\nThe value provided is not appropriate for the operation."
        
    except Exception as e:
        # Capture the full traceback for unexpected errors
        tb_str = traceback.format_exc()
        result["error"] = f"Runtime Error: {str(e)}\n\nFull traceback:\n{tb_str}"
        
    finally:
        # Restore original stdout and stderr
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        
        # Cancel the alarm (if set)
        if hasattr(signal, 'SIGALRM'):
            signal.alarm(0)
        
        # If there were any stderr messages, add them to the error
        stderr_content = error_buffer.getvalue()
        if stderr_content and not result["error"]:
            result["error"] = stderr_content
            result["success"] = False
    
    return result

def validate_code_safety(code: str) -> Dict[str, Any]:
    """
    Validate that the code doesn't contain potentially dangerous operations
    
    Args:
        code: Python code to validate
    
    Returns:
        Dictionary with validation status and warnings
    """
    
    dangerous_patterns = [
        'import os',
        'import sys',
        'import subprocess',
        'import socket',
        'import urllib',
        'import requests',
        'import http',
        'open(',
        'file(',
        'exec(',
        'eval(',
        '__import__',
        'globals()',
        'locals()',
        'vars()',
        'dir()',
        'getattr(',
        'setattr(',
        'delattr(',
        'hasattr(',
    ]
    
    warnings = []
    is_safe = True
    
    for pattern in dangerous_patterns:
        if pattern in code.lower():
            warnings.append(f"Potentially unsafe pattern detected: {pattern}")
            if pattern in ['exec(', 'eval(', '__import__', 'open(', 'file(']:
                is_safe = False
    
    return {
        "is_safe": is_safe,
        "warnings": warnings
    }

def run_tests(code: str, test_cases: list) -> Dict[str, Any]:
    """
    Run test cases against the provided code
    
    Args:
        code: User's Python code
        test_cases: List of test case dictionaries
    
    Returns:
        Dictionary with test results
    """
    
    results = {
        "passed": 0,
        "total": len(test_cases),
        "details": []
    }
    
    for i, test_case in enumerate(test_cases):
        test_code = code + "\n" + test_case.get('test', '')
        expected = test_case.get('expected', '')
        
        result = execute_code(test_code)
        
        test_result = {
            "test_number": i + 1,
            "passed": False,
            "expected": expected,
            "actual": result.get('output', '').strip(),
            "error": result.get('error', '')
        }
        
        if result['success'] and result['output'].strip() == expected:
            test_result['passed'] = True
            results['passed'] += 1
        
        results['details'].append(test_result)
    
    return results
