import os
import django

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from django.utils import timezone
from learning_content.models import Course, Lesson, Quiz, Question, Answer
from django.utils.text import slugify

# Get the Android Development with Kotlin course
try:
    course = Course.objects.get(slug='android-development-with-kotlin')
    print(f"Adding quizzes to course: {course.title}")
except Course.DoesNotExist:
    print("Android Development with Kotlin course not found.")
    exit(1)

# Define quizzes for Android Development
quizzes_data = [
    {
        'title': 'Kotlin Basics Quiz',
        'lesson_title': 'Kotlin Basics',
        'questions': [
            {
                'text': 'Which keyword is used to declare a variable in Kotlin that can be reassigned?',
                'choices': [
                    {'text': 'val', 'is_correct': False},
                    {'text': 'var', 'is_correct': True},
                    {'text': 'const', 'is_correct': False},
                    {'text': 'let', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the correct way to declare a nullable string in Kotlin?',
                'choices': [
                    {'text': 'String?', 'is_correct': True},
                    {'text': 'String?:', 'is_correct': False},
                    {'text': 'Nullable<String>', 'is_correct': False},
                    {'text': 'Optional<String>', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is a Kotlin feature not present in Java?',
                'choices': [
                    {'text': 'Inheritance', 'is_correct': False},
                    {'text': 'Extension functions', 'is_correct': True},
                    {'text': 'Interfaces', 'is_correct': False},
                    {'text': 'Generics', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the Kotlin equivalent of Java\'s "static" keyword?',
                'choices': [
                    {'text': 'static', 'is_correct': False},
                    {'text': 'companion object', 'is_correct': True},
                    {'text': 'final', 'is_correct': False},
                    {'text': 'global', 'is_correct': False}
                ]
            },
            {
                'text': 'Which collection in Kotlin is immutable by default?',
                'choices': [
                    {'text': 'ArrayList', 'is_correct': False},
                    {'text': 'HashMap', 'is_correct': False},
                    {'text': 'List', 'is_correct': True},
                    {'text': 'Set', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the correct way to handle null safety in Kotlin?',
                'choices': [
                    {'text': 'Using try-catch blocks', 'is_correct': False},
                    {'text': 'Using the safe call operator (?.) or Elvis operator (?:)', 'is_correct': True},
                    {'text': 'Using the null keyword', 'is_correct': False},
                    {'text': 'Using the Optional class', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a coroutine in Kotlin?',
                'choices': [
                    {'text': 'A type of variable', 'is_correct': False},
                    {'text': 'A design pattern', 'is_correct': False},
                    {'text': 'A lightweight thread for asynchronous programming', 'is_correct': True},
                    {'text': 'A type of function that cannot be overridden', 'is_correct': False}
                ]
            },
            {
                'text': 'Which function is used to convert a nullable type to a non-nullable type in Kotlin?',
                'choices': [
                    {'text': 'toNonNull()', 'is_correct': False},
                    {'text': 'unwrap()', 'is_correct': False},
                    {'text': '!!', 'is_correct': True},
                    {'text': 'nonNull()', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of the "data" class in Kotlin?',
                'choices': [
                    {'text': 'To store only primitive data types', 'is_correct': False},
                    {'text': 'To automatically generate equals(), hashCode(), toString(), and copy() methods', 'is_correct': True},
                    {'text': 'To create a database connection', 'is_correct': False},
                    {'text': 'To define static variables', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the difference between val and const val in Kotlin?',
                'choices': [
                    {'text': 'There is no difference', 'is_correct': False},
                    {'text': 'val is runtime constant, const val is compile-time constant', 'is_correct': True},
                    {'text': 'val is for primitives, const val is for objects', 'is_correct': False},
                    {'text': 'val is immutable, const val is mutable', 'is_correct': False}
                ]
            }
        ]
    },
    {
        'title': 'Android UI Components Quiz',
        'lesson_title': 'Android UI Components',
        'questions': [
            {
                'text': 'Which layout arranges its children in a single horizontal or vertical row?',
                'choices': [
                    {'text': 'FrameLayout', 'is_correct': False},
                    {'text': 'LinearLayout', 'is_correct': True},
                    {'text': 'RelativeLayout', 'is_correct': False},
                    {'text': 'ConstraintLayout', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of RecyclerView in Android?',
                'choices': [
                    {'text': 'To display a scrollable list of elements', 'is_correct': True},
                    {'text': 'To recycle unused resources', 'is_correct': False},
                    {'text': 'To handle user input', 'is_correct': False},
                    {'text': 'To manage background processes', 'is_correct': False}
                ]
            },
            {
                'text': 'Which component is used to navigate between different screens in an Android app?',
                'choices': [
                    {'text': 'Intent', 'is_correct': True},
                    {'text': 'Activity', 'is_correct': False},
                    {'text': 'Fragment', 'is_correct': False},
                    {'text': 'View', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of ViewHolder pattern in RecyclerView?',
                'choices': [
                    {'text': 'To hold the view hierarchy of each item', 'is_correct': True},
                    {'text': 'To create new views', 'is_correct': False},
                    {'text': 'To handle click events', 'is_correct': False},
                    {'text': 'To manage the adapter', 'is_correct': False}
                ]
            },
            {
                'text': 'Which XML attribute is used to set the width of a view to match its parent?',
                'choices': [
                    {'text': 'android:width="match_parent"', 'is_correct': False},
                    {'text': 'android:layout_width="match_parent"', 'is_correct': True},
                    {'text': 'android:width="fill_parent"', 'is_correct': False},
                    {'text': 'android:layout_width="fill"', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of ConstraintLayout in Android?',
                'choices': [
                    {'text': 'To create flat view hierarchies', 'is_correct': True},
                    {'text': 'To constrain the user from modifying the UI', 'is_correct': False},
                    {'text': 'To limit the number of views', 'is_correct': False},
                    {'text': 'To create 3D layouts', 'is_correct': False}
                ]
            },
            {
                'text': 'Which component is used to display a modal dialog in Android?',
                'choices': [
                    {'text': 'AlertDialog', 'is_correct': True},
                    {'text': 'ModalView', 'is_correct': False},
                    {'text': 'PopupWindow', 'is_correct': False},
                    {'text': 'DialogFragment', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of the Adapter in ListView or RecyclerView?',
                'choices': [
                    {'text': 'To adapt the app to different screen sizes', 'is_correct': False},
                    {'text': 'To connect the data source to the view', 'is_correct': True},
                    {'text': 'To handle user interactions', 'is_correct': False},
                    {'text': 'To manage the layout', 'is_correct': False}
                ]
            },
            {
                'text': 'Which component is used to display images in Android?',
                'choices': [
                    {'text': 'ImageView', 'is_correct': True},
                    {'text': 'PictureView', 'is_correct': False},
                    {'text': 'PhotoView', 'is_correct': False},
                    {'text': 'GraphicsView', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of the Fragment in Android?',
                'choices': [
                    {'text': 'To fragment the application into multiple APKs', 'is_correct': False},
                    {'text': 'To represent a portion of the user interface in an Activity', 'is_correct': True},
                    {'text': 'To break down complex layouts', 'is_correct': False},
                    {'text': 'To manage background tasks', 'is_correct': False}
                ]
            }
        ]
    },
    {
        'title': 'Android Lifecycle Quiz',
        'lesson_title': 'Android Lifecycle',
        'questions': [
            {
                'text': 'Which lifecycle method is called when an activity becomes visible to the user?',
                'choices': [
                    {'text': 'onCreate()', 'is_correct': False},
                    {'text': 'onStart()', 'is_correct': True},
                    {'text': 'onResume()', 'is_correct': False},
                    {'text': 'onVisible()', 'is_correct': False}
                ]
            },
            {
                'text': 'Which lifecycle method is called when an activity is no longer visible to the user?',
                'choices': [
                    {'text': 'onStop()', 'is_correct': True},
                    {'text': 'onPause()', 'is_correct': False},
                    {'text': 'onDestroy()', 'is_correct': False},
                    {'text': 'onHide()', 'is_correct': False}
                ]
            },
            {
                'text': 'In which lifecycle method should you save persistent data?',
                'choices': [
                    {'text': 'onPause()', 'is_correct': True},
                    {'text': 'onStop()', 'is_correct': False},
                    {'text': 'onDestroy()', 'is_correct': False},
                    {'text': 'onSaveInstanceState()', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the correct order of activity lifecycle methods during startup?',
                'choices': [
                    {'text': 'onCreate() -> onStart() -> onResume()', 'is_correct': True},
                    {'text': 'onStart() -> onCreate() -> onResume()', 'is_correct': False},
                    {'text': 'onCreate() -> onResume() -> onStart()', 'is_correct': False},
                    {'text': 'onResume() -> onStart() -> onCreate()', 'is_correct': False}
                ]
            },
            {
                'text': 'Which lifecycle method is called when the activity is being recreated after a configuration change?',
                'choices': [
                    {'text': 'onRestart()', 'is_correct': False},
                    {'text': 'onRecreate()', 'is_correct': False},
                    {'text': 'onCreate()', 'is_correct': True},
                    {'text': 'onConfigurationChanged()', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of onSaveInstanceState() method?',
                'choices': [
                    {'text': 'To save persistent data to a database', 'is_correct': False},
                    {'text': 'To save the UI state before the activity is destroyed', 'is_correct': True},
                    {'text': 'To save the activity instance to memory', 'is_correct': False},
                    {'text': 'To save the application state', 'is_correct': False}
                ]
            },
            {
                'text': 'Which lifecycle method is called when the user presses the back button?',
                'choices': [
                    {'text': 'onBackPressed()', 'is_correct': False},
                    {'text': 'onPause() -> onStop() -> onDestroy()', 'is_correct': True},
                    {'text': 'onStop() -> onDestroy()', 'is_correct': False},
                    {'text': 'onDestroy()', 'is_correct': False}
                ]
            },
            {
                'text': 'What happens to an activity when another activity comes into the foreground?',
                'choices': [
                    {'text': 'It is destroyed', 'is_correct': False},
                    {'text': 'It is paused', 'is_correct': True},
                    {'text': 'It continues running in the background', 'is_correct': False},
                    {'text': 'It is stopped and then destroyed', 'is_correct': False}
                ]
            },
            {
                'text': 'Which lifecycle method is called when the activity is being destroyed?',
                'choices': [
                    {'text': 'onFinish()', 'is_correct': False},
                    {'text': 'onStop()', 'is_correct': False},
                    {'text': 'onDestroy()', 'is_correct': True},
                    {'text': 'onEnd()', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of ViewModel in Android?',
                'choices': [
                    {'text': 'To create views programmatically', 'is_correct': False},
                    {'text': 'To store and manage UI-related data in a lifecycle-conscious way', 'is_correct': True},
                    {'text': 'To handle view binding', 'is_correct': False},
                    {'text': 'To create custom views', 'is_correct': False}
                ]
            }
        ]
    },
    {
        'title': 'Android Networking Quiz',
        'lesson_title': 'Android Networking',
        'questions': [
            {
                'text': 'Which permission is required to access the internet in an Android app?',
                'choices': [
                    {'text': 'android.permission.INTERNET', 'is_correct': True},
                    {'text': 'android.permission.ACCESS_NETWORK', 'is_correct': False},
                    {'text': 'android.permission.NETWORK_ACCESS', 'is_correct': False},
                    {'text': 'android.permission.WEB_ACCESS', 'is_correct': False}
                ]
            },
            {
                'text': 'Which library is commonly used for making HTTP requests in Android?',
                'choices': [
                    {'text': 'HttpClient', 'is_correct': False},
                    {'text': 'Retrofit', 'is_correct': True},
                    {'text': 'NetworkManager', 'is_correct': False},
                    {'text': 'WebRequest', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of OkHttp in Android?',
                'choices': [
                    {'text': 'To handle HTTP requests and responses', 'is_correct': True},
                    {'text': 'To manage database connections', 'is_correct': False},
                    {'text': 'To create UI components', 'is_correct': False},
                    {'text': 'To handle user authentication', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is NOT a common format for API responses?',
                'choices': [
                    {'text': 'JSON', 'is_correct': False},
                    {'text': 'XML', 'is_correct': False},
                    {'text': 'HTML', 'is_correct': False},
                    {'text': 'YAML', 'is_correct': True}
                ]
            },
            {
                'text': 'What is the purpose of Gson library in Android?',
                'choices': [
                    {'text': 'To convert Java objects to JSON and vice versa', 'is_correct': True},
                    {'text': 'To make HTTP requests', 'is_correct': False},
                    {'text': 'To handle authentication', 'is_correct': False},
                    {'text': 'To manage network connections', 'is_correct': False}
                ]
            },
            {
                'text': 'Which component is used to check network connectivity in Android?',
                'choices': [
                    {'text': 'NetworkManager', 'is_correct': False},
                    {'text': 'ConnectivityManager', 'is_correct': True},
                    {'text': 'ConnectionChecker', 'is_correct': False},
                    {'text': 'NetworkChecker', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of the Volley library in Android?',
                'choices': [
                    {'text': 'To handle network requests', 'is_correct': True},
                    {'text': 'To manage animations', 'is_correct': False},
                    {'text': 'To handle database operations', 'is_correct': False},
                    {'text': 'To create UI components', 'is_correct': False}
                ]
            },
            {
                'text': 'Which HTTP method is used to retrieve data from a server?',
                'choices': [
                    {'text': 'GET', 'is_correct': True},
                    {'text': 'POST', 'is_correct': False},
                    {'text': 'PUT', 'is_correct': False},
                    {'text': 'DELETE', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of the @GET annotation in Retrofit?',
                'choices': [
                    {'text': 'To specify that the request should use the GET method', 'is_correct': True},
                    {'text': 'To get data from a local database', 'is_correct': False},
                    {'text': 'To get the response as a string', 'is_correct': False},
                    {'text': 'To get the request URL', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is a benefit of using Retrofit over traditional HTTP clients?',
                'choices': [
                    {'text': 'It automatically handles threading', 'is_correct': False},
                    {'text': 'It provides a simple API for making requests', 'is_correct': False},
                    {'text': 'It automatically converts JSON responses to Java objects', 'is_correct': False},
                    {'text': 'All of the above', 'is_correct': True}
                ]
            }
        ]
    },
    {
        'title': 'Android Storage Quiz',
        'lesson_title': 'Android Storage',
        'questions': [
            {
                'text': 'Which of the following is NOT a storage option in Android?',
                'choices': [
                    {'text': 'Shared Preferences', 'is_correct': False},
                    {'text': 'Internal Storage', 'is_correct': False},
                    {'text': 'External Storage', 'is_correct': False},
                    {'text': 'Cloud Storage', 'is_correct': True}
                ]
            },
            {
                'text': 'What is the purpose of SharedPreferences in Android?',
                'choices': [
                    {'text': 'To store key-value pairs of primitive data types', 'is_correct': True},
                    {'text': 'To share data between different apps', 'is_correct': False},
                    {'text': 'To store large amounts of structured data', 'is_correct': False},
                    {'text': 'To store files', 'is_correct': False}
                ]
            },
            {
                'text': 'Which class is used to create and manage SQLite databases in Android?',
                'choices': [
                    {'text': 'SQLiteDatabase', 'is_correct': False},
                    {'text': 'SQLiteOpenHelper', 'is_correct': True},
                    {'text': 'DatabaseHelper', 'is_correct': False},
                    {'text': 'SQLiteManager', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the difference between internal and external storage in Android?',
                'choices': [
                    {'text': 'Internal storage is always available, external storage may not be', 'is_correct': True},
                    {'text': 'Internal storage is slower than external storage', 'is_correct': False},
                    {'text': 'Internal storage is public, external storage is private', 'is_correct': False},
                    {'text': 'There is no difference', 'is_correct': False}
                ]
            },
            {
                'text': 'Which permission is required to write to external storage in Android?',
                'choices': [
                    {'text': 'android.permission.WRITE_EXTERNAL_STORAGE', 'is_correct': True},
                    {'text': 'android.permission.EXTERNAL_STORAGE', 'is_correct': False},
                    {'text': 'android.permission.STORAGE', 'is_correct': False},
                    {'text': 'android.permission.WRITE_STORAGE', 'is_correct': False}
                ]
            },
            {
                'text': 'What is Room in Android?',
                'choices': [
                    {'text': 'A UI component for displaying data', 'is_correct': False},
                    {'text': 'A persistence library that provides an abstraction layer over SQLite', 'is_correct': True},
                    {'text': 'A storage location for temporary files', 'is_correct': False},
                    {'text': 'A library for managing shared preferences', 'is_correct': False}
                ]
            },
            {
                'text': 'Which component is used to define the database schema in Room?',
                'choices': [
                    {'text': 'Entity', 'is_correct': True},
                    {'text': 'Schema', 'is_correct': False},
                    {'text': 'Table', 'is_correct': False},
                    {'text': 'Model', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of ContentProvider in Android?',
                'choices': [
                    {'text': 'To provide content to the user interface', 'is_correct': False},
                    {'text': 'To share data between applications', 'is_correct': True},
                    {'text': 'To store content in a database', 'is_correct': False},
                    {'text': 'To provide content for web views', 'is_correct': False}
                ]
            },
            {
                'text': 'Which method is used to get a reference to the shared preferences in Android?',
                'choices': [
                    {'text': 'getSharedPreferences()', 'is_correct': True},
                    {'text': 'getPreferences()', 'is_correct': False},
                    {'text': 'createSharedPreferences()', 'is_correct': False},
                    {'text': 'openSharedPreferences()', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of the @Dao annotation in Room?',
                'choices': [
                    {'text': 'To mark a class as a Data Access Object', 'is_correct': True},
                    {'text': 'To define a database table', 'is_correct': False},
                    {'text': 'To create a database instance', 'is_correct': False},
                    {'text': 'To define a query', 'is_correct': False}
                ]
            }
        ]
    }
]

# Add quizzes to the course
for index, quiz_data in enumerate(quizzes_data):
    # First, create or get a lesson for this quiz
    lesson_title = quiz_data['lesson_title']
    lesson_slug = slugify(lesson_title)
    
    lesson, created = Lesson.objects.get_or_create(
        course=course,
        slug=lesson_slug,
        defaults={
            'title': lesson_title,
            'content': f"# {lesson_title}\n\nLesson content for {lesson_title}",
            'order': index + 1,
            'is_published': True
        }
    )
    
    if created:
        print(f"Created lesson: {lesson.title}")
    else:
        print(f"Lesson already exists: {lesson.title}")
        lesson.order = index + 1
        lesson.save()
        print(f"Updated order for lesson: {lesson.title} to {index + 1}")
    
    # Now create the quiz associated with this lesson
    quiz, quiz_created = Quiz.objects.get_or_create(
        lesson=lesson,
        defaults={
            'title': quiz_data['title'],
            'description': f"Test your knowledge of {lesson_title}"
        }
    )
    
    if quiz_created:
        print(f"Created quiz: {quiz.title}")
        
        # Add questions to the quiz
        for question_data in quiz_data['questions']:
            question = Question.objects.create(
                quiz=quiz,
                text=question_data['text']
            )
            print(f"Created question: {question.text[:50]}...")
            
            # Add choices to the question
            for choice_data in question_data['choices']:
                choice = Answer.objects.create(
                    question=question,
                    text=choice_data['text'],
                    is_correct=choice_data['is_correct']
                )
                print(f"Created choice: {choice.text[:30]}...")
    else:
        print(f"Quiz already exists: {quiz.title}")

# Create an overview lesson
overview_lesson, created = Lesson.objects.get_or_create(
    course=course,
    slug='android-development-overview',
    defaults={
        'title': 'Android Development with Kotlin Overview',
        'content': f"""# Android Development with Kotlin

This course provides a comprehensive introduction to Android app development using Kotlin. You will learn how to build modern, responsive Android applications using the latest tools and best practices.

## Table of Contents

1. [Kotlin Basics](/learning/lesson/kotlin-basics)
2. [Android UI Components](/learning/lesson/android-ui-components)
3. [Android Lifecycle](/learning/lesson/android-lifecycle)
4. [Android Networking](/learning/lesson/android-networking)
5. [Android Storage](/learning/lesson/android-storage)

## Course Overview

In this course, you will learn:

- Kotlin programming language fundamentals
- Android UI development with modern components
- Activity and Fragment lifecycle management
- Making network requests and handling responses
- Data storage options in Android

Each topic includes detailed explanations, code examples, and interactive quizzes to test your understanding.

## Prerequisites

- Basic programming knowledge
- Understanding of object-oriented programming concepts
- Familiarity with mobile app concepts

## Learning Objectives

By the end of this course, you will be able to:

1. Write Kotlin code for Android applications
2. Create responsive and interactive user interfaces
3. Manage application lifecycle and state
4. Implement network operations and API integration
5. Store and retrieve data using various Android storage options

Let's begin your journey into Android development with Kotlin!
""",
        'order': 0,
        'is_published': True
    }
)

if created:
    print(f"Created overview lesson: {overview_lesson.title}")
else:
    overview_lesson.order = 0
    overview_lesson.save()
    print(f"Updated overview lesson: {overview_lesson.title}")

print("Quizzes have been added to the 'Android Development with Kotlin' course.") 