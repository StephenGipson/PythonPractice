# Overview

This is an Interactive Python Practice Platform built with Streamlit that provides a comprehensive learning environment for Python programming. The platform offers hands-on coding exercises with instant feedback, code quality analysis, and progress tracking. It features a multi-tier exercise system ranging from beginner to advanced levels, custom exercise creation capabilities, and specialized learning tracks for data science and web development.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The application uses **Streamlit** as the primary web framework, providing an interactive single-page application interface. The UI is organized into multiple pages using Streamlit's sidebar navigation:
- Practice Exercises page for solving coding challenges
- Custom Exercise Builder for creating new exercises
- Exercise management for viewing user-created content

The frontend integrates **streamlit-ace** for an enhanced code editing experience, providing syntax highlighting and a professional code editor interface within the browser.

## Core Application Structure
The system follows a **modular architecture** with clear separation of concerns:
- `app.py` serves as the main application controller and UI orchestrator
- Individual modules handle specific functionalities (exercises, progress tracking, code execution)
- Session state management maintains user context across interactions

## Code Execution Engine
A **sandboxed code execution system** (`code_executor.py`) safely runs user-submitted Python code with:
- Timeout protection to prevent infinite loops
- Output capture and redirection
- Error handling and traceback generation
- Isolated execution environment for security

## Exercise Management System
The platform implements a **dual exercise system**:
- **Predefined exercises** stored in Python data structures with categorization by difficulty
- **Custom exercise builder** allowing users to create, save, and share their own exercises
- JSON-based persistence for custom exercises with validation and test case management

## Progress Tracking
A **file-based progress tracking system** (`progress_tracker.py`) maintains user learning history:
- Exercise completion status and timestamps
- Attempt counting and success metrics
- JSON persistence for data durability
- Session state integration for real-time updates

## Code Quality Analysis
An **integrated code quality analyzer** (`code_quality.py`) provides educational feedback:
- AST-based code parsing for structural analysis
- Best practices suggestions and style recommendations
- Naming convention validation
- Complexity analysis and improvement suggestions

## Educational Content System
The platform includes a **concept explanation engine** (`concept_explanations.py`) that provides:
- Contextual learning materials organized by topic
- Interactive hints and guidance
- Enhanced explanations tied to specific exercise categories

## Specialized Learning Tracks
A **modular track system** (`specialized_tracks.py`) offers focused learning paths:
- Data science exercises with real-world datasets
- Web development challenges
- Domain-specific problem sets with practical applications

# External Dependencies

## Core Framework Dependencies
- **Streamlit**: Web application framework for the user interface
- **streamlit-ace**: Advanced code editor component for syntax highlighting and code editing

## Python Standard Library Usage
- **ast**: Abstract syntax tree parsing for code quality analysis
- **json**: Data serialization for progress tracking and custom exercises
- **io**: Stream handling for code execution output capture
- **sys**: System-specific parameters and functions for output redirection
- **signal**: Unix signal handling for code execution timeouts
- **traceback**: Exception handling and error reporting
- **contextlib**: Context management utilities
- **datetime**: Timestamp generation for progress tracking
- **re**: Regular expression operations for code analysis

## File System Integration
- **Local JSON files**: Progress tracking (`progress.json`) and custom exercises (`custom_exercises.json`)
- **File-based persistence**: No external database required, using local storage for data persistence

The architecture prioritizes simplicity and self-containment, avoiding complex external dependencies while providing a rich learning experience through Python's extensive standard library.