import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from learning_content.models import Course, Lesson, Resource

def add_resources():
    # Add resources to Python for Beginners course
    python_course = Course.objects.get(title='Python for Beginners')
    
    # Course-level resources
    Resource.objects.create(
        title="Python Cheat Sheet",
        description="A comprehensive cheat sheet covering Python syntax and common operations.",
        resource_type="pdf",
        url="https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf",
        course=python_course
    )
    
    Resource.objects.create(
        title="Python Official Documentation",
        description="The official Python documentation is an excellent reference for all Python features.",
        resource_type="link",
        url="https://docs.python.org/3/",
        course=python_course
    )
    
    Resource.objects.create(
        title="Python Practice Exercises",
        description="A collection of 100 practice exercises to reinforce your Python skills.",
        resource_type="exercise",
        url="https://www.w3resource.com/python-exercises/",
        course=python_course
    )
    
    # Lesson-level resources
    intro_lesson = Lesson.objects.get(title='Introduction to Python', course=python_course)
    
    Resource.objects.create(
        title="Getting Started with Python",
        description="A guide to installing Python and setting up your development environment.",
        resource_type="pdf",
        url="https://realpython.com/python-first-steps/",
        lesson=intro_lesson
    )
    
    Resource.objects.create(
        title="Hello World Example",
        description="A simple Python script demonstrating the classic 'Hello, World!' program.",
        resource_type="code",
        url="https://github.com/python/cpython/blob/main/Lib/test/hello.py",
        lesson=intro_lesson
    )
    
    # Add resources to JavaScript Essentials course
    js_course = Course.objects.get(title='JavaScript Essentials')
    
    Resource.objects.create(
        title="JavaScript Cheat Sheet",
        description="A quick reference guide for JavaScript syntax and methods.",
        resource_type="pdf",
        url="https://htmlcheatsheet.com/js/",
        course=js_course
    )
    
    Resource.objects.create(
        title="MDN JavaScript Guide",
        description="Mozilla Developer Network's comprehensive JavaScript guide.",
        resource_type="link",
        url="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
        course=js_course
    )
    
    # Add resources to Deep Learning Fundamentals course
    dl_course = Course.objects.get(title='Deep Learning Fundamentals')
    
    Resource.objects.create(
        title="Neural Networks and Deep Learning",
        description="An online book by Michael Nielsen explaining neural networks and deep learning.",
        resource_type="link",
        url="http://neuralnetworksanddeeplearning.com/",
        course=dl_course
    )
    
    Resource.objects.create(
        title="TensorFlow Playground",
        description="An interactive visualization of neural networks, written in JavaScript.",
        resource_type="link",
        url="https://playground.tensorflow.org/",
        course=dl_course
    )
    
    nn_lesson = Lesson.objects.get(title='Neural Network Basics', course=dl_course)
    
    Resource.objects.create(
        title="Simple Neural Network Implementation",
        description="A Python implementation of a basic neural network using NumPy.",
        resource_type="code",
        url="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/mnist/mnist_softmax.py",
        lesson=nn_lesson
    )
    
    # Add resources to HTML & CSS Fundamentals course
    html_course = Course.objects.get(title='HTML & CSS Fundamentals')
    
    Resource.objects.create(
        title="HTML5 Cheat Sheet",
        description="A comprehensive reference for HTML5 elements and attributes.",
        resource_type="pdf",
        url="https://htmlcheatsheet.com/",
        course=html_course
    )
    
    Resource.objects.create(
        title="CSS Tricks",
        description="A website dedicated to teaching people how to use CSS.",
        resource_type="link",
        url="https://css-tricks.com/",
        course=html_course
    )
    
    # Add resources to Android Development with Kotlin course
    android_course = Course.objects.get(title='Android Development with Kotlin')
    
    Resource.objects.create(
        title="Kotlin Language Reference",
        description="The official Kotlin language reference documentation.",
        resource_type="link",
        url="https://kotlinlang.org/docs/reference/",
        course=android_course
    )
    
    Resource.objects.create(
        title="Android Developer Guides",
        description="Official Android developer documentation and guides.",
        resource_type="link",
        url="https://developer.android.com/guide",
        course=android_course
    )
    
    kotlin_lesson = Lesson.objects.get(title='Kotlin for Android', course=android_course)
    
    Resource.objects.create(
        title="Kotlin Koans",
        description="A series of exercises to get familiar with Kotlin syntax and features.",
        resource_type="exercise",
        url="https://play.kotlinlang.org/koans/",
        lesson=kotlin_lesson
    )
    
    print("Resources have been added successfully!")

if __name__ == '__main__':
    add_resources() 