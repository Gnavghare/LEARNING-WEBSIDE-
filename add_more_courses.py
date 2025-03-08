import os
import django
import random
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from learning_content.models import Category, Course, Lesson, Quiz, Question, Answer

def add_more_courses():
    # Get existing categories
    categories = Category.objects.all()
    
    # Web Development Courses
    web_dev = Category.objects.get(name='Web Development')
    web_courses = [
        {
            'title': 'HTML & CSS Fundamentals',
            'description': 'Master the building blocks of the web. Learn how to create responsive, beautiful websites using HTML5 and CSS3. This course covers semantic HTML, CSS layouts, flexbox, grid, and responsive design principles.',
            'category': web_dev,
            'level': 'beginner',
            'is_featured': True,
            'is_published': True,
            'lessons': [
                {
                    'title': 'Introduction to HTML',
                    'content': '<p>HTML (HyperText Markup Language) is the standard markup language for creating web pages.</p><h3>In this lesson, you will learn:</h3><ul><li>Basic HTML document structure</li><li>HTML elements and tags</li><li>Semantic HTML5 elements</li><li>Text formatting and links</li></ul>',
                    'order': 1
                },
                {
                    'title': 'CSS Basics',
                    'content': '<p>CSS (Cascading Style Sheets) is used to style and layout web pages.</p><h3>Key concepts covered:</h3><ul><li>CSS syntax and selectors</li><li>Colors, fonts, and text styling</li><li>The CSS box model</li><li>Layouts and positioning</li></ul>',
                    'order': 2
                },
                {
                    'title': 'Responsive Design',
                    'content': '<p>Responsive design ensures your website looks good on all devices.</p><h3>Topics covered:</h3><ul><li>Media queries</li><li>Flexible layouts</li><li>Mobile-first approach</li><li>Testing responsive designs</li></ul>',
                    'order': 3
                }
            ]
        },
        {
            'title': 'JavaScript Essentials',
            'description': 'Learn the core concepts of JavaScript programming. This course covers variables, data types, functions, DOM manipulation, events, and modern ES6+ features to help you build interactive web applications.',
            'category': web_dev,
            'level': 'beginner',
            'is_featured': True,
            'is_published': True,
            'lessons': [
                {
                    'title': 'JavaScript Fundamentals',
                    'content': '<p>JavaScript is the programming language of the web.</p><h3>In this lesson, you will learn:</h3><ul><li>Variables and data types</li><li>Operators and expressions</li><li>Control flow (if statements, loops)</li><li>Functions and scope</li></ul>',
                    'order': 1
                },
                {
                    'title': 'DOM Manipulation',
                    'content': '<p>The Document Object Model (DOM) represents the structure of HTML documents.</p><h3>Topics covered:</h3><ul><li>Selecting DOM elements</li><li>Modifying content and attributes</li><li>Creating and removing elements</li><li>Event handling</li></ul>',
                    'order': 2
                },
                {
                    'title': 'Modern JavaScript (ES6+)',
                    'content': '<p>ES6 and beyond introduced many powerful features to JavaScript.</p><h3>Features covered:</h3><ul><li>Arrow functions</li><li>Template literals</li><li>Destructuring</li><li>Promises and async/await</li><li>Modules</li></ul>',
                    'order': 3
                }
            ]
        }
    ]
    
    # Data Science Courses
    data_science = Category.objects.get(name='Data Science')
    data_courses = [
        {
            'title': 'Python for Data Analysis',
            'description': 'Learn how to use Python for data analysis with pandas, NumPy, and Matplotlib. This course covers data manipulation, cleaning, visualization, and basic statistical analysis techniques.',
            'category': data_science,
            'level': 'beginner',
            'is_featured': True,
            'is_published': True,
            'lessons': [
                {
                    'title': 'Introduction to NumPy',
                    'content': '<p>NumPy is the fundamental package for scientific computing in Python.</p><h3>In this lesson, you will learn:</h3><ul><li>NumPy arrays and operations</li><li>Array indexing and slicing</li><li>Broadcasting</li><li>Mathematical functions</li></ul>',
                    'order': 1
                },
                {
                    'title': 'Data Analysis with Pandas',
                    'content': '<p>Pandas is a powerful data manipulation and analysis library.</p><h3>Topics covered:</h3><ul><li>Series and DataFrames</li><li>Reading and writing data</li><li>Data cleaning and transformation</li><li>Grouping and aggregation</li></ul>',
                    'order': 2
                },
                {
                    'title': 'Data Visualization',
                    'content': '<p>Visualizing data helps to understand patterns and communicate insights.</p><h3>Libraries covered:</h3><ul><li>Matplotlib for basic plotting</li><li>Seaborn for statistical visualizations</li><li>Creating different types of plots</li><li>Customizing visualizations</li></ul>',
                    'order': 3
                }
            ]
        },
        {
            'title': 'Deep Learning Fundamentals',
            'description': 'Explore the foundations of deep learning and neural networks. Learn about different neural network architectures, training techniques, and applications in computer vision and natural language processing.',
            'category': data_science,
            'level': 'advanced',
            'is_featured': False,
            'is_published': True,
            'lessons': [
                {
                    'title': 'Neural Network Basics',
                    'content': '<p>Neural networks are the foundation of deep learning.</p><h3>In this lesson, you will learn:</h3><ul><li>Neurons and activation functions</li><li>Feedforward networks</li><li>Backpropagation</li><li>Gradient descent optimization</li></ul>',
                    'order': 1
                },
                {
                    'title': 'Convolutional Neural Networks',
                    'content': '<p>CNNs are specialized neural networks for processing grid-like data such as images.</p><h3>Topics covered:</h3><ul><li>Convolutional layers</li><li>Pooling operations</li><li>CNN architectures (LeNet, AlexNet, VGG)</li><li>Image classification and object detection</li></ul>',
                    'order': 2
                },
                {
                    'title': 'Recurrent Neural Networks',
                    'content': '<p>RNNs are designed to work with sequential data.</p><h3>Architectures covered:</h3><ul><li>Simple RNNs</li><li>LSTM and GRU cells</li><li>Sequence-to-sequence models</li><li>Applications in NLP and time series</li></ul>',
                    'order': 3
                }
            ]
        }
    ]
    
    # Mobile Development Courses
    mobile_dev = Category.objects.get(name='Mobile Development')
    mobile_courses = [
        {
            'title': 'iOS Development with Swift',
            'description': 'Learn to build native iOS applications using Swift and SwiftUI. This course covers Swift programming fundamentals, iOS app architecture, UI design principles, and working with iOS frameworks.',
            'category': mobile_dev,
            'level': 'intermediate',
            'is_featured': False,
            'is_published': True,
            'lessons': [
                {
                    'title': 'Swift Programming Basics',
                    'content': '<p>Swift is Apple\'s modern programming language for iOS, macOS, watchOS, and tvOS.</p><h3>In this lesson, you will learn:</h3><ul><li>Swift syntax and data types</li><li>Control flow and functions</li><li>Classes, structures, and protocols</li><li>Optionals and error handling</li></ul>',
                    'order': 1
                },
                {
                    'title': 'Introduction to SwiftUI',
                    'content': '<p>SwiftUI is a modern way to declare user interfaces for any Apple platform.</p><h3>Topics covered:</h3><ul><li>Views and modifiers</li><li>Layout and stacks</li><li>State and binding</li><li>Navigation and lists</li></ul>',
                    'order': 2
                },
                {
                    'title': 'Working with iOS Frameworks',
                    'content': '<p>iOS provides many frameworks for common functionality.</p><h3>Frameworks covered:</h3><ul><li>Core Data for persistence</li><li>URLSession for networking</li><li>Core Location for location services</li><li>Notifications and background tasks</li></ul>',
                    'order': 3
                }
            ]
        },
        {
            'title': 'Android Development with Kotlin',
            'description': 'Master Android app development using Kotlin and Jetpack Compose. This course covers Kotlin programming, Android architecture components, UI design with Compose, and integrating with Android services.',
            'category': mobile_dev,
            'level': 'intermediate',
            'is_featured': True,
            'is_published': True,
            'lessons': [
                {
                    'title': 'Kotlin for Android',
                    'content': '<p>Kotlin is a modern programming language officially supported for Android development.</p><h3>In this lesson, you will learn:</h3><ul><li>Kotlin syntax and features</li><li>Null safety and extensions</li><li>Coroutines for asynchronous programming</li><li>Collections and functional programming</li></ul>',
                    'order': 1
                },
                {
                    'title': 'Jetpack Compose Basics',
                    'content': '<p>Jetpack Compose is Android\'s modern toolkit for building native UI.</p><h3>Topics covered:</h3><ul><li>Composable functions</li><li>Layout and state management</li><li>Theming and styling</li><li>Animations and transitions</li></ul>',
                    'order': 2
                },
                {
                    'title': 'Android Architecture Components',
                    'content': '<p>Architecture components help you build robust, testable, and maintainable apps.</p><h3>Components covered:</h3><ul><li>ViewModel and LiveData</li><li>Room for database operations</li><li>Navigation component</li><li>WorkManager for background tasks</li></ul>',
                    'order': 3
                }
            ]
        }
    ]
    
    # Programming Courses
    programming = Category.objects.get(name='Programming')
    programming_courses = [
        {
            'title': 'Algorithms and Data Structures',
            'description': 'Master essential algorithms and data structures used in software development. This course covers arrays, linked lists, trees, graphs, sorting, searching, and algorithm analysis techniques.',
            'category': programming,
            'level': 'intermediate',
            'is_featured': False,
            'is_published': True,
            'lessons': [
                {
                    'title': 'Basic Data Structures',
                    'content': '<p>Data structures are ways to organize and store data efficiently.</p><h3>In this lesson, you will learn:</h3><ul><li>Arrays and linked lists</li><li>Stacks and queues</li><li>Hash tables</li><li>Time and space complexity analysis</li></ul>',
                    'order': 1
                },
                {
                    'title': 'Trees and Graphs',
                    'content': '<p>Trees and graphs are non-linear data structures with many applications.</p><h3>Topics covered:</h3><ul><li>Binary trees and binary search trees</li><li>Tree traversal algorithms</li><li>Graph representations</li><li>Graph traversal (BFS, DFS)</li></ul>',
                    'order': 2
                },
                {
                    'title': 'Sorting and Searching',
                    'content': '<p>Sorting and searching are fundamental operations in computer science.</p><h3>Algorithms covered:</h3><ul><li>Bubble, insertion, and selection sort</li><li>Merge sort and quicksort</li><li>Linear and binary search</li><li>Algorithm optimization techniques</li></ul>',
                    'order': 3
                }
            ]
        }
    ]
    
    # Combine all courses
    all_new_courses = web_courses + data_courses + mobile_courses + programming_courses
    
    # Add courses and lessons
    for course_data in all_new_courses:
        lessons_data = course_data.pop('lessons')
        
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
        
        if created:
            print(f"Course created: {course.title}")
            
            # Add lessons
            for lesson_data in lessons_data:
                lesson, lesson_created = Lesson.objects.get_or_create(
                    title=lesson_data['title'],
                    course=course,
                    defaults={
                        'slug': slugify(lesson_data['title']),
                        'content': lesson_data['content'],
                        'order': lesson_data['order'],
                        'is_published': True
                    }
                )
                
                if lesson_created:
                    print(f"  Lesson created: {lesson.title}")
                    
                    # Add a quiz for the first lesson of each course
                    if lesson_data['order'] == 1:
                        quiz, quiz_created = Quiz.objects.get_or_create(
                            lesson=lesson,
                            defaults={
                                'title': f"{lesson.title} Quiz",
                                'description': f"Test your knowledge of {lesson.title}."
                            }
                        )
                        
                        if quiz_created:
                            print(f"    Quiz created: {quiz.title}")
                            
                            # Generate 3 questions for each quiz
                            for i in range(3):
                                question, q_created = Question.objects.get_or_create(
                                    text=f"Sample question {i+1} for {lesson.title}",
                                    quiz=quiz
                                )
                                
                                if q_created:
                                    # Create 4 answers for each question (1 correct, 3 incorrect)
                                    Answer.objects.create(
                                        text=f"Correct answer for question {i+1}",
                                        question=question,
                                        is_correct=True
                                    )
                                    
                                    for j in range(3):
                                        Answer.objects.create(
                                            text=f"Incorrect answer {j+1} for question {i+1}",
                                            question=question,
                                            is_correct=False
                                        )
                                    
                                    print(f"      Question created with 4 answers")
        else:
            print(f"Course already exists: {course.title}")

if __name__ == '__main__':
    add_more_courses()
    print("Additional courses have been added successfully!") 