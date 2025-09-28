import streamlit as st
from streamlit_ace import st_ace
import sys
import io
import traceback
from exercises import get_exercises, get_exercise_by_id
from progress_tracker import ProgressTracker
from code_executor import execute_code
from code_quality import analyze_code_quality, format_feedback
from concept_explanations import get_category_concepts, get_enhanced_hints
from custom_exercises import CustomExerciseManager, get_difficulty_options, get_example_exercise_templates, validate_test_case
from specialized_tracks import get_specialized_tracks

# Initialize session state
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'custom_exercise_manager' not in st.session_state:
    st.session_state.custom_exercise_manager = CustomExerciseManager()

if 'current_exercise_id' not in st.session_state:
    st.session_state.current_exercise_id = None

if 'code_content' not in st.session_state:
    st.session_state.code_content = ""

if 'current_page' not in st.session_state:
    st.session_state.current_page = "exercises"

def main():
    st.set_page_config(
        page_title="Python Practice Platform",
        page_icon="🐍",
        layout="wide"
    )
    
    st.title("🐍 Interactive Python Practice Platform")
    st.markdown("Learn Python through hands-on coding exercises with instant feedback!")
    
    # Sidebar for navigation
    with st.sidebar:
        st.header("🧭 Navigation")
        
        # Page selection
        page_options = {
            "exercises": "📚 Practice Exercises",
            "custom_builder": "🔨 Create Exercise",
            "custom_list": "📝 My Exercises"
        }
        
        for page_key, page_name in page_options.items():
            if st.button(page_name, key=f"nav_{page_key}", use_container_width=True):
                st.session_state.current_page = page_key
                st.session_state.show_concepts = False
                st.rerun()
        
        st.divider()
        st.header("📚 Exercises")
        
        # Progress overview
        progress = st.session_state.progress_tracker.get_progress_summary()
        st.metric("Completed Exercises", progress['completed'])
        st.metric("Total Exercises", progress['total'])
        
        if progress['total'] > 0:
            progress_percentage = (progress['completed'] / progress['total']) * 100
            st.progress(progress_percentage / 100)
            st.write(f"Progress: {progress_percentage:.1f}%")
        
        st.divider()
        
        # Learning Resources section
        with st.expander("📚 Learning Resources"):
            st.markdown("**Quick Tips:**")
            hints = get_enhanced_hints()
            
            tip_type = st.selectbox(
                "Choose tip category:",
                ["debugging_tips", "problem_solving_strategies", "python_specific_tips"],
                format_func=lambda x: x.replace("_", " ").title()
            )
            
            for tip in hints[tip_type]:
                st.markdown(f"• {tip}")
        
        st.divider()
        
        # Exercise categories
        exercises = get_exercises()
        categories = list(exercises.keys())
        
        for category in categories:
            st.subheader(category.title())
            category_exercises = exercises[category]
            
            for exercise in category_exercises:
                # Check if exercise is completed
                is_completed = st.session_state.progress_tracker.is_completed(exercise['id'])
                status_icon = "✅" if is_completed else "⭕"
                
                if st.button(
                    f"{status_icon} {exercise['title']}", 
                    key=f"btn_{exercise['id']}",
                    use_container_width=True
                ):
                    # Reset state when switching exercises
                    if st.session_state.current_exercise_id != exercise['id']:
                        st.session_state.show_concepts = False
                    st.session_state.current_exercise_id = exercise['id']
                    st.session_state.code_content = exercise.get('starter_code', '')
                    st.rerun()
        
        # Specialized tracks
        st.divider()
        st.subheader("🎯 Specialized Tracks")
        
        specialized_tracks = get_specialized_tracks()
        for track_key, track_data in specialized_tracks.items():
            with st.expander(f"{track_data['icon']} {track_data['title']}"):
                st.markdown(track_data['description'])
                
                for exercise in track_data['exercises']:
                    is_completed = st.session_state.progress_tracker.is_completed(exercise['id'])
                    status_icon = "✅" if is_completed else "⭕"
                    
                    if st.button(
                        f"{status_icon} {exercise['title']}", 
                        key=f"btn_track_{exercise['id']}",
                        use_container_width=True
                    ):
                        # Reset state when switching exercises
                        if st.session_state.current_exercise_id != exercise['id']:
                            st.session_state.show_concepts = False
                        st.session_state.current_exercise_id = exercise['id']
                        st.session_state.code_content = exercise.get('starter_code', '')
                        st.rerun()
    
    # Main content area
    if st.session_state.current_page == "exercises":
        if st.session_state.current_exercise_id:
            display_exercise()
        else:
            display_welcome()
    elif st.session_state.current_page == "custom_builder":
        display_exercise_builder()
    elif st.session_state.current_page == "custom_list":
        display_custom_exercises()

