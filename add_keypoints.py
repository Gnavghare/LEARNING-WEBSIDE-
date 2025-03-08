from django.utils import timezone
from learning_content.models import Course, KeyPoint

# Get the course by ID
course = Course.objects.get(id=12)  # Algorithms and Data Structures course
print(f"Adding content to course: {course.title}")

# Add detailed key points with descriptions, types, examples, and exercises
keypoints_data = [
    {
        'keypoint': 'Arrays',
        'description': 'Arrays are a collection of items stored at contiguous memory locations. They are used to store multiple items of the same type together. Arrays provide O(1) access time for elements with known indices, but insertion and deletion operations are costly as they require shifting elements. Arrays can be one-dimensional, two-dimensional, or multi-dimensional.',
        'type': 'Data Structure',
        'example': 'int[] arr = {1, 2, 3, 4, 5};\nint value = arr[2]; // Access element at index 2 (value = 3)',
        'exercise': 'Implement a function to reverse an array in-place without using additional memory.',
        'time_complexity': 'Access: O(1), Search: O(n), Insertion: O(n), Deletion: O(n)',
        'space_complexity': 'O(n)',
        'applications': 'Used in implementing matrices, dynamic programming, and as the foundation for other data structures like stacks, queues, and heaps.'
    },
    {
        'keypoint': 'Linked Lists',
        'description': 'A linked list is a linear data structure where each element is a separate object. Each element (node) of a list comprises two items - the data and a reference to the next node. Linked lists can be singly linked (each node points to the next node), doubly linked (each node points to both the next and previous nodes), or circular (the last node points back to the first node).',
        'type': 'Data Structure',
        'example': 'class Node {\n    int data;\n    Node next;\n}\n\nNode head = new Node(1);\nhead.next = new Node(2);\nhead.next.next = new Node(3);',
        'exercise': 'Write a function to detect a cycle in a linked list using Floyd\'s Tortoise and Hare algorithm.',
        'time_complexity': 'Access: O(n), Search: O(n), Insertion: O(1), Deletion: O(1)',
        'space_complexity': 'O(n)',
        'applications': 'Used in implementing stacks, queues, hash tables, and for memory management in operating systems.'
    },
    {
        'keypoint': 'Stacks',
        'description': 'A stack is a linear data structure which follows the Last In First Out (LIFO) principle. The last element added to the stack will be the first one to be removed. Stacks support two main operations: push (add an element to the top) and pop (remove the top element). Stacks can be implemented using arrays or linked lists.',
        'type': 'Data Structure',
        'example': 'Stack<Integer> stack = new Stack<>();\nstack.push(1);\nstack.push(2);\nint top = stack.pop(); // top = 2',
        'exercise': 'Implement a stack using two queues, ensuring that push, pop, top, and empty operations work correctly.',
        'time_complexity': 'Access: O(n), Search: O(n), Insertion (Push): O(1), Deletion (Pop): O(1)',
        'space_complexity': 'O(n)',
        'applications': 'Used in function call management, expression evaluation, backtracking algorithms, and undo mechanisms in applications.'
    },
    {
        'keypoint': 'Queues',
        'description': 'A queue is a linear data structure that follows the First In First Out (FIFO) principle. The first element added to the queue will be the first one to be removed. Queues support two main operations: enqueue (add an element to the rear) and dequeue (remove the front element). Queues can be implemented using arrays or linked lists.',
        'type': 'Data Structure',
        'example': 'Queue<Integer> queue = new LinkedList<>();\nqueue.add(1); // enqueue\nqueue.add(2);\nint front = queue.remove(); // dequeue, front = 1',
        'exercise': 'Implement a queue using two stacks, ensuring that enqueue, dequeue, peek, and empty operations work correctly.',
        'time_complexity': 'Access: O(n), Search: O(n), Insertion (Enqueue): O(1), Deletion (Dequeue): O(1)',
        'space_complexity': 'O(n)',
        'applications': 'Used in CPU scheduling, disk scheduling, handling of interrupts in real-time systems, and breadth-first search algorithm.'
    },
    {
        'keypoint': 'Trees',
        'description': 'A tree is a hierarchical data structure consisting of nodes connected by edges. Each tree has a root node, and every node has zero or more child nodes. Binary trees are a special type where each node has at most two children (left and right). Binary Search Trees (BST) maintain the property that the left subtree of a node contains only nodes with keys less than the node\'s key, and the right subtree contains only nodes with keys greater than the node\'s key.',
        'type': 'Data Structure',
        'example': 'class TreeNode {\n    int value;\n    TreeNode left;\n    TreeNode right;\n}\n\nTreeNode root = new TreeNode(10);\nroot.left = new TreeNode(5);\nroot.right = new TreeNode(15);',
        'exercise': 'Write a function to perform inorder, preorder, and postorder traversals of a binary tree recursively and iteratively.',
        'time_complexity': 'Access: O(log n) average, O(n) worst, Search: O(log n) average, O(n) worst, Insertion: O(log n) average, O(n) worst, Deletion: O(log n) average, O(n) worst',
        'space_complexity': 'O(n)',
        'applications': 'Used in implementing file systems, databases, decision trees in machine learning, and for representing hierarchical data.'
    },
    {
        'keypoint': 'Graphs',
        'description': 'A graph is a non-linear data structure consisting of nodes (vertices) and edges that connect pairs of nodes. Graphs can be directed (edges have direction) or undirected (edges have no direction). They can also be weighted (edges have values) or unweighted. Graphs can be represented using adjacency matrices, adjacency lists, or edge lists.',
        'type': 'Data Structure',
        'example': 'class Graph {\n    Map<Vertex, List<Vertex>> adjList = new HashMap<>();\n}\n\ngraph.adjList.put(A, [B, C]);\ngraph.adjList.put(B, [A, D]);\ngraph.adjList.put(C, [A, D]);',
        'exercise': 'Implement depth-first search (DFS) and breadth-first search (BFS) algorithms for a graph, and use them to find paths between two vertices.',
        'time_complexity': 'Adjacency Matrix: O(V²) space, O(1) edge lookup, O(V) to find all edges of a vertex. Adjacency List: O(V+E) space, O(degree(V)) edge lookup, O(degree(V)) to find all edges of a vertex.',
        'space_complexity': 'O(V + E) for adjacency list, O(V²) for adjacency matrix',
        'applications': 'Used in social networks, web page ranking, shortest path algorithms, network routing, and recommendation systems.'
    },
    {
        'keypoint': 'Hash Tables',
        'description': 'A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. Hash tables provide efficient insertion, deletion, and lookup operations. Collision resolution techniques include chaining (using linked lists) and open addressing (linear probing, quadratic probing, double hashing).',
        'type': 'Data Structure',
        'example': 'HashMap<String, Integer> map = new HashMap<>();\nmap.put("key1", 1);\nmap.put("key2", 2);\nint value = map.get("key1"); // value = 1',
        'exercise': 'Design a hash table with collision handling using chaining. Implement put, get, and remove operations with O(1) average time complexity.',
        'time_complexity': 'Average: O(1) for search, insert, delete. Worst: O(n) if many collisions',
        'space_complexity': 'O(n)',
        'applications': 'Used in implementing databases, caches, symbol tables in compilers, and for fast data retrieval in general.'
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
            'time_complexity': keypoint_data.get('time_complexity', ''),
            'space_complexity': keypoint_data.get('space_complexity', ''),
            'applications': keypoint_data.get('applications', ''),
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        }
    )
    
    if created:
        print(f"Created key point: {keypoint.title}")
    else:
        print(f"Key point already exists: {keypoint.title}")
        
        # Update existing key point with new information
        keypoint.description = keypoint_data['description']
        keypoint.type = keypoint_data['type']
        keypoint.example = keypoint_data['example']
        keypoint.exercise = keypoint_data['exercise']
        keypoint.time_complexity = keypoint_data.get('time_complexity', '')
        keypoint.space_complexity = keypoint_data.get('space_complexity', '')
        keypoint.applications = keypoint_data.get('applications', '')
        keypoint.updated_at = timezone.now()
        keypoint.save()
        print(f"Updated key point: {keypoint.title}")

print("Detailed content has been added to the 'Algorithms and Data Structures' course.") 