import os
import django
import re
import html

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from learning_content.models import Course, Lesson, Quiz, Question, Answer
from django.utils.text import slugify

# Get the course by ID
course = Course.objects.get(id=12)  # Algorithms and Data Structures course
print(f"Fixing content and quizzes for course: {course.title}")

# Function to clean text by removing escape characters
def clean_text(text):
    if not text:
        return ""
    
    # Unescape HTML entities
    text = html.unescape(text)
    
    # Remove any remaining escape sequences
    text = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace("\\'", "'")
    
    return text

# Clean the course description
course.description = clean_text(course.description)
course.save()
print("Cleaned course description")

# Get all lessons for this course
lessons = Lesson.objects.filter(course=course).order_by('order')
print(f"Found {len(lessons)} lessons for this course")

# Clean each lesson's content and ensure quiz references are correct
for lesson in lessons:
    print(f"Processing lesson: {lesson.title}")
    
    # Clean the lesson content
    lesson.content = clean_text(lesson.content)
    
    # Check if this lesson has a quiz
    try:
        quiz = Quiz.objects.get(lesson=lesson)
        print(f"Found quiz: {quiz.title} with {quiz.questions.count()} questions")
        
        # Add a section at the end of the lesson content that lists all quiz questions
        quiz_content = f"\n\n## Quiz: {quiz.title}\n\n"
        quiz_content += f"{quiz.description}\n\n"
        
        # Add each question and its choices
        for i, question in enumerate(quiz.questions.all()):
            quiz_content += f"### Question {i+1}: {question.text}\n\n"
            
            for j, answer in enumerate(question.answers.all()):
                correct_marker = "✓" if answer.is_correct else ""
                quiz_content += f"- {answer.text} {correct_marker}\n"
            
            quiz_content += "\n"
        
        # Append the quiz content to the lesson
        if "## Quiz" not in lesson.content:
            lesson.content += quiz_content
            print("Added quiz content to lesson")
    
    except Quiz.DoesNotExist:
        print(f"No quiz found for lesson: {lesson.title}")
    
    # Save the updated lesson content
    lesson.save()
    print(f"Saved cleaned content for lesson: {lesson.title}")

# Update the overview lesson
try:
    overview_lesson = Lesson.objects.get(course=course, slug='algorithms-and-data-structures-overview')
    overview_lesson.content = clean_text(overview_lesson.content)
    
    # Add a section about quizzes
    if "## Quizzes" not in overview_lesson.content:
        quiz_section = """
## Quizzes

Each topic in this course includes a quiz to test your understanding. The quizzes are designed to reinforce key concepts and help you assess your knowledge. After studying each topic, make sure to complete the corresponding quiz to solidify your learning.

Quiz topics include:
"""
        
        # List all quizzes
        quizzes = Quiz.objects.filter(lesson__course=course)
        for quiz in quizzes:
            quiz_section += f"- {quiz.title} ({quiz.questions.count()} questions)\n"
        
        overview_lesson.content += quiz_section
        print("Added quiz section to overview lesson")
    
    overview_lesson.save()
    print("Cleaned overview lesson content")
    
except Lesson.DoesNotExist:
    print("Overview lesson not found")

print("Course content has been cleaned and quizzes have been properly integrated for the 'Algorithms and Data Structures' course.") 