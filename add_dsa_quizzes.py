import os
import django

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from django.utils import timezone
from learning_content.models import Course, Lesson, Quiz, Question, Answer, KeyPoint
from django.utils.text import slugify

# Get the course by ID
course = Course.objects.get(id=12)  # Algorithms and Data Structures course
print(f"Adding quizzes to course: {course.title}")

# Get all key points for this course
keypoints = KeyPoint.objects.filter(course=course)
print(f"Found {len(keypoints)} key points for this course")

# Define quizzes for each key point
quizzes_data = [
    {
        'title': 'Arrays Quiz',
        'lesson_title': 'Arrays',
        'questions': [
            {
                'text': 'What is the time complexity of accessing an element in an array by index?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': True},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following operations is costly in an array?',
                'choices': [
                    {'text': 'Accessing an element', 'is_correct': False},
                    {'text': 'Inserting an element at the beginning', 'is_correct': True},
                    {'text': 'Inserting an element at the end', 'is_correct': False},
                    {'text': 'Accessing the first element', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the space complexity of an array with n elements?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is NOT a characteristic of arrays?',
                'choices': [
                    {'text': 'Fixed size', 'is_correct': False},
                    {'text': 'Elements stored in contiguous memory', 'is_correct': False},
                    {'text': 'Dynamic size', 'is_correct': True},
                    {'text': 'Random access', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of searching for an element in an unsorted array?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n log n)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of searching for an element in a sorted array using binary search?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': True},
                    {'text': 'O(n log n)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is true about arrays in most programming languages?',
                'choices': [
                    {'text': 'They can store elements of different data types', 'is_correct': False},
                    {'text': 'They can only store elements of the same data type', 'is_correct': True},
                    {'text': 'They can only store primitive data types', 'is_correct': False},
                    {'text': 'They can only store objects', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of deleting an element from the end of an array?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': True},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of deleting an element from the beginning of an array?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following operations can be performed in O(1) time on an array?',
                'choices': [
                    {'text': 'Inserting an element at a specific index', 'is_correct': False},
                    {'text': 'Deleting an element from a specific index', 'is_correct': False},
                    {'text': 'Accessing an element at a specific index', 'is_correct': True},
                    {'text': 'Finding the minimum element', 'is_correct': False}
                ]
            }
        ]
    },
    {
        'title': 'Linked Lists Quiz',
        'lesson_title': 'Linked Lists',
        'questions': [
            {
                'text': 'What is the time complexity of inserting an element at the beginning of a linked list?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': True},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is true about linked lists?',
                'choices': [
                    {'text': 'They have a fixed size', 'is_correct': False},
                    {'text': 'They allow random access', 'is_correct': False},
                    {'text': 'They are dynamic in size', 'is_correct': True},
                    {'text': 'They are stored in contiguous memory locations', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of accessing the nth element in a singly linked list?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the space complexity of a linked list with n elements?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is NOT a type of linked list?',
                'choices': [
                    {'text': 'Singly linked list', 'is_correct': False},
                    {'text': 'Doubly linked list', 'is_correct': False},
                    {'text': 'Circular linked list', 'is_correct': False},
                    {'text': 'Binary linked list', 'is_correct': True}
                ]
            },
            {
                'text': 'What is the main advantage of a doubly linked list over a singly linked list?',
                'choices': [
                    {'text': 'It uses less memory', 'is_correct': False},
                    {'text': 'It allows traversal in both directions', 'is_correct': True},
                    {'text': 'It has faster insertion at the beginning', 'is_correct': False},
                    {'text': 'It has faster access to elements', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of deleting a node from the end of a singly linked list?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of inserting a node at the end of a singly linked list if we maintain a tail pointer?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': True},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following operations is more efficient in a linked list compared to an array?',
                'choices': [
                    {'text': 'Random access of elements', 'is_correct': False},
                    {'text': 'Insertion at the beginning', 'is_correct': True},
                    {'text': 'Searching for an element', 'is_correct': False},
                    {'text': 'Accessing the last element', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a common application of linked lists?',
                'choices': [
                    {'text': 'Implementing hash tables', 'is_correct': True},
                    {'text': 'Sorting algorithms', 'is_correct': False},
                    {'text': 'Binary search', 'is_correct': False},
                    {'text': 'Matrix operations', 'is_correct': False}
                ]
            }
        ]
    },
    {
        'title': 'Stacks and Queues Quiz',
        'lesson_title': 'Stacks and Queues',
        'questions': [
            {
                'text': 'Which principle does a stack follow?',
                'choices': [
                    {'text': 'FIFO (First In, First Out)', 'is_correct': False},
                    {'text': 'LIFO (Last In, First Out)', 'is_correct': True},
                    {'text': 'LILO (Last In, Last Out)', 'is_correct': False},
                    {'text': 'FILO (First In, Last Out)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which principle does a queue follow?',
                'choices': [
                    {'text': 'FIFO (First In, First Out)', 'is_correct': True},
                    {'text': 'LIFO (Last In, First Out)', 'is_correct': False},
                    {'text': 'LILO (Last In, Last Out)', 'is_correct': False},
                    {'text': 'FILO (First In, Last Out)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of push operation in a stack?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': True},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of enqueue operation in a queue?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': True},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following applications uses a stack?',
                'choices': [
                    {'text': 'Breadth-first search', 'is_correct': False},
                    {'text': 'Function call management', 'is_correct': True},
                    {'text': 'Print queue', 'is_correct': False},
                    {'text': 'CPU scheduling', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following applications uses a queue?',
                'choices': [
                    {'text': 'Depth-first search', 'is_correct': False},
                    {'text': 'Expression evaluation', 'is_correct': False},
                    {'text': 'Breadth-first search', 'is_correct': True},
                    {'text': 'Backtracking', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a priority queue?',
                'choices': [
                    {'text': 'A queue that follows LIFO principle', 'is_correct': False},
                    {'text': 'A queue where elements are dequeued based on their priority', 'is_correct': True},
                    {'text': 'A queue that can only store elements of the same type', 'is_correct': False},
                    {'text': 'A queue with a fixed size', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a circular queue?',
                'choices': [
                    {'text': 'A queue implemented using a circular linked list', 'is_correct': False},
                    {'text': 'A queue where the last element is connected to the first element', 'is_correct': True},
                    {'text': 'A queue that can only store circular references', 'is_correct': False},
                    {'text': 'A queue that can only store a fixed number of elements', 'is_correct': False}
                ]
            },
            {
                'text': 'Which data structure is typically used to implement a stack?',
                'choices': [
                    {'text': 'Array or Linked List', 'is_correct': True},
                    {'text': 'Binary Tree', 'is_correct': False},
                    {'text': 'Hash Table', 'is_correct': False},
                    {'text': 'Graph', 'is_correct': False}
                ]
            },
            {
                'text': 'What happens when you try to pop from an empty stack?',
                'choices': [
                    {'text': 'It returns null', 'is_correct': False},
                    {'text': 'It returns the last popped element', 'is_correct': False},
                    {'text': 'It throws an underflow error', 'is_correct': True},
                    {'text': 'It waits until an element is pushed', 'is_correct': False}
                ]
            }
        ]
    },
    {
        'title': 'Trees and Graphs Quiz',
        'lesson_title': 'Trees and Graphs',
        'questions': [
            {
                'text': 'What is the maximum number of children a binary tree node can have?',
                'choices': [
                    {'text': '1', 'is_correct': False},
                    {'text': '2', 'is_correct': True},
                    {'text': '3', 'is_correct': False},
                    {'text': 'Unlimited', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the height of a complete binary tree with n nodes?',
                'choices': [
                    {'text': 'log(n)', 'is_correct': True},
                    {'text': 'n', 'is_correct': False},
                    {'text': 'n/2', 'is_correct': False},
                    {'text': 'sqrt(n)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which traversal visits the root node first?',
                'choices': [
                    {'text': 'Inorder', 'is_correct': False},
                    {'text': 'Preorder', 'is_correct': True},
                    {'text': 'Postorder', 'is_correct': False},
                    {'text': 'Level order', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a directed graph?',
                'choices': [
                    {'text': 'A graph where edges have weights', 'is_correct': False},
                    {'text': 'A graph where edges have direction', 'is_correct': True},
                    {'text': 'A graph with no cycles', 'is_correct': False},
                    {'text': 'A graph with a fixed number of nodes', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a binary search tree (BST)?',
                'choices': [
                    {'text': 'A tree where each node has exactly two children', 'is_correct': False},
                    {'text': 'A tree where nodes are stored in sorted order', 'is_correct': False},
                    {'text': 'A tree where left child is less than parent and right child is greater', 'is_correct': True},
                    {'text': 'A tree used only for searching operations', 'is_correct': False}
                ]
            },
            {
                'text': 'What algorithm is commonly used to find the shortest path in a weighted graph?',
                'choices': [
                    {'text': 'Depth-first search', 'is_correct': False},
                    {'text': 'Breadth-first search', 'is_correct': False},
                    {'text': "Dijkstra's algorithm", 'is_correct': True},
                    {'text': 'Binary search', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the time complexity of inserting a node in a binary search tree in the worst case?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a minimum spanning tree?',
                'choices': [
                    {'text': 'A tree with the minimum number of nodes', 'is_correct': False},
                    {'text': 'A tree with the minimum height', 'is_correct': False},
                    {'text': 'A subgraph that connects all vertices with minimum total edge weight', 'is_correct': True},
                    {'text': 'A tree with the minimum number of leaves', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is NOT a balanced binary search tree?',
                'choices': [
                    {'text': 'AVL tree', 'is_correct': False},
                    {'text': 'Red-black tree', 'is_correct': False},
                    {'text': 'B-tree', 'is_correct': False},
                    {'text': 'Linked list', 'is_correct': True}
                ]
            },
            {
                'text': 'What is the difference between a tree and a graph?',
                'choices': [
                    {'text': 'Trees can have cycles, graphs cannot', 'is_correct': False},
                    {'text': 'Trees are directed, graphs are undirected', 'is_correct': False},
                    {'text': 'Trees cannot have cycles, graphs can have cycles', 'is_correct': True},
                    {'text': 'Trees have more nodes than graphs', 'is_correct': False}
                ]
            }
        ]
    },
    {
        'title': 'Hash Tables Quiz',
        'lesson_title': 'Hash Tables',
        'questions': [
            {
                'text': 'What is the average time complexity of lookup in a hash table?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': True},
                    {'text': 'O(n)', 'is_correct': False},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'What is a hash collision?',
                'choices': [
                    {'text': 'When two keys have the same hash value', 'is_correct': True},
                    {'text': 'When a hash function returns an error', 'is_correct': False},
                    {'text': 'When a hash table is full', 'is_correct': False},
                    {'text': 'When a key is not found in the hash table', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is NOT a collision resolution technique?',
                'choices': [
                    {'text': 'Separate chaining', 'is_correct': False},
                    {'text': 'Linear probing', 'is_correct': False},
                    {'text': 'Quadratic probing', 'is_correct': False},
                    {'text': 'Binary search', 'is_correct': True}
                ]
            },
            {
                'text': 'What is the load factor of a hash table?',
                'choices': [
                    {'text': 'The ratio of the number of entries to the number of buckets', 'is_correct': True},
                    {'text': 'The maximum number of collisions', 'is_correct': False},
                    {'text': 'The size of the largest bucket', 'is_correct': False},
                    {'text': 'The number of empty buckets', 'is_correct': False}
                ]
            },
            {
                'text': 'What happens when the load factor of a hash table becomes too high?',
                'choices': [
                    {'text': 'The hash table is automatically sorted', 'is_correct': False},
                    {'text': 'Performance degrades due to increased collisions', 'is_correct': True},
                    {'text': 'The hash table rejects new entries', 'is_correct': False},
                    {'text': 'The hash function changes automatically', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is a characteristic of a good hash function?',
                'choices': [
                    {'text': 'It should be slow to compute', 'is_correct': False},
                    {'text': 'It should generate the same hash for different inputs', 'is_correct': False},
                    {'text': 'It should distribute keys uniformly', 'is_correct': True},
                    {'text': 'It should always generate prime numbers', 'is_correct': False}
                ]
            },
            {
                'text': 'What is separate chaining in hash tables?',
                'choices': [
                    {'text': 'Using multiple hash tables', 'is_correct': False},
                    {'text': 'Storing colliding elements in a linked list at each bucket', 'is_correct': True},
                    {'text': 'Using a secondary hash function', 'is_correct': False},
                    {'text': 'Separating keys and values into different tables', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the worst-case time complexity of lookup in a hash table?',
                'choices': [
                    {'text': 'O(1)', 'is_correct': False},
                    {'text': 'O(n)', 'is_correct': True},
                    {'text': 'O(log n)', 'is_correct': False},
                    {'text': 'O(n^2)', 'is_correct': False}
                ]
            },
            {
                'text': 'Which of the following is an application of hash tables?',
                'choices': [
                    {'text': 'Implementing dictionaries', 'is_correct': True},
                    {'text': 'Sorting data', 'is_correct': False},
                    {'text': 'Finding shortest paths in graphs', 'is_correct': False},
                    {'text': 'Balancing binary trees', 'is_correct': False}
                ]
            },
            {
                'text': 'What is rehashing in the context of hash tables?',
                'choices': [
                    {'text': 'Changing the hash function', 'is_correct': False},
                    {'text': 'Recalculating hash values for all keys', 'is_correct': False},
                    {'text': 'Creating a new, larger hash table and transferring all entries', 'is_correct': True},
                    {'text': 'Removing all collisions from the hash table', 'is_correct': False}
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
    
    lesson, lesson_created = Lesson.objects.get_or_create(
        course=course,
        slug=lesson_slug,
        defaults={
            'title': lesson_title,
            'content': f"Lesson content for {lesson_title}",
            'order': index + 1,
            'is_published': True
        }
    )
    
    if lesson_created:
        print(f"Created lesson: {lesson.title}")
    else:
        print(f"Lesson already exists: {lesson.title}")
    
    # Now create the quiz associated with this lesson
    quiz, created = Quiz.objects.get_or_create(
        lesson=lesson,
        defaults={
            'title': quiz_data['title'],
            'description': f"Quiz on {quiz_data['title']}"
        }
    )
    
    if created:
        print(f"Created quiz: {quiz.title}")
    else:
        print(f"Quiz already exists: {quiz.title}")
        
    # Add questions to the quiz
    for question_data in quiz_data['questions']:
        question, q_created = Question.objects.get_or_create(
            quiz=quiz,
            text=question_data['text']
        )
        
        if q_created:
            print(f"Created question: {question.text[:50]}...")
        else:
            print(f"Question already exists: {question.text[:50]}...")
            
        # Add choices to the question
        for choice_data in question_data['choices']:
            choice, c_created = Answer.objects.get_or_create(
                question=question,
                text=choice_data['text'],
                defaults={
                    'is_correct': choice_data['is_correct']
                }
            )
            
            if c_created:
                print(f"Created choice: {choice.text[:30]}...")
            else:
                print(f"Choice already exists: {choice.text[:30]}...")

print("Quizzes have been added to the 'Algorithms and Data Structures' course.") 