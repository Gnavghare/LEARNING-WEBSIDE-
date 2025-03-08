import os
import django

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings')
django.setup()

from learning_content.models import Course, KeyPoint, Lesson
from django.utils.text import slugify

# Get the course by ID
course = Course.objects.get(id=12)  # Algorithms and Data Structures course
print(f"Integrating key point content into lessons for course: {course.title}")

# Get all key points for this course
keypoints = KeyPoint.objects.filter(course=course)
print(f"Found {len(keypoints)} key points for this course")

# Update each lesson with the corresponding key point content
for keypoint in keypoints:
    try:
        # Find the lesson for this key point
        lesson_slug = slugify(keypoint.title)
        try:
            lesson = Lesson.objects.get(course=course, slug=lesson_slug)
            print(f"Updating lesson content for: {lesson.title}")
            
            # Create comprehensive content that includes all key point information
            content = f"""# {keypoint.title}

{keypoint.description}

## Code Examples

{keypoint.example if keypoint.example else 'No code examples available.'}

## Time Complexity

{keypoint.time_complexity if keypoint.time_complexity else 'Time complexity information not available.'}

## Space Complexity

{keypoint.space_complexity if keypoint.space_complexity else 'Space complexity information not available.'}

## Applications

{keypoint.applications if keypoint.applications else 'Application information not available.'}

## Quiz

To test your understanding of {keypoint.title}, please complete the quiz at the end of this lesson.
"""
            
            # Update the lesson content
            lesson.content = content
            lesson.save()
            print(f"Successfully updated lesson content for: {lesson.title}")
            
        except Lesson.DoesNotExist:
            print(f"No lesson found for key point: {keypoint.title}")
            
    except Exception as e:
        print(f"Error updating lesson for key point {keypoint.title}: {str(e)}")

# Update the overview lesson to include links to all topics
try:
    overview_lesson = Lesson.objects.get(course=course, slug='algorithms-and-data-structures-overview')
    
    # Create a table of contents with links to all topics
    toc = "## Table of Contents\n\n"
    for i, keypoint in enumerate(keypoints.order_by('title')):
        lesson_slug = slugify(keypoint.title)
        toc += f"{i+1}. [{keypoint.title}](/learning/lesson/{lesson_slug})\n"
    
    # Create comprehensive overview content
    overview_content = f"""# Algorithms and Data Structures

This course provides a comprehensive introduction to fundamental data structures and algorithms. Understanding these concepts is essential for writing efficient code and solving complex computational problems.

{toc}

## Course Overview

In this course, you will learn about various data structures such as arrays, linked lists, stacks, queues, trees, graphs, and hash tables. For each data structure, you will understand:

- Basic concepts and implementation
- Time and space complexity analysis
- Common operations and their efficiency
- Real-world applications
- Practical code examples

Each topic includes detailed explanations, code examples, complexity analysis, and interactive quizzes to test your understanding.

## Prerequisites

- Basic programming knowledge in any language
- Understanding of basic mathematical concepts
- Familiarity with basic problem-solving techniques

## Learning Objectives

By the end of this course, you will be able to:

1. Understand the characteristics and operations of common data structures
2. Analyze the time and space complexity of algorithms
3. Choose appropriate data structures for specific problems
4. Implement basic data structures and algorithms
5. Apply data structures and algorithms to solve real-world problems

Let's begin our journey into the world of algorithms and data structures!
"""
    
    # Update the overview lesson content
    overview_lesson.content = overview_content
    overview_lesson.save()
    print("Successfully updated overview lesson content")
    
except Lesson.DoesNotExist:
    print("Overview lesson not found")
except Exception as e:
    print(f"Error updating overview lesson: {str(e)}")

print("Key point content has been integrated into lessons for the 'Algorithms and Data Structures' course.") 