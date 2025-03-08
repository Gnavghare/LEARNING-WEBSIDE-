import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from learning_content.models import Category, Course, Lesson, Quiz, Question, Answer
from django.contrib.auth.models import User
from django.utils.text import slugify

def create_sample_data():
    # Create categories
    categories = [
        {
            'name': 'Programming',
            'description': 'Learn programming languages and software development.'
        },
        {
            'name': 'Data Science',
            'description': 'Explore data analysis, machine learning, and statistics.'
        },
        {
            'name': 'Web Development',
            'description': 'Build websites and web applications using modern technologies.'
        },
        {
            'name': 'Mobile Development',
            'description': 'Create mobile applications for iOS and Android platforms.'
        }
    ]
    
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'slug': slugify(category_data['name']),
                'description': category_data['description']
            }
        )
        print(f"Category {'created' if created else 'already exists'}: {category.name}")
    
    # Get categories
    programming = Category.objects.get(name='Programming')
    data_science = Category.objects.get(name='Data Science')
    web_dev = Category.objects.get(name='Web Development')
    mobile_dev = Category.objects.get(name='Mobile Development')
    
    # Create courses
    courses = [
        {
            'title': 'Python for Beginners',
            'description': 'Learn the basics of Python programming language. This course covers variables, data types, control structures, functions, and more.',
            'category': programming,
            'level': 'beginner',
            'is_featured': True,
            'is_published': True
        },
        {
            'title': 'Advanced JavaScript',
            'description': 'Take your JavaScript skills to the next level. Learn about closures, prototypes, async/await, and modern ES6+ features.',
            'category': programming,
            'level': 'advanced',
            'is_featured': False,
            'is_published': True
        },
        {
            'title': 'Introduction to Machine Learning',
            'description': 'Get started with machine learning concepts and algorithms. Learn about supervised and unsupervised learning, regression, classification, and clustering.',
            'category': data_science,
            'level': 'intermediate',
            'is_featured': True,
            'is_published': True
        },
        {
            'title': 'React.js Fundamentals',
            'description': 'Learn how to build modern user interfaces with React.js. This course covers components, props, state, hooks, and more.',
            'category': web_dev,
            'level': 'intermediate',
            'is_featured': True,
            'is_published': True
        },
        {
            'title': 'Flutter App Development',
            'description': 'Build cross-platform mobile applications with Flutter. Learn Dart programming language and Flutter widgets to create beautiful UIs.',
            'category': mobile_dev,
            'level': 'beginner',
            'is_featured': False,
            'is_published': True
        }
    ]
    
    for course_data in courses:
        course, created = Course.objects.get_or_create(
            title=course_data['title'],
            defaults={
                'slug': slugify(course_data['title']),
                'description': course_data['description'],
                'category': course_data['category'],
                'level': course_data['level'],
                'is_featured': course_data['is_featured'],
                'is_published': course_data['is_published']
            }
        )
        print(f"Course {'created' if created else 'already exists'}: {course.title}")
    
    # Create lessons for Python course
    python_course = Course.objects.get(title='Python for Beginners')
    python_lessons = [
        {
            'title': 'Introduction to Python',
            'content': '<p>Python is a high-level, interpreted programming language known for its readability and simplicity.</p><h3>Why Learn Python?</h3><ul><li>Easy to learn and use</li><li>Versatile and widely used</li><li>Large community and extensive libraries</li></ul>',
            'order': 1
        },
        {
            'title': 'Variables and Data Types',
            'content': '<p>In this lesson, we\'ll learn about variables and the basic data types in Python.</p><h3>Python Data Types:</h3><ul><li>Integers</li><li>Floats</li><li>Strings</li><li>Booleans</li><li>Lists</li><li>Tuples</li><li>Dictionaries</li></ul>',
            'order': 2
        },
        {
            'title': 'Control Structures',
            'content': '<p>Control structures allow you to control the flow of your program.</p><h3>Types of Control Structures:</h3><ul><li>Conditional statements (if, elif, else)</li><li>Loops (for, while)</li></ul>',
            'order': 3
        }
    ]
    
    for lesson_data in python_lessons:
        lesson, created = Lesson.objects.get_or_create(
            title=lesson_data['title'],
            course=python_course,
            defaults={
                'slug': slugify(lesson_data['title']),
                'content': lesson_data['content'],
                'order': lesson_data['order'],
                'is_published': True
            }
        )
        print(f"Lesson {'created' if created else 'already exists'}: {lesson.title}")
    
    # Create a quiz for the first lesson
    intro_lesson = Lesson.objects.get(title='Introduction to Python')
    quiz, created = Quiz.objects.get_or_create(
        lesson=intro_lesson,
        defaults={
            'title': 'Python Basics Quiz',
            'description': 'Test your knowledge of Python basics.'
        }
    )
    print(f"Quiz {'created' if created else 'already exists'}: {quiz.title}")
    
    # Create questions for the quiz
    questions_data = [
        {
            'text': 'What is Python?',
            'answers': [
                {'text': 'A high-level programming language', 'is_correct': True},
                {'text': 'A type of snake', 'is_correct': False},
                {'text': 'A database management system', 'is_correct': False},
                {'text': 'A web browser', 'is_correct': False}
            ]
        },
        {
            'text': 'Who created Python?',
            'answers': [
                {'text': 'Guido van Rossum', 'is_correct': True},
                {'text': 'Bill Gates', 'is_correct': False},
                {'text': 'Mark Zuckerberg', 'is_correct': False},
                {'text': 'Linus Torvalds', 'is_correct': False}
            ]
        },
        {
            'text': 'What is the correct file extension for Python files?',
            'answers': [
                {'text': '.py', 'is_correct': True},
                {'text': '.python', 'is_correct': False},
                {'text': '.pt', 'is_correct': False},
                {'text': '.p', 'is_correct': False}
            ]
        }
    ]
    
    for question_data in questions_data:
        question, created = Question.objects.get_or_create(
            text=question_data['text'],
            quiz=quiz
        )
        print(f"Question {'created' if created else 'already exists'}: {question.text}")
        
        for answer_data in question_data['answers']:
            answer, created = Answer.objects.get_or_create(
                text=answer_data['text'],
                question=question,
                defaults={
                    'is_correct': answer_data['is_correct']
                }
            )
            print(f"Answer {'created' if created else 'already exists'}: {answer.text}")

if __name__ == '__main__':
    create_sample_data()
    print("Sample data creation completed!") 