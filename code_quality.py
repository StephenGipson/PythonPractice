"""
Code quality analysis and best practices suggestions for the Python practice platform
"""

import ast
import re
from typing import List, Dict, Any

class CodeQualityAnalyzer:
    """Analyzes Python code and provides quality feedback and best practices suggestions"""
    
    def __init__(self):
        self.suggestions = []
        self.warnings = []
        self.best_practices = []
    
    def analyze_code(self, code: str) -> Dict[str, Any]:
        """
        Analyze code and return feedback
        
        Args:
            code: Python code string to analyze
            
        Returns:
            Dictionary with analysis results
        """
        self.suggestions = []
        self.warnings = []
        self.best_practices = []
        
        # Basic syntax and structure checks
        self._check_syntax(code)
        self._check_naming_conventions(code)
        self._check_code_style(code)
        self._check_best_practices(code)
        self._check_complexity(code)
        
        return {
            "suggestions": self.suggestions,
            "warnings": self.warnings,
            "best_practices": self.best_practices,
            "score": self._calculate_quality_score()
        }
    
    def _check_syntax(self, code: str):
        """Check for basic syntax issues"""
        try:
            ast.parse(code)
        except SyntaxError as e:
            self.warnings.append(f"Syntax Error: {str(e)}")
            return
        
        # Check for missing return statements in functions
        if 'def ' in code and 'return' not in code:
            # Parse to check if function should return something
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        # Check if function has computations that might need to be returned
                        # Only suggest if the last statement is an expression or assignment
                        if node.body:
                            last_stmt = node.body[-1]
                            if (isinstance(last_stmt, ast.Expr) and 
                                not isinstance(last_stmt.value, ast.Call) or
                                isinstance(last_stmt, ast.Assign)):
                                # Check if there are calculations that might need returning
                                has_calculation = any(
                                    isinstance(stmt, ast.Assign) and
                                    isinstance(stmt.value, (ast.BinOp, ast.Call))
                                    for stmt in node.body
                                )
                                if has_calculation:
                                    self.suggestions.append(f"Consider if function '{node.name}' should return a computed value")
            except:
                pass
    
    def _check_naming_conventions(self, code: str):
        """Check Python naming conventions"""
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Check for camelCase variables (should be snake_case)
            camel_case_pattern = r'\b[a-z]+[A-Z][a-zA-Z]*\b'
            if re.search(camel_case_pattern, line) and not line.startswith('#'):
                matches = re.findall(camel_case_pattern, line)
                for match in matches:
                    if match not in ['firstName', 'lastName', 'userName']:  # Common exceptions
                        snake_case = re.sub(r'([A-Z])', r'_\1', match).lower()
                        self.suggestions.append(f"Line {line_num}: Consider using snake_case '{snake_case}' instead of camelCase '{match}'")
            
            # Check for ALL_CAPS variables that aren't constants
            if '=' in line and not line.startswith('#'):
                var_name = line.split('=')[0].strip()
                if var_name.isupper() and len(var_name) > 1 and not var_name.startswith('_'):
                    if not self._is_constant_assignment(line):
                        self.suggestions.append(f"Line {line_num}: ALL_CAPS should be reserved for constants")
            
            # Check for single-letter variable names (except common ones)
            single_letter_pattern = r'\b[a-z]\s*='
            if re.search(single_letter_pattern, line) and not any(x in line for x in ['for ', 'in range', 'enumerate']):
                matches = re.findall(r'\b([a-z])\s*=', line)
                for match in matches:
                    if match not in ['i', 'j', 'k', 'x', 'y', 'z', 'n']:
                        self.suggestions.append(f"Line {line_num}: Consider using descriptive variable names instead of single letter '{match}'")
    
    def _check_code_style(self, code: str):
        """Check code style and formatting"""
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Check line length
            if len(line) > 100:
                self.suggestions.append(f"Line {line_num}: Consider breaking long lines (current: {len(line)} chars)")
            
            # Check for missing spaces around operators (exclude strings)
            if not line.strip().startswith('#') and '"' not in line and "'" not in line:
                operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
                for op in operators:
                    if op in line:
                        # Simple check for missing spaces (not perfect but helpful)
                        pattern = rf'[a-zA-Z0-9]{re.escape(op)}[a-zA-Z0-9]'
                        if re.search(pattern, line):
                            self.suggestions.append(f"Line {line_num}: Consider adding spaces around operator '{op}'")
                            break
            
            # Check for missing spaces after commas
            if ',' in line and ',  ' not in line and ', ' not in line:
                comma_pattern = r',[a-zA-Z0-9]'
                if re.search(comma_pattern, line):
                    self.suggestions.append(f"Line {line_num}: Consider adding space after comma")
        
        # Check for consistent indentation
        indent_sizes = []
        has_tabs = False
        
        for line in lines:
            if line.strip() and (line.startswith(' ') or line.startswith('\t')):
                if line.startswith('\t'):
                    has_tabs = True
                leading_spaces = len(line) - len(line.lstrip())
                if leading_spaces > 0:
                    indent_sizes.append(leading_spaces)
        
        if has_tabs:
            self.suggestions.append("Consider using spaces instead of tabs for indentation")
        
        if indent_sizes:
            # Check if all indentations are multiples of 4
            non_four_multiples = [size for size in indent_sizes if size % 4 != 0]
            if non_four_multiples:
                self.suggestions.append("Consider using 4-space indentation for consistency")
    
    def _check_best_practices(self, code: str):
        """Check for Python best practices"""
        lines = code.split('\n')
        
        # Check for string concatenation in loops
        in_loop = False
        for line_num, line in enumerate(lines, 1):
            line_stripped = line.strip()
            
            if line_stripped.startswith('for ') or line_stripped.startswith('while '):
                in_loop = True
            elif line_stripped == '' or not line.startswith(' '):
                in_loop = False
            
            if in_loop and '+=' in line and any(quote in line for quote in ['"', "'"]):
                self.best_practices.append(f"Line {line_num}: Consider using join() or f-strings for string concatenation in loops")
        
        # Check for hardcoded values that could be constants
        magic_numbers = re.findall(r'\b\d{2,}\b', code)
        if magic_numbers:
            unique_numbers = set(magic_numbers)
            if len(unique_numbers) > 2:
                self.best_practices.append("Consider defining magic numbers as named constants for better readability")
        
        # Check for exception handling best practices
        if 'except:' in code:
            self.best_practices.append("Consider catching specific exceptions instead of using bare 'except:'")
        
        # Check for proper use of list comprehensions using AST
        if 'def ' in code or 'for ' in code:
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.For):
                        # Check if the loop body only contains simple append operations
                        if (len(node.body) == 1 and 
                            isinstance(node.body[0], ast.Expr) and
                            isinstance(node.body[0].value, ast.Call) and
                            isinstance(node.body[0].value.func, ast.Attribute) and
                            node.body[0].value.func.attr == 'append'):
                            self.best_practices.append("Consider using list comprehension for simple append operations")
            except:
                pass
        
        # Check for proper function documentation
        if 'def ' in code:
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        # Check if function has docstring using ast.get_docstring
                        if ast.get_docstring(node) is None:
                            self.best_practices.append(f"Function '{node.name}' could benefit from a docstring")
            except:
                pass
    
    def _check_complexity(self, code: str):
        """Check code complexity and suggest improvements"""
        lines = code.split('\n')
        
        # Count nested levels
        max_nesting = 0
        current_nesting = 0
        
        for line in lines:
            stripped = line.strip()
            if stripped:
                # Calculate indentation level
                indent_level = (len(line) - len(line.lstrip())) // 4
                
                if any(stripped.startswith(keyword) for keyword in ['if', 'for', 'while', 'try', 'with']):
                    current_nesting = indent_level + 1
                    max_nesting = max(max_nesting, current_nesting)
        
        if max_nesting > 3:
            self.suggestions.append(f"Consider breaking down complex nested code (nesting level: {max_nesting})")
        
        # Check function length
        function_lines = {}
        current_function = None
        
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith('def '):
                current_function = stripped.split('(')[0].replace('def ', '')
                function_lines[current_function] = [line_num]
            elif current_function and (not line.startswith(' ') or not stripped):
                if stripped and not line.startswith(' '):
                    current_function = None
            elif current_function:
                function_lines[current_function].append(line_num)
        
        for func_name, line_numbers in function_lines.items():
            if len(line_numbers) > 20:
                self.suggestions.append(f"Function '{func_name}' is quite long ({len(line_numbers)} lines). Consider breaking it into smaller functions")
    
    def _is_constant_assignment(self, line: str) -> bool:
        """Check if a line assigns a constant value"""
        # Simple heuristic: if right side is a literal
        if '=' in line:
            right_side = line.split('=', 1)[1].strip()
            # Check if it's a number, string, or simple expression
            return (right_side.isdigit() or 
                   right_side.startswith('"') or 
                   right_side.startswith("'") or
                   right_side in ['True', 'False', 'None'])
        return False
    
    def _calculate_quality_score(self) -> int:
        """Calculate a quality score from 0-100"""
        base_score = 100
        
        # Deduct points for issues
        base_score -= len(self.warnings) * 15  # Warnings are more serious
        base_score -= len(self.suggestions) * 5  # Suggestions are less serious
        base_score -= len(self.best_practices) * 3  # Best practices are educational
        
        return max(0, min(100, base_score))

