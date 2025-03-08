from django.core.management.base import BaseCommand
from django.utils import timezone
from learning_content.models import Course, Lesson, Quiz, Question, Choice, KeyPoint

class Command(BaseCommand):
    help = 'Adds detailed content to the Algorithms and Data Structures course'

    def handle(self, *args, **options):
        # Get the course by ID
        course = Course.objects.get(id=12)  # Algorithms and Data Structures course
        self.stdout.write(self.style.SUCCESS(f"Adding content to course: {course.title}"))

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
            # Create or get each key point
            keypoint, created = KeyPoint.objects.get_or_create(
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
            
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created key point: {keypoint.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Key point already exists: {keypoint.title}"))
                
                # Update existing key point with new information
                keypoint.description = keypoint_data['description']
                keypoint.type = keypoint_data['type']
                keypoint.example = keypoint_data['example']
                keypoint.exercise = keypoint_data['exercise']
                keypoint.updated_at = timezone.now()
                keypoint.save()
                self.stdout.write(self.style.SUCCESS(f"Updated key point: {keypoint.title}"))
        
        self.stdout.write(self.style.SUCCESS("Detailed content has been added to the 'Algorithms and Data Structures' course.")) 