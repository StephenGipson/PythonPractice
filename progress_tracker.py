"""
Progress tracking functionality for the Python practice platform
"""

import json
import os
from datetime import datetime

class ProgressTracker:
    def __init__(self, filename="progress.json"):
        self.filename = filename
        self.progress_data = self.load_progress()
    
    def load_progress(self):
        """Load progress data from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Return default structure if file doesn't exist or is corrupted
        return {
            "completed_exercises": [],
            "completion_dates": {},
            "total_attempts": {},
            "created_at": datetime.now().isoformat()
        }
    
    def save_progress(self):
        """Save progress data to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.progress_data, f, indent=2)
        except Exception as e:
            print(f"Error saving progress: {e}")
    
    def mark_completed(self, exercise_id):
        """Mark an exercise as completed"""
        if exercise_id not in self.progress_data["completed_exercises"]:
            self.progress_data["completed_exercises"].append(exercise_id)
            self.progress_data["completion_dates"][exercise_id] = datetime.now().isoformat()
        
        # Increment attempt count
        if exercise_id not in self.progress_data["total_attempts"]:
            self.progress_data["total_attempts"][exercise_id] = 0
        self.progress_data["total_attempts"][exercise_id] += 1
    
    def is_completed(self, exercise_id):
        """Check if an exercise is completed"""
        return exercise_id in self.progress_data["completed_exercises"]
    
    def get_completion_date(self, exercise_id):
        """Get the completion date for an exercise"""
        return self.progress_data["completion_dates"].get(exercise_id)
    
    def get_attempt_count(self, exercise_id):
        """Get the number of attempts for an exercise"""
        return self.progress_data["total_attempts"].get(exercise_id, 0)
    
    def get_progress_summary(self):
        """Get a summary of progress"""
        from exercises import get_all_exercise_ids
        
        all_exercise_ids = get_all_exercise_ids()
        completed_count = len(self.progress_data["completed_exercises"])
        total_count = len(all_exercise_ids)
        
        return {
            "completed": completed_count,
            "total": total_count,
            "percentage": (completed_count / total_count * 100) if total_count > 0 else 0,
            "completed_exercises": self.progress_data["completed_exercises"],
            "recent_completions": self._get_recent_completions()
        }
    
    def _get_recent_completions(self, limit=5):
        """Get recent completions"""
        completed_with_dates = []
        for exercise_id in self.progress_data["completed_exercises"]:
            date = self.progress_data["completion_dates"].get(exercise_id)
            if date:
                completed_with_dates.append((exercise_id, date))
        
        # Sort by date (most recent first)
        completed_with_dates.sort(key=lambda x: x[1], reverse=True)
        
        return completed_with_dates[:limit]
    
    def reset_progress(self):
        """Reset all progress"""
        self.progress_data = {
            "completed_exercises": [],
            "completion_dates": {},
            "total_attempts": {},
            "created_at": datetime.now().isoformat()
        }
        self.save_progress()
    
    def get_category_progress(self):
        """Get progress by category"""
        from exercises import get_exercises
        
        exercises = get_exercises()
        category_progress = {}
        
        for category, exercise_list in exercises.items():
            total_in_category = len(exercise_list)
            completed_in_category = sum(
                1 for exercise in exercise_list 
                if exercise['id'] in self.progress_data["completed_exercises"]
            )
            
            category_progress[category] = {
                "completed": completed_in_category,
                "total": total_in_category,
                "percentage": (completed_in_category / total_in_category * 100) if total_in_category > 0 else 0
            }
        
        return category_progress
