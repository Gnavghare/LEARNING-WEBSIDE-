import os
import django
from django.utils import timezone
from learning_content.models import Course, Lesson, Quiz, Question, Choice, KeyPoint

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

# Function to add lessons, notes, and quizzes

def add_algo_ds_content():
    # Get the course by ID
    course = Course.objects.get(id=12)  # Algorithms and Data Structures course
    print(f"Adding content to course: {course.title}")

    # Add lessons with detailed information and notes
    lessons_data = [
        {
            'title': 'Basic Data Structures',
            'content': 'Detailed content about basic data structures... <img src="/static/images/basic_data_structures.png" alt="Basic Data Structures">',
            'notes': 'Notes on basic data structures...'
        },
        {
            'title': 'Trees and Graphs',
            'content': 'Detailed content about trees and graphs... <img src="/static/images/trees_and_graphs.png" alt="Trees and Graphs">',
            'notes': 'Notes on trees and graphs...'
        },
        {
            'title': 'Sorting and Searching',
            'content': 'Detailed content about sorting and searching... <img src="/static/images/sorting_and_searching.png" alt="Sorting and Searching">',
            'notes': 'Notes on sorting and searching...'
        }
    ]

    for lesson_data in lessons_data:
        lesson, created = Lesson.objects.get_or_create(
            course=course,
            title=lesson_data['title'],
            defaults={
                'content': lesson_data['content'],
                'notes': lesson_data['notes'],
                'created_at': timezone.now(),
                'updated_at': timezone.now()
            }
        )

    # Add quizzes with 10 MCQs each
    for i in range(5):
        quiz = Quiz.objects.create(
            course=course,
            title=f'Quiz {i + 1}',
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

        for j in range(10):
            question = Question.objects.create(
                quiz=quiz,
                text=f'Question {j + 1} for Quiz {i + 1}',
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

            # Add choices for each question
            for k in range(4):
                Choice.objects.create(
                    question=question,
                    text=f'Choice {k + 1} for Question {j + 1}',
                    is_correct=(k == 0),  # Mark the first choice as correct
                    created_at=timezone.now(),
                    updated_at=timezone.now()
                )

    # Add detailed key points with descriptions, types, examples, and exercises
    keypoints_data = [
        {
            'keypoint': 'Arrays',
            'description': 'Arrays are a collection of items stored at contiguous memory locations. They are used to store multiple items of the same type together.',
            'type': 'Data Structure',
            'example': 'int[] arr = {1, 2, 3, 4, 5};',
            'exercise': 'Implement a function to reverse an array.'
        },
        {
            'keypoint': 'Linked Lists',
            'description': 'A linked list is a linear data structure where each element is a separate object. Each element (node) of a list is comprising of two items - the data and a reference to the next node.',
            'type': 'Data Structure',
            'example': 'Node -> Node -> Node',
            'exercise': 'Write a function to detect a cycle in a linked list.'
        },
        {
            'keypoint': 'Stacks',
            'description': 'A stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO (Last In First Out) or FILO (First In Last Out).',
            'type': 'Data Structure',
            'example': 'push(1), push(2), pop() -> 2',
            'exercise': 'Implement a stack using two queues.'
        },
        {
            'keypoint': 'Queues',
            'description': 'A queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO).',
            'type': 'Data Structure',
            'example': 'enqueue(1), enqueue(2), dequeue() -> 1',
            'exercise': 'Implement a queue using two stacks.'
        },
        {
            'keypoint': 'Trees',
            'description': 'A tree is a hierarchical data structure defined as a collection of nodes. Nodes represent value and nodes are connected by edges.',
            'type': 'Data Structure',
            'example': 'Binary Tree: Node(1) -> Node(2), Node(3)',
            'exercise': 'Write a function to perform inorder traversal of a binary tree.'
        },
        {
            'keypoint': 'Graphs',
            'description': 'A graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph.',
            'type': 'Data Structure',
            'example': 'Graph: A -- B, A -- C',
            'exercise': 'Implement depth-first search (DFS) for a graph.'
        },
        {
            'keypoint': 'Hash Tables',
            'description': 'A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values.',
            'type': 'Data Structure',
            'example': '{"key1": "value1", "key2": "value2"}',
            'exercise': 'Design a hash table with collision handling using chaining.'
        }
    ]

    for keypoint_data in keypoints_data:
        # Assuming a KeyPoint model exists
        KeyPoint.objects.get_or_create(
            course=course,
            title=keypoint_data['keypoint'],
            defaults={
                'description': keypoint_data['description'],
                'type': keypoint_data['type'],
                'example': keypoint_data['example'],
                'exercise': keypoint_data['exercise'],
                'created_at': timezone.now(),
                'updated_at': timezone.now()
            }
        )

if __name__ == '__main__':
    add_algo_ds_content()
    print("Lessons, notes, and quizzes have been added to the 'Algorithms and Data Structures' course.") 