def display_welcome():
    st.markdown("""
    ## Welcome to the Python Practice Platform! 🎯
    
    This interactive platform helps you learn Python programming through hands-on exercises.
    
    ### Features:
    - 📝 **Interactive Code Editor** with syntax highlighting
    - ⚡ **Instant Feedback** - Run your code and see results immediately
    - 📊 **Progress Tracking** - Keep track of completed exercises
    - 🎯 **Structured Learning** - Exercises organized by difficulty level
    - 🔍 **Error Handling** - Clear error messages to help you debug
    - 🔍 **Code Quality Analysis** - Get feedback on your coding style
    - 📚 **Concept Explanations** - Learn Python concepts as you practice
    
    ### Getting Started:
    1. Choose an exercise from the sidebar
    2. Read the instructions carefully
    3. Write your code in the editor
    4. Click "Run Code" to test your solution
    5. Use the "Submit Solution" button when you're confident in your answer
    6. Check code quality and learn concepts for deeper understanding
    
    **Select an exercise from the sidebar to begin your Python journey!**
    """)

def display_concept_explanations(difficulty):
    """Display concept explanations for the given difficulty level"""
    st.markdown("---")
    st.markdown("### 📚 Related Python Concepts")
    
    concepts = get_category_concepts(difficulty)
    
    if not concepts:
        st.info("No specific concept explanations available for this category yet.")
        return
    
    # Create tabs for different concepts
    concept_tabs = st.tabs([concept['title'] for concept in concepts])
    
    for i, concept in enumerate(concepts):
        with concept_tabs[i]:
            # Display the main explanation
            st.markdown(concept['explanation'])
            
            # Display examples if available
            if 'examples' in concept:
                st.markdown("#### 💻 Examples")
                for example in concept['examples']:
                    with st.expander(f"📝 {example['title']}"):
                        st.code(example['code'], language='python')
            
            # Display common mistakes if available
            if 'common_mistakes' in concept:
                st.markdown("#### ⚠️ Common Mistakes to Avoid")
                for mistake in concept['common_mistakes']:
                    st.markdown(f"• {mistake}")
    
    st.markdown("---")

def display_exercise():
    exercise_id = st.session_state.current_exercise_id
    
    # Try to get from built-in exercises first
    exercise = get_exercise_by_id(exercise_id)
    
    # If not found, try custom exercises
    if not exercise and exercise_id.startswith('custom_'):
        exercise = st.session_state.custom_exercise_manager.get_exercise_by_id(exercise_id)
    
    # If not found, try specialized tracks
    if not exercise:
        specialized_tracks = get_specialized_tracks()
        for track_data in specialized_tracks.values():
            for track_exercise in track_data['exercises']:
                if track_exercise['id'] == exercise_id:
                    exercise = track_exercise
                    break
            if exercise:
                break
    
    if not exercise:
        st.error("Exercise not found!")
        return
    
    # Exercise header
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.header(f"📝 {exercise['title']}")
        st.markdown(f"**Difficulty:** {exercise['difficulty'].title()}")
    
    with col2:
        is_completed = st.session_state.progress_tracker.is_completed(exercise['id'])
        if is_completed:
            st.success("✅ Completed")
        else:
            st.info("⭕ Not Completed")
    
    with col3:
        # Add concept explanations button
        if st.button("📖 Learn Concepts"):
            st.session_state.show_concepts = not st.session_state.get('show_concepts', False)
            st.rerun()
    
    # Show concept explanations if requested
    if st.session_state.get('show_concepts', False):
        display_concept_explanations(exercise['difficulty'])
    
    # Exercise description
    st.markdown("### 📋 Instructions")
    st.markdown(exercise['description'])
    
    if 'example' in exercise:
        st.markdown("### 💡 Example")
        st.code(exercise['example'], language='python')
    
    if 'hint' in exercise:
        with st.expander("💭 Need a hint?"):
            st.markdown(exercise['hint'])
    
    # Code editor
    st.markdown("### 💻 Your Code")
    
    # Initialize code content if not set
    if not st.session_state.code_content and 'starter_code' in exercise:
        st.session_state.code_content = exercise['starter_code']
    
    # Code editor
    code = st_ace(
        value=st.session_state.code_content,
        language='python',
        theme='monokai',
        key=f"editor_{exercise['id']}",
        height=300,
        auto_update=True,
        font_size=14,
        wrap=False,
        annotations=None
    )
    
    # Update session state
    st.session_state.code_content = code
    
    # Action buttons
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        if st.button("▶️ Run Code", type="primary"):
            run_code(code, exercise)
    
    with col2:
        if st.button("✅ Submit Solution"):
            submit_solution(code, exercise)
    
    with col3:
        if st.button("🔍 Check Quality"):
            check_code_quality(code)
    
    with col4:
        if st.button("🔄 Reset Code"):
            st.session_state.code_content = exercise.get('starter_code', '')
            st.rerun()

