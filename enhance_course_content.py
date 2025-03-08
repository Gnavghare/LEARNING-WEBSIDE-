import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from learning_content.models import Course, Lesson

def enhance_course_content():
    # Enhanced content for Python for Beginners
    python_course = Course.objects.get(title='Python for Beginners')
    python_course.description = """
    <p>Master the fundamentals of Python programming in this comprehensive beginner's course. Python is one of the most popular and versatile programming languages in the world, used for web development, data analysis, artificial intelligence, scientific computing, and more.</p>
    
    <p>This course is designed for absolute beginners with no prior programming experience. You'll start with the basics and gradually build your skills through hands-on exercises and projects. By the end of this course, you'll have a solid foundation in Python programming and be ready to tackle more advanced topics.</p>
    
    <h3>What You'll Learn:</h3>
    <ul>
        <li>Python syntax and basic programming concepts</li>
        <li>Variables, data types, and operators</li>
        <li>Control structures (if statements, loops)</li>
        <li>Functions and modules</li>
        <li>Working with lists, tuples, and dictionaries</li>
        <li>File handling and exception handling</li>
        <li>Object-oriented programming basics</li>
    </ul>
    
    <h3>Recommended Books:</h3>
    <ul>
        <li><strong>Python Crash Course</strong> by Eric Matthes</li>
        <li><strong>Automate the Boring Stuff with Python</strong> by Al Sweigart</li>
        <li><strong>Learning Python</strong> by Mark Lutz</li>
    </ul>
    
    <h3>Prerequisites:</h3>
    <p>No prior programming experience required. Just bring your curiosity and willingness to learn!</p>
    """
    python_course.save()
    print(f"Enhanced description for: {python_course.title}")
    
    # Update Python course lessons
    intro_lesson = Lesson.objects.get(title='Introduction to Python', course=python_course)
    intro_lesson.content = """
    <h2>Introduction to Python</h2>
    
    <p>Python is a high-level, interpreted programming language known for its readability and simplicity. Created by Guido van Rossum and first released in 1991, Python has become one of the most popular programming languages in the world.</p>
    
    <h3>Why Learn Python?</h3>
    <ul>
        <li><strong>Easy to learn and use:</strong> Python's syntax is clear and intuitive, making it an excellent first language for beginners.</li>
        <li><strong>Versatile:</strong> Python is used in web development, data science, artificial intelligence, scientific computing, automation, and more.</li>
        <li><strong>Large community and extensive libraries:</strong> Python has a vast ecosystem of libraries and frameworks that extend its capabilities.</li>
        <li><strong>High demand in the job market:</strong> Python skills are highly sought after by employers across various industries.</li>
    </ul>
    
    <h3>Python's Philosophy</h3>
    <p>Python's design philosophy emphasizes code readability and simplicity. The Zen of Python, a collection of 19 guiding principles for writing computer programs in Python, includes aphorisms such as:</p>
    
    <blockquote>
        <p>Beautiful is better than ugly.<br>
        Explicit is better than implicit.<br>
        Simple is better than complex.<br>
        Complex is better than complicated.<br>
        Readability counts.</p>
    </blockquote>
    
    <h3>Getting Started with Python</h3>
    <p>To start programming in Python, you need to:</p>
    <ol>
        <li>Install Python on your computer (from <a href="https://www.python.org/downloads/" target="_blank">python.org</a>)</li>
        <li>Choose a code editor or IDE (Integrated Development Environment)</li>
        <li>Write your first Python program</li>
    </ol>
    
    <h3>Your First Python Program</h3>
    <p>The traditional first program in any programming language is "Hello, World!" In Python, it's as simple as:</p>
    
    <pre><code>print("Hello, World!")</code></pre>
    
    <p>This single line of code tells Python to display the text "Hello, World!" on the screen.</p>
    
    <h3>Python Versions</h3>
    <p>There are two major versions of Python in use today:</p>
    <ul>
        <li><strong>Python 2:</strong> Legacy version, officially discontinued as of January 1, 2020.</li>
        <li><strong>Python 3:</strong> Current version with ongoing development and improvements.</li>
    </ul>
    <p>This course uses Python 3, as it's the present and future of the language.</p>
    
    <h3>Key Resources for This Lesson</h3>
    <ul>
        <li><a href="https://docs.python.org/3/" target="_blank">Official Python Documentation</a></li>
        <li><a href="https://www.python.org/dev/peps/pep-0020/" target="_blank">PEP 20 - The Zen of Python</a></li>
    </ul>
    """
    intro_lesson.save()
    print(f"Enhanced content for lesson: {intro_lesson.title}")
    
    # Enhanced content for JavaScript Essentials
    js_course = Course.objects.get(title='JavaScript Essentials')
    js_course.description = """
    <p>Dive into the world of JavaScript, the programming language that powers the interactive web. This essential course will take you from JavaScript fundamentals to building dynamic web applications.</p>
    
    <p>JavaScript is the language of the web browser, but it has grown far beyond that. Today, JavaScript runs on servers, mobile devices, desktop applications, and even IoT devices. Understanding JavaScript is crucial for any web developer and opens doors to numerous career opportunities.</p>
    
    <h3>What You'll Learn:</h3>
    <ul>
        <li>JavaScript syntax and core concepts</li>
        <li>DOM manipulation and event handling</li>
        <li>Asynchronous JavaScript (Promises, async/await)</li>
        <li>Working with APIs and fetching data</li>
        <li>Modern ES6+ features</li>
        <li>Error handling and debugging</li>
        <li>Introduction to popular JavaScript frameworks</li>
    </ul>
    
    <h3>Recommended Books:</h3>
    <ul>
        <li><strong>Eloquent JavaScript</strong> by Marijn Haverbeke</li>
        <li><strong>JavaScript: The Good Parts</strong> by Douglas Crockford</li>
        <li><strong>You Don't Know JS</strong> series by Kyle Simpson</li>
    </ul>
    
    <h3>Prerequisites:</h3>
    <p>Basic understanding of HTML and CSS is recommended but not required. This course is designed for beginners with little to no programming experience.</p>
    """
    js_course.save()
    print(f"Enhanced description for: {js_course.title}")
    
    # Enhanced content for Deep Learning Fundamentals
    dl_course = Course.objects.get(title='Deep Learning Fundamentals')
    dl_course.description = """
    <p>Explore the fascinating world of deep learning, the cutting-edge technology behind modern artificial intelligence systems. This comprehensive course covers the theoretical foundations and practical applications of neural networks and deep learning algorithms.</p>
    
    <p>Deep learning has revolutionized fields such as computer vision, natural language processing, speech recognition, and game playing. Companies like Google, Facebook, Amazon, and Tesla rely heavily on deep learning for their products and services. By mastering deep learning, you'll be at the forefront of this technological revolution.</p>
    
    <h3>What You'll Learn:</h3>
    <ul>
        <li>Neural network architecture and training</li>
        <li>Backpropagation and optimization algorithms</li>
        <li>Convolutional Neural Networks (CNNs) for image processing</li>
        <li>Recurrent Neural Networks (RNNs) for sequence data</li>
        <li>Generative models and GANs</li>
        <li>Transfer learning and fine-tuning</li>
        <li>Implementing deep learning models with PyTorch and TensorFlow</li>
    </ul>
    
    <h3>Recommended Books:</h3>
    <ul>
        <li><strong>Deep Learning</strong> by Ian Goodfellow, Yoshua Bengio, and Aaron Courville</li>
        <li><strong>Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow</strong> by Aurélien Géron</li>
        <li><strong>Deep Learning with Python</strong> by François Chollet</li>
    </ul>
    
    <h3>Prerequisites:</h3>
    <p>Basic understanding of Python programming, linear algebra, and calculus is recommended. Familiarity with machine learning concepts is helpful but not required.</p>
    
    <h3>Industry Applications:</h3>
    <ul>
        <li><strong>Healthcare:</strong> Medical image analysis, drug discovery, patient diagnosis</li>
        <li><strong>Finance:</strong> Fraud detection, algorithmic trading, risk assessment</li>
        <li><strong>Automotive:</strong> Self-driving cars, predictive maintenance</li>
        <li><strong>Entertainment:</strong> Recommendation systems, content generation</li>
        <li><strong>Retail:</strong> Customer behavior analysis, inventory management</li>
    </ul>
    """
    dl_course.save()
    print(f"Enhanced description for: {dl_course.title}")
    
    # Update Deep Learning course lessons
    nn_lesson = Lesson.objects.get(title='Neural Network Basics', course=dl_course)
    nn_lesson.content = """
    <h2>Neural Network Basics</h2>
    
    <p>Neural networks are the foundation of deep learning, inspired by the structure and function of the human brain. In this lesson, we'll explore the fundamental concepts of neural networks, their components, and how they learn from data.</p>
    
    <h3>What is a Neural Network?</h3>
    <p>A neural network is a computational model composed of interconnected nodes (neurons) organized in layers. These networks can learn complex patterns from data through a process of adjusting the connections (weights) between neurons.</p>
    
    <h3>Components of a Neural Network</h3>
    <ul>
        <li><strong>Neurons:</strong> The basic computational units that receive inputs, apply an activation function, and produce an output.</li>
        <li><strong>Weights:</strong> Parameters that determine the strength of connections between neurons.</li>
        <li><strong>Biases:</strong> Additional parameters that allow the network to represent more complex functions.</li>
        <li><strong>Activation Functions:</strong> Non-linear functions that introduce complexity into the network, enabling it to learn complex patterns.</li>
        <li><strong>Layers:</strong> Groups of neurons organized in a hierarchical structure.</li>
    </ul>
    
    <h3>Types of Layers</h3>
    <ul>
        <li><strong>Input Layer:</strong> Receives the raw data and passes it to the next layer.</li>
        <li><strong>Hidden Layers:</strong> Intermediate layers between input and output that perform most of the computation.</li>
        <li><strong>Output Layer:</strong> Produces the final prediction or classification.</li>
    </ul>
    
    <h3>Common Activation Functions</h3>
    <ul>
        <li><strong>Sigmoid:</strong> Maps values to the range [0, 1], useful for binary classification.</li>
        <li><strong>Tanh:</strong> Maps values to the range [-1, 1], often used in hidden layers.</li>
        <li><strong>ReLU (Rectified Linear Unit):</strong> Returns max(0, x), the most commonly used activation function in modern networks.</li>
        <li><strong>Softmax:</strong> Converts a vector of values to a probability distribution, often used in the output layer for multi-class classification.</li>
    </ul>
    
    <h3>The Feedforward Process</h3>
    <p>The feedforward process is how a neural network makes predictions:</p>
    <ol>
        <li>Input data is fed into the input layer.</li>
        <li>Each neuron computes a weighted sum of its inputs plus a bias.</li>
        <li>The result is passed through an activation function.</li>
        <li>The output becomes the input for the next layer.</li>
        <li>This process continues until the output layer produces the final result.</li>
    </ol>
    
    <h3>Training Neural Networks: Backpropagation</h3>
    <p>Backpropagation is the primary algorithm used to train neural networks:</p>
    <ol>
        <li>Forward pass: Compute the network's prediction.</li>
        <li>Compute the error (difference between prediction and actual target).</li>
        <li>Backward pass: Propagate the error backward through the network.</li>
        <li>Update weights and biases using gradient descent to minimize the error.</li>
        <li>Repeat for many iterations until the network converges.</li>
    </ol>
    
    <h3>Gradient Descent Optimization</h3>
    <p>Gradient descent is an optimization algorithm used to minimize the error (loss) function:</p>
    <ul>
        <li><strong>Batch Gradient Descent:</strong> Updates weights using the entire dataset.</li>
        <li><strong>Stochastic Gradient Descent (SGD):</strong> Updates weights using a single sample at a time.</li>
        <li><strong>Mini-batch Gradient Descent:</strong> Updates weights using a small batch of samples, combining the advantages of both approaches.</li>
    </ul>
    
    <h3>Advanced Optimizers</h3>
    <ul>
        <li><strong>Adam:</strong> Adaptive Moment Estimation, combines the advantages of AdaGrad and RMSProp.</li>
        <li><strong>RMSProp:</strong> Adapts learning rates based on the average of recent gradients.</li>
        <li><strong>Adagrad:</strong> Adapts learning rates based on the history of gradients.</li>
    </ul>
    
    <h3>Challenges in Training Neural Networks</h3>
    <ul>
        <li><strong>Vanishing/Exploding Gradients:</strong> Gradients becoming too small or too large during backpropagation.</li>
        <li><strong>Overfitting:</strong> The network memorizes the training data but fails to generalize to new data.</li>
        <li><strong>Underfitting:</strong> The network is too simple to capture the underlying patterns in the data.</li>
    </ul>
    
    <h3>Regularization Techniques</h3>
    <ul>
        <li><strong>Dropout:</strong> Randomly deactivates neurons during training to prevent co-adaptation.</li>
        <li><strong>L1/L2 Regularization:</strong> Adds a penalty term to the loss function to discourage large weights.</li>
        <li><strong>Batch Normalization:</strong> Normalizes the inputs of each layer to stabilize and accelerate training.</li>
    </ul>
    
    <h3>Key Resources for This Lesson</h3>
    <ul>
        <li><a href="http://neuralnetworksanddeeplearning.com/" target="_blank">Neural Networks and Deep Learning</a> by Michael Nielsen</li>
        <li><a href="https://playground.tensorflow.org/" target="_blank">TensorFlow Playground</a> - Interactive visualization of neural networks</li>
    </ul>
    """
    nn_lesson.save()
    print(f"Enhanced content for lesson: {nn_lesson.title}")
    
    # Enhanced content for HTML & CSS Fundamentals
    html_course = Course.objects.get(title='HTML & CSS Fundamentals')
    html_course.description = """
    <p>Master the building blocks of the web with this comprehensive HTML and CSS course. Learn how to create responsive, beautiful websites from scratch using modern web development techniques.</p>
    
    <p>HTML (HyperText Markup Language) and CSS (Cascading Style Sheets) are the foundation of every website. HTML provides the structure and content, while CSS controls the presentation and layout. Together, they form the cornerstone of web development skills.</p>
    
    <h3>What You'll Learn:</h3>
    <ul>
        <li>HTML5 semantic elements and document structure</li>
        <li>CSS selectors, properties, and values</li>
        <li>Box model, layout techniques, and positioning</li>
        <li>Flexbox and CSS Grid for modern layouts</li>
        <li>Responsive design and media queries</li>
        <li>CSS animations and transitions</li>
        <li>Web accessibility principles</li>
        <li>Best practices for clean, maintainable code</li>
    </ul>
    
    <h3>Recommended Books:</h3>
    <ul>
        <li><strong>HTML and CSS: Design and Build Websites</strong> by Jon Duckett</li>
        <li><strong>CSS Secrets</strong> by Lea Verou</li>
        <li><strong>Responsive Web Design</strong> by Ethan Marcotte</li>
    </ul>
    
    <h3>Prerequisites:</h3>
    <p>No prior experience required. This course is designed for complete beginners.</p>
    
    <h3>Projects You'll Build:</h3>
    <ul>
        <li>Personal portfolio website</li>
        <li>Responsive landing page</li>
        <li>Interactive product showcase</li>
        <li>Multi-page business website</li>
    </ul>
    
    <h3>Industry Tools You'll Learn:</h3>
    <ul>
        <li>Visual Studio Code</li>
        <li>Chrome DevTools</li>
        <li>GitHub for version control</li>
        <li>Figma for design implementation</li>
    </ul>
    """
    html_course.save()
    print(f"Enhanced description for: {html_course.title}")
    
    # Enhanced content for Android Development with Kotlin
    android_course = Course.objects.get(title='Android Development with Kotlin')
    android_course.description = """
    <p>Master Android app development using Kotlin, the modern, concise programming language officially supported by Google for Android development. This comprehensive course will take you from the basics of Kotlin to building sophisticated Android applications using Jetpack Compose and modern architecture patterns.</p>
    
    <p>Android powers billions of devices worldwide, from smartphones and tablets to wearables and TVs. By learning Android development with Kotlin, you'll be equipped to create apps that can reach a global audience and make an impact in the mobile ecosystem.</p>
    
    <h3>What You'll Learn:</h3>
    <ul>
        <li>Kotlin programming fundamentals and advanced features</li>
        <li>Android app architecture and lifecycle</li>
        <li>UI development with Jetpack Compose</li>
        <li>Navigation and app structure</li>
        <li>Data persistence with Room database</li>
        <li>Networking and API integration</li>
        <li>Background processing and coroutines</li>
        <li>Testing and debugging Android applications</li>
        <li>Publishing apps to the Google Play Store</li>
    </ul>
    
    <h3>Recommended Books:</h3>
    <ul>
        <li><strong>Kotlin in Action</strong> by Dmitry Jemerov and Svetlana Isakova</li>
        <li><strong>Android Programming: The Big Nerd Ranch Guide</strong> by Bill Phillips, Chris Stewart, and Kristin Marsicano</li>
        <li><strong>Jetpack Compose by Tutorials</strong> by the raywenderlich.com Team</li>
    </ul>
    
    <h3>Prerequisites:</h3>
    <p>Basic programming knowledge is helpful but not required. The course starts with Kotlin fundamentals before moving to Android-specific topics.</p>
    
    <h3>Projects You'll Build:</h3>
    <ul>
        <li>Task management app with local data storage</li>
        <li>Weather app integrating with REST APIs</li>
        <li>Social media client with authentication</li>
        <li>E-commerce app with payment integration</li>
    </ul>
    
    <h3>Industry Tools You'll Learn:</h3>
    <ul>
        <li>Android Studio</li>
        <li>Gradle build system</li>
        <li>Git for version control</li>
        <li>Firebase for backend services</li>
        <li>Google Play Console</li>
    </ul>
    
    <h3>Career Opportunities:</h3>
    <p>Android developers are in high demand across various industries. After completing this course, you'll be prepared for roles such as:</p>
    <ul>
        <li>Android Developer</li>
        <li>Mobile Application Developer</li>
        <li>Kotlin Developer</li>
        <li>Mobile Software Engineer</li>
        <li>Freelance App Developer</li>
    </ul>
    """
    android_course.save()
    print(f"Enhanced description for: {android_course.title}")
    
    # Update Android Development course lessons
    kotlin_lesson = Lesson.objects.get(title='Kotlin for Android', course=android_course)
    kotlin_lesson.content = """
    <h2>Kotlin for Android Development</h2>
    
    <p>Kotlin has become the preferred language for Android development, officially supported by Google since 2017. In this lesson, we'll explore Kotlin's features and syntax, with a focus on how they benefit Android development.</p>
    
    <h3>Introduction to Kotlin</h3>
    <p>Kotlin is a modern, statically-typed programming language that runs on the Java Virtual Machine (JVM). Developed by JetBrains, Kotlin addresses many of the pain points of Java while maintaining full interoperability with Java code.</p>
    
    <h3>Key Features of Kotlin</h3>
    <ul>
        <li><strong>Conciseness:</strong> Kotlin reduces boilerplate code, making your codebase more maintainable.</li>
        <li><strong>Null Safety:</strong> The type system distinguishes between nullable and non-nullable references, helping prevent null pointer exceptions.</li>
        <li><strong>Interoperability:</strong> Kotlin works seamlessly with Java, allowing you to leverage existing Java libraries and gradually migrate code.</li>
        <li><strong>Functional Programming:</strong> Kotlin supports functional programming concepts like higher-order functions, lambdas, and immutability.</li>
        <li><strong>Extension Functions:</strong> Add new functionality to existing classes without inheritance.</li>
        <li><strong>Coroutines:</strong> Simplified asynchronous programming with lightweight, composable operations.</li>
    </ul>
    
    <h3>Kotlin Syntax Basics</h3>
    
    <h4>Variables and Types</h4>
    <pre><code>// Variable declaration
val name: String = "John" // Immutable (cannot be reassigned)
var age: Int = 25 // Mutable (can be reassigned)

// Type inference
val message = "Hello" // Type is inferred as String
var count = 10 // Type is inferred as Int

// Nullable types
val nullableString: String? = null // Can hold null
val nonNullString: String = "Not null" // Cannot be null</code></pre>
    
    <h4>Functions</h4>
    <pre><code>// Function declaration
fun greet(name: String): String {
    return "Hello, $name!"
}

// Single-expression function
fun add(a: Int, b: Int) = a + b

// Default parameters
fun greetWithDefault(name: String = "Guest") = "Hello, $name!"

// Named arguments
greetWithDefault(name = "Alice")</code></pre>
    
    <h4>Control Flow</h4>
    <pre><code>// If expression
val max = if (a > b) a else b

// When expression (similar to switch)
when (x) {
    1 -> print("x is 1")
    2, 3 -> print("x is 2 or 3")
    in 4..10 -> print("x is between 4 and 10")
    else -> print("x is something else")
}

// For loop
for (i in 1..10) {
    println(i)
}

// While loop
while (condition) {
    // code
}</code></pre>
    
    <h3>Kotlin for Android: Practical Examples</h3>
    
    <h4>Activity Declaration</h4>
    <pre><code>class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // Find view by ID
        val textView = findViewById<TextView>(R.id.textView)
        textView.text = "Hello, Kotlin!"
        
        // Set click listener
        val button = findViewById<Button>(R.id.button)
        button.setOnClickListener {
            // Handle click event
            textView.text = "Button clicked!"
        }
    }
}</code></pre>
    
    <h4>Data Classes</h4>
    <p>Data classes automatically generate equals(), hashCode(), toString(), and copy() methods:</p>
    <pre><code>data class User(
    val id: String,
    val name: String,
    val email: String
)</code></pre>
    
    <h4>Extension Functions</h4>
    <pre><code>// Add a new function to the View class
fun View.hide() {
    this.visibility = View.GONE
}

// Usage
button.hide()</code></pre>
    
    <h3>Coroutines for Asynchronous Programming</h3>
    <p>Coroutines simplify asynchronous operations in Android:</p>
    <pre><code>// Launch a coroutine in a ViewModel
viewModelScope.launch {
    // Perform network request on IO dispatcher
    val result = withContext(Dispatchers.IO) {
        api.fetchData()
    }
    
    // Update UI with result
    _uiState.value = result
}</code></pre>
    
    <h3>Kotlin Android Extensions</h3>
    <p>Kotlin Android Extensions (now replaced by ViewBinding) allowed direct reference to views:</p>
    <pre><code>// Old way with Kotlin Android Extensions
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // Direct reference to views
        textView.text = "Hello, Kotlin!"
        button.setOnClickListener {
            textView.text = "Button clicked!"
        }
    }
}</code></pre>
    
    <h3>Modern Approach: ViewBinding</h3>
    <pre><code>// Modern approach with ViewBinding
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        // Access views through binding
        binding.textView.text = "Hello, Kotlin!"
        binding.button.setOnClickListener {
            binding.textView.text = "Button clicked!"
        }
    }
}</code></pre>
    
    <h3>Key Resources for This Lesson</h3>
    <ul>
        <li><a href="https://kotlinlang.org/docs/home.html" target="_blank">Official Kotlin Documentation</a></li>
        <li><a href="https://developer.android.com/kotlin" target="_blank">Android Kotlin Documentation</a></li>
        <li><a href="https://play.kotlinlang.org/" target="_blank">Kotlin Playground</a> - Try Kotlin online</li>
    </ul>
    
    <h3>Practice Exercises</h3>
    <ol>
        <li>Create a Kotlin data class to represent a Contact with properties for name, phone, and email.</li>
        <li>Write an extension function for the String class that checks if the string is a valid email address.</li>
        <li>Implement a function that uses coroutines to simulate a network request with a delay.</li>
    </ol>
    """
    kotlin_lesson.save()
    print(f"Enhanced content for lesson: {kotlin_lesson.title}")

if __name__ == '__main__':
    enhance_course_content()
    print("Course content has been enhanced with detailed information, book recommendations, and rich text content!") 