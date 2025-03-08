# Learning Website

A comprehensive learning platform built with Django and Tailwind CSS, similar to "Greek for Greeks". This website allows users to browse courses, track their progress, and take quizzes to test their knowledge.

## Features

- **User Authentication**: Login, logout, and user registration
- **Course Management**: Browse, filter, and search for courses
- **Learning Content**: Structured lessons with text and video content
- **Progress Tracking**: Track completed lessons and course progress
- **Interactive Quizzes**: Test knowledge with quizzes for each lesson
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Database**: SQLite (development), PostgreSQL (production)
- **Media Storage**: Local storage (development), AWS S3 (production)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/learning-website.git
   cd learning-website
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the website at http://127.0.0.1:8000/

## Project Structure

- `learning_website/`: Main project settings
- `learning_content/`: App for courses, lessons, and quizzes
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)
- `media/`: User-uploaded files

## Admin Interface

The admin interface is available at http://127.0.0.1:8000/admin/ and allows you to:

- Create and manage categories
- Create and manage courses and lessons
- Create quizzes and questions
- View user progress

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django documentation
- Tailwind CSS documentation
- "Greek for Greeks" for inspiration 