def run_code(code, exercise):
    """Execute the code and display output"""
    if not code.strip():
        st.warning("Please write some code before running!")
        return
    
    st.markdown("### 📤 Output")
    
    try:
        # Execute the code
        result = execute_code(code)
        
        if result['success']:
            if result['output']:
                st.code(result['output'], language='text')
            else:
                st.info("Code executed successfully (no output)")
        else:
            st.error("**Error occurred:**")
            st.code(result['error'], language='text')
            
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")

def check_code_quality(code):
    """Analyze code quality and provide feedback"""
    if not code.strip():
        st.warning("Please write some code before checking quality!")
        return
    
    st.markdown("### 🔍 Code Quality Analysis")
    
    with st.spinner("Analyzing your code..."):
        try:
            # Analyze code quality
            analysis = analyze_code_quality(code)
            feedback = format_feedback(analysis)
            
            # Display the formatted feedback
            st.markdown(feedback)
            
            # Show score with color coding
            score = analysis.get('score', 0)
            if score >= 90:
                st.success(f"Outstanding! Your code quality score is {score}/100")
            elif score >= 75:
                st.info(f"Good work! Your code quality score is {score}/100")
            elif score >= 60:
                st.warning(f"Not bad! Your code quality score is {score}/100 - room for improvement")
            else:
                st.error(f"Code quality score: {score}/100 - consider the suggestions above")
                
        except Exception as e:
            st.error(f"Error analyzing code quality: {str(e)}")

def submit_solution(code, exercise):
    """Submit and validate the solution"""
    if not code.strip():
        st.warning("Please write some code before submitting!")
        return
    
    # Execute the code first
    result = execute_code(code)
    
    if not result['success']:
        st.error("Your code has errors. Please fix them before submitting.")
        st.code(result['error'], language='text')
        return
    
    # Check if exercise has test cases
    if 'test_cases' in exercise:
        passed_tests = 0
        total_tests = len(exercise['test_cases'])
        
        st.markdown("### 🧪 Running Tests...")
        
        for i, test_case in enumerate(exercise['test_cases']):
            test_code = code + "\n" + test_case['test']
            test_result = execute_code(test_code)
            
            if test_result['success']:
                expected = test_case.get('expected', '')
                actual = test_result['output'].strip()
                
                # Check if this is an assertion-based test (no expected output)
                if not expected or expected.lower() in ['', 'none', 'no output']:
                    # For assertion-based tests, success means the test passed
                    st.success(f"✅ Test {i+1}: Passed (assertion test)")
                    passed_tests += 1
                elif actual == expected:
                    # For output-comparison tests
                    st.success(f"✅ Test {i+1}: Passed")
                    passed_tests += 1
                else:
                    st.error(f"❌ Test {i+1}: Failed")
                    st.write(f"Expected: `{expected}`")
                    st.write(f"Got: `{actual}`")
            else:
                # Check if this is an assertion error (expected for assertion tests)
                if 'AssertionError' in test_result['error']:
                    st.error(f"❌ Test {i+1}: Assertion failed")
                    st.code(test_result['error'], language='text')
                else:
                    st.error(f"❌ Test {i+1}: Error occurred")
                    st.code(test_result['error'], language='text')
        
        # Check if all tests passed
        if passed_tests == total_tests:
            st.balloons()
            st.success(f"🎉 Congratulations! All {total_tests} tests passed!")
            st.session_state.progress_tracker.mark_completed(exercise['id'])
            st.session_state.progress_tracker.save_progress()
            
            # Provide code quality feedback on successful completion
            with st.expander("📊 Code Quality Feedback"):
                try:
                    analysis = analyze_code_quality(code)
                    feedback = format_feedback(analysis)
                    st.markdown(feedback)
                except Exception as e:
                    st.info("Code quality analysis not available for this submission.")
        else:
            st.warning(f"You passed {passed_tests}/{total_tests} tests. Keep trying!")
    
    else:
        # No test cases, just mark as completed if code runs
        st.success("🎉 Solution submitted successfully!")
        st.session_state.progress_tracker.mark_completed(exercise['id'])
        st.session_state.progress_tracker.save_progress()
        
        # Provide code quality feedback
        with st.expander("📊 Code Quality Feedback"):
            try:
                analysis = analyze_code_quality(code)
                feedback = format_feedback(analysis)
                st.markdown(feedback)
            except Exception as e:
                st.info("Code quality analysis not available for this submission.")