def analyze_code_quality(code: str) -> Dict[str, Any]:
    """
    Public function to analyze code quality
    
    Args:
        code: Python code string to analyze
        
    Returns:
        Dictionary with analysis results
    """
    analyzer = CodeQualityAnalyzer()
    return analyzer.analyze_code(code)

def format_feedback(analysis: Dict[str, Any]) -> str:
    """
    Format the analysis results into a readable feedback string
    
    Args:
        analysis: Analysis results from analyze_code_quality
        
    Returns:
        Formatted feedback string
    """
    feedback = []
    
    # Add quality score
    score = analysis.get('score', 0)
    if score >= 90:
        feedback.append(f"🎉 Excellent code quality! Score: {score}/100")
    elif score >= 75:
        feedback.append(f"✅ Good code quality! Score: {score}/100")
    elif score >= 60:
        feedback.append(f"👍 Decent code quality. Score: {score}/100")
    else:
        feedback.append(f"⚠️ Code quality needs improvement. Score: {score}/100")
    
    # Add warnings
    if analysis.get('warnings'):
        feedback.append("\n🚨 **Issues to Fix:**")
        for warning in analysis['warnings']:
            feedback.append(f"• {warning}")
    
    # Add suggestions
    if analysis.get('suggestions'):
        feedback.append("\n💡 **Suggestions for Improvement:**")
        for suggestion in analysis['suggestions']:
            feedback.append(f"• {suggestion}")
    
    # Add best practices
    if analysis.get('best_practices'):
        feedback.append("\n📚 **Best Practices to Consider:**")
        for practice in analysis['best_practices']:
            feedback.append(f"• {practice}")
    
    return '\n'.join(feedback) if feedback else "✅ No issues found!"