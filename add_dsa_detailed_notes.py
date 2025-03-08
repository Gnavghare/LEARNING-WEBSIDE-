import os
import django

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from learning_content.models import Course, KeyPoint

# Get the course by ID
course = Course.objects.get(id=12)  # Algorithms and Data Structures course
print(f"Adding detailed notes to key points for course: {course.title}")

# Define detailed notes for each key point
keypoint_details = {
    # Arrays
    1: {
        'example': '''
```python
# Creating an array in Python
arr = [1, 2, 3, 4, 5]

# Accessing elements
first_element = arr[0]  # 1
third_element = arr[2]  # 3

# Modifying elements
arr[1] = 10  # arr becomes [1, 10, 3, 4, 5]

# Adding elements
arr.append(6)  # arr becomes [1, 10, 3, 4, 5, 6]

# Inserting elements at a specific position
arr.insert(2, 20)  # arr becomes [1, 10, 20, 3, 4, 5, 6]

# Removing elements
arr.pop()  # removes and returns the last element, arr becomes [1, 10, 20, 3, 4, 5]
arr.pop(2)  # removes and returns the element at index 2, arr becomes [1, 10, 3, 4, 5]
```
        ''',
        'time_complexity': '''
- Access: O(1)
- Search: O(n) for unsorted arrays, O(log n) for sorted arrays using binary search
- Insertion: O(n) in worst case (when inserting at the beginning)
- Deletion: O(n) in worst case (when deleting from the beginning)
        ''',
        'space_complexity': 'O(n) where n is the number of elements in the array',
        'applications': '''
- Storing and accessing sequential data
- Temporarily storing objects
- Used as buffers for I/O operations
- Lookup tables and inverse lookup tables
- Implementing other data structures like stacks, queues, heaps, hash tables
        ''',
        'book_reference': '''
**Introduction to Algorithms** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (CLRS)
- Chapter 10: Elementary Data Structures
- Pages 232-240

**Data Structures and Algorithms in Python** by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
- Chapter 5: Array-Based Sequences
- Pages 198-242
        '''
    },
    
    # Linked Lists
    2: {
        'example': '''
```python
# Definition for a singly linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Traversing a linked list
current = head
while current:
    print(current.val)
    current = current.next

# Inserting a node at the beginning
new_head = ListNode(0)
new_head.next = head
head = new_head

# Inserting a node in the middle
current = head
while current and current.val != 3:
    current = current.next
if current:
    new_node = ListNode(2.5)
    new_node.next = current.next
    current.next = new_node

# Deleting a node
current = head
while current and current.next and current.next.val != 3:
    current = current.next
if current and current.next:
    current.next = current.next.next
```
        ''',
        'time_complexity': '''
- Access: O(n)
- Search: O(n)
- Insertion: O(1) if inserting at the beginning or end (with tail pointer), O(n) if inserting in the middle
- Deletion: O(1) if deleting from the beginning, O(n) if deleting from the middle or end
        ''',
        'space_complexity': 'O(n) where n is the number of elements in the linked list',
        'applications': '''
- Implementing dynamic memory allocation
- Implementing other data structures like stacks, queues, and hash tables
- Representing sparse matrices
- Performing arithmetic operations on long integers
- Creating adjacency lists for graphs
        ''',
        'book_reference': '''
**Introduction to Algorithms** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (CLRS)
- Chapter 10: Elementary Data Structures
- Pages 236-241

**Algorithms, 4th Edition** by Robert Sedgewick and Kevin Wayne
- Chapter 1.3: Bags, Queues, and Stacks
- Pages 142-151
        '''
    },
    
    # Stacks
    3: {
        'example': '''
```python
# Implementing a stack using a list in Python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Using the stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # 3
print(stack.pop())   # 3
print(stack.pop())   # 2
print(stack.size())  # 1
```
        ''',
        'time_complexity': '''
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)
        ''',
        'space_complexity': 'O(n) where n is the number of elements in the stack',
        'applications': '''
- Function call management (call stack)
- Expression evaluation and syntax parsing
- Backtracking algorithms
- Undo mechanisms in text editors
- Browser history (back button)
- Depth-first search in graphs
- Checking balanced parentheses
        ''',
        'book_reference': '''
**Introduction to Algorithms** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (CLRS)
- Chapter 10: Elementary Data Structures
- Pages 232-236

**Data Structures and Algorithms in Python** by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
- Chapter 6: Stacks, Queues, and Deques
- Pages 243-254
        '''
    },
    
    # Queues
    4: {
        'example': '''
```python
# Implementing a queue using a list in Python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Using the queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.front())    # 1
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
print(queue.size())     # 1
```
        ''',
        'time_complexity': '''
- Enqueue: O(1)
- Dequeue: O(1) for a proper queue implementation (using a linked list or circular array)
- Front: O(1)
- Search: O(n)
        ''',
        'space_complexity': 'O(n) where n is the number of elements in the queue',
        'applications': '''
- CPU scheduling
- Disk scheduling
- Print spooling
- Handling of interrupts in real-time systems
- Breadth-first search in graphs
- Implementing buffers for devices like keyboards
- Task scheduling
        ''',
        'book_reference': '''
**Introduction to Algorithms** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (CLRS)
- Chapter 10: Elementary Data Structures
- Pages 232-236

**Data Structures and Algorithms in Python** by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
- Chapter 6: Stacks, Queues, and Deques
- Pages 243-254
        '''
    },
    
    # Trees
    5: {
        'example': '''
```python
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Creating a binary tree:
#       1
#      / \\
#     2   3
#    / \\
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Inorder traversal (Left, Root, Right)
def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
    return result

# Preorder traversal (Root, Left, Right)
def preorder_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))
    return result

# Postorder traversal (Left, Right, Root)
def postorder_traversal(root):
    result = []
    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.val)
    return result

print(inorder_traversal(root))    # [4, 2, 5, 1, 3]
print(preorder_traversal(root))   # [1, 2, 4, 5, 3]
print(postorder_traversal(root))  # [4, 5, 2, 3, 1]
```
        ''',
        'time_complexity': '''
- Access: O(log n) for balanced trees, O(n) for unbalanced trees
- Search: O(log n) for balanced trees, O(n) for unbalanced trees
- Insertion: O(log n) for balanced trees, O(n) for unbalanced trees
- Deletion: O(log n) for balanced trees, O(n) for unbalanced trees
        ''',
        'space_complexity': 'O(n) where n is the number of nodes in the tree',
        'applications': '''
- Hierarchical data representation (file systems, organization charts)
- Binary Search Trees for efficient searching
- Expression trees for parsing and evaluating expressions
- Huffman coding for data compression
- Priority queues and heaps
- Syntax trees in compilers
- Trie for efficient string operations
        ''',
        'book_reference': '''
**Introduction to Algorithms** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (CLRS)
- Chapter 12: Binary Search Trees
- Pages 286-307
- Chapter 13: Red-Black Trees
- Pages 308-338

**Algorithms, 4th Edition** by Robert Sedgewick and Kevin Wayne
- Chapter 3: Searching
- Pages 396-470
        '''
    },
    
    # Graphs
    6: {
        'example': '''
```python
# Representing a graph using adjacency list
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
    
    # Breadth-First Search
    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        
        while queue:
            current = queue.pop(0)
            print(current, end=" ")
            
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    # Depth-First Search
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start_vertex)
        print(start_vertex, end=" ")
        
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Creating a graph
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

g.print_graph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'D']
# D: ['B', 'C', 'E']
# E: ['D']

print("BFS starting from vertex A:")
g.bfs("A")  # A B C D E

print("\nDFS starting from vertex A:")
g.dfs("A")  # A B D C E
```
        ''',
        'time_complexity': '''
- Adjacency List:
  - Add Vertex: O(1)
  - Add Edge: O(1)
  - Remove Vertex: O(V + E) where V is the number of vertices and E is the number of edges
  - Remove Edge: O(E)
  - BFS/DFS: O(V + E)

- Adjacency Matrix:
  - Add Vertex: O(V²)
  - Add Edge: O(1)
  - Remove Vertex: O(V²)
  - Remove Edge: O(1)
  - BFS/DFS: O(V²)
        ''',
        'space_complexity': '''
- Adjacency List: O(V + E) where V is the number of vertices and E is the number of edges
- Adjacency Matrix: O(V²) where V is the number of vertices
        ''',
        'applications': '''
- Social networks
- Web page ranking
- GPS and mapping
- Network routing
- Airline traffic
- Circuit design
- Scheduling problems
- Recommendation systems
- Shortest path algorithms (Dijkstra's, Bellman-Ford)
- Minimum spanning tree algorithms (Prim's, Kruskal's)
        ''',
        'book_reference': '''
**Introduction to Algorithms** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (CLRS)
- Chapter 22: Elementary Graph Algorithms
- Pages 589-618
- Chapter 23: Minimum Spanning Trees
- Pages 624-642
- Chapter 24: Single-Source Shortest Paths
- Pages 643-683
- Chapter 25: All-Pairs Shortest Paths
- Pages 684-707

**Algorithms, 4th Edition** by Robert Sedgewick and Kevin Wayne
- Chapter 4: Graphs
- Pages 518-642
        '''
    },
    
    # Hash Tables
    7: {
        'example': '''
```python
# Implementing a simple hash table
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_index = self._hash_function(key)
        
        # Check if key already exists
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index][i] = (key, value)
                return
        
        # If key doesn't exist, append it
        self.table[hash_index].append((key, value))
    
    def get(self, key):
        hash_index = self._hash_function(key)
        
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        
        return None
    
    def remove(self, key):
        hash_index = self._hash_function(key)
        
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                del self.table[hash_index][i]
                return
    
    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")

# Using the hash table
ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 7)
ht.insert("orange", 10)
ht.insert("grape", 3)

ht.print_table()
# Output might look like:
# 0: []
# 1: []
# 2: [('banana', 7)]
# 3: []
# 4: [('apple', 5)]
# 5: []
# 6: [('orange', 10)]
# 7: []
# 8: [('grape', 3)]
# 9: []

print(ht.get("apple"))  # 5
print(ht.get("banana"))  # 7

ht.remove("apple")
print(ht.get("apple"))  # None
```
        ''',
        'time_complexity': '''
- Insert: O(1) average case, O(n) worst case
- Search: O(1) average case, O(n) worst case
- Delete: O(1) average case, O(n) worst case
        ''',
        'space_complexity': 'O(n) where n is the number of key-value pairs stored',
        'applications': '''
- Implementing dictionaries and maps
- Database indexing
- Caching
- Symbol tables in compilers
- Unique data identification
- Cryptographic applications
- Implementing sets
- Counting frequencies (e.g., word count)
        ''',
        'book_reference': '''
**Introduction to Algorithms** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (CLRS)
- Chapter 11: Hash Tables
- Pages 253-285

**Algorithms, 4th Edition** by Robert Sedgewick and Kevin Wayne
- Chapter 3.4: Hash Tables
- Pages 458-481
        '''
    }
}

# Update each key point with detailed notes
for keypoint_id, details in keypoint_details.items():
    try:
        keypoint = KeyPoint.objects.get(id=keypoint_id)
        print(f"Updating key point: {keypoint.title}")
        
        if 'example' in details:
            keypoint.example = details['example']
        
        if 'time_complexity' in details:
            keypoint.time_complexity = details['time_complexity']
        
        if 'space_complexity' in details:
            keypoint.space_complexity = details['space_complexity']
        
        if 'applications' in details:
            keypoint.applications = details['applications']
        
        # Add book reference to the description
        if 'book_reference' in details:
            if not keypoint.description.endswith(details['book_reference']):
                keypoint.description += "\n\n## Recommended Reading\n" + details['book_reference']
        
        keypoint.save()
        print(f"Successfully updated key point: {keypoint.title}")
    
    except KeyPoint.DoesNotExist:
        print(f"Key point with ID {keypoint_id} does not exist.")
    except Exception as e:
        print(f"Error updating key point with ID {keypoint_id}: {str(e)}")

print("Detailed notes have been added to key points in the 'Algorithms and Data Structures' course.") 