def display_exercise_builder():
    """Display the custom exercise builder interface"""
    st.header("🔨 Create Your Own Exercise")
    st.markdown("Design custom Python coding challenges for yourself and others!")
    
    # Template selection
    with st.expander("📝 Use a Template (Optional)"):
        templates = get_example_exercise_templates()
        template_names = ["None"] + list(templates.keys())
        selected_template = st.selectbox(
            "Choose a template to start with:",
            template_names,
            format_func=lambda x: x.replace("_", " ").title() if x != "None" else "Start from scratch"
        )
        
        if selected_template != "None" and st.button("Load Template"):
            template_data = templates[selected_template]
            for key, value in template_data.items():
                if key == "test_cases":
                    st.session_state[f"builder_{key}"] = "\n".join([f"# Test {i+1}:\n{tc['test']}\n# Expected: {tc['expected']}\n" for i, tc in enumerate(value)])
                else:
                    st.session_state[f"builder_{key}"] = value
            st.success("Template loaded! You can modify the fields below.")
    
    # Exercise creation form
    with st.form("exercise_builder"):
        st.subheader("Exercise Details")
        
        # Basic information
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input(
                "Exercise Title*",
                value=st.session_state.get('builder_title', ''),
                placeholder="e.g., Calculate Average Grade"
            )
        
        with col2:
            difficulty = st.selectbox(
                "Difficulty Level*",
                get_difficulty_options(),
                index=get_difficulty_options().index(st.session_state.get('builder_difficulty', 'beginner'))
            )
        
        # Description
        description = st.text_area(
            "Exercise Description*",
            value=st.session_state.get('builder_description', ''),
            placeholder="Describe what the student needs to implement...",
            height=100
        )
        
        # Code components
        col1, col2 = st.columns(2)
        with col1:
            starter_code = st.text_area(
                "Starter Code (Optional)",
                value=st.session_state.get('builder_starter_code', '# Write your code here\n'),
                placeholder="Provide initial code structure...",
                height=100
            )
        
        with col2:
            example = st.text_area(
                "Example Solution (Optional)",
                value=st.session_state.get('builder_example', ''),
                placeholder="Show a sample solution...",
                height=100
            )
        
        # Hint and tags
        hint = st.text_input(
            "Hint (Optional)",
            value=st.session_state.get('builder_hint', ''),
            placeholder="Give students a helpful hint..."
        )
        
        tags = st.text_input(
            "Tags (Optional)",
            value=st.session_state.get('builder_tags', ''),
            placeholder="loops, functions, lists (comma-separated)"
        )
        
        # Test cases
        st.subheader("Test Cases (Optional)")
        st.markdown("""
        **Test Case Formats:**
        - **Assertion tests** (recommended): `assert function_name(args) == expected`
        - **Output tests**: Use `print(result)` and specify expected output
        """)
        test_cases_text = st.text_area(
            "Test Cases",
            value=st.session_state.get('builder_test_cases', ''),
            placeholder="# Test 1 - Assertion based (recommended):\nresult = my_function(5, 3)\nassert result == 8\n# Expected: \n\n# Test 2 - Output based:\nprint(my_function(10, 2))\n# Expected: 5",
            height=120,
            help="Write Python test code. For assertion tests, leave Expected empty. For output tests, specify what should be printed."
        )
        
        # Submit button
        submitted = st.form_submit_button("✨ Create Exercise", type="primary")
        
        if submitted:
            # Validate required fields
            if not title.strip() or not description.strip():
                st.error("Please fill in all required fields (marked with *)")
            else:
                # Parse test cases
                test_cases = []
                if test_cases_text.strip():
                    try:
                        # Simple parsing of test cases
                        lines = test_cases_text.strip().split('\n')
                        current_test = ""
                        current_expected = ""
                        
                        for line in lines:
                            line = line.strip()
                            if line.startswith('# Expected:'):
                                current_expected = line.replace('# Expected:', '').strip()
                                if current_test:
                                    test_cases.append({
                                        "test": current_test,
                                        "expected": current_expected
                                    })
                                current_test = ""
                            elif line.startswith('#'):
                                # Start of new test case
                                current_test = ""
                            elif line and not line.startswith('#'):
                                current_test += line + "\n"
                    except Exception as e:
                        st.warning("Could not parse test cases. Exercise created without tests.")
                
                # Prepare exercise data
                exercise_data = {
                    "title": title,
                    "difficulty": difficulty,
                    "description": description,
                    "starter_code": starter_code,
                    "example": example,
                    "hint": hint,
                    "test_cases": test_cases,
                    "tags": [tag.strip() for tag in tags.split(',') if tag.strip()]
                }
                
                # Add exercise
                if st.session_state.custom_exercise_manager.add_exercise(exercise_data):
                    st.success("🎉 Exercise created successfully!")
                    # Clear form
                    for key in list(st.session_state.keys()):
                        if isinstance(key, str) and key.startswith('builder_'):
                            del st.session_state[key]
                    st.rerun()
                else:
                    st.error("Failed to create exercise. Please check your input.")

def display_custom_exercises():
    """Display the list of custom exercises"""
    st.header("📝 My Custom Exercises")
    
    custom_exercises = st.session_state.custom_exercise_manager.get_all_custom_exercises()
    
    if not custom_exercises:
        st.info("No custom exercises yet. Create your first exercise using the Exercise Builder!")
        if st.button("🔨 Create Exercise"):
            st.session_state.current_page = "custom_builder"
            st.rerun()
        return
    
    # Search and filter
    col1, col2 = st.columns([2, 1])
    with col1:
        search_query = st.text_input("🔍 Search exercises", placeholder="Search by title, description, or tags...")
    
    with col2:
        filter_difficulty = st.selectbox("Filter by difficulty", ["All"] + get_difficulty_options())
    
    # Apply filters
    filtered_exercises = custom_exercises
    
    if search_query:
        filtered_exercises = st.session_state.custom_exercise_manager.search_exercises(search_query)
    
    if filter_difficulty != "All":
        filtered_exercises = [ex for ex in filtered_exercises if ex['difficulty'] == filter_difficulty.lower()]
    
    # Display exercises
    if not filtered_exercises:
        st.info("No exercises match your search criteria.")
        return
    
    st.markdown(f"Showing {len(filtered_exercises)} exercise(s)")
    
    for exercise in filtered_exercises:
        with st.expander(f"{exercise['title']} ({exercise['difficulty'].title()})"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**Description:** {exercise['description'][:200]}...")
                if exercise.get('tags'):
                    tags_str = ", ".join(exercise['tags'])
                    st.markdown(f"**Tags:** {tags_str}")
                st.markdown(f"**Created:** {exercise['created_at'][:10]}")
            
            with col2:
                if st.button("📝 Practice", key=f"practice_{exercise['id']}"):
                    # Switch to this custom exercise
                    st.session_state.current_page = "exercises"
                    st.session_state.current_exercise_id = exercise['id']
                    st.session_state.code_content = exercise.get('starter_code', '')
                    st.rerun()
                
                if st.button("🗑️ Delete", key=f"delete_{exercise['id']}"):
                    if st.session_state.custom_exercise_manager.delete_exercise(exercise['id']):
                        st.success("Exercise deleted!")
                        st.rerun()
                    else:
                        st.error("Failed to delete exercise.")

if __name__ == "__main__":
    main()
