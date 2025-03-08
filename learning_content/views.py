from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.db.models import Count, Q
from .models import Category, Course, Lesson, Quiz, Question, Answer, UserProgress, UserQuizAttempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def home(request):
    """Home page view with featured courses and categories"""
    featured_courses = Course.objects.filter(is_featured=True, is_published=True)[:6]
    categories = Category.objects.annotate(course_count=Count('courses')).order_by('-course_count')[:6]
    
    context = {
        'featured_courses': featured_courses,
        'categories': categories,
    }
    return render(request, 'learning_content/home.html', context)

def about(request):
    """About page view"""
    return render(request, 'learning_content/about.html')

def course_list(request):
    """View for listing all courses with filtering options"""
    courses = Course.objects.filter(is_published=True)
    categories = Category.objects.all()
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        courses = courses.filter(category__slug=category_slug)
    
    # Filter by level
    level = request.GET.get('level')
    if level:
        courses = courses.filter(level=level)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        courses = courses.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    
    context = {
        'courses': courses,
        'categories': categories,
        'selected_category': category_slug,
        'selected_level': level,
        'query': query,
    }
    return render(request, 'learning_content/course_list.html', context)

def course_detail(request, slug):
    """View for course details and lessons"""
    course = get_object_or_404(Course, slug=slug, is_published=True)
    lessons = course.lessons.filter(is_published=True).order_by('order')
    
    # Get key points for the course
    key_points = course.keypoints.all().order_by('title')
    
    # Get user progress if logged in
    user_progress = None
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(
            user=request.user,
            course=course,
            completed=True
        ).values_list('lesson_id', flat=True)
    
    context = {
        'course': course,
        'lessons': lessons,
        'key_points': key_points,
        'user_progress': user_progress,
    }
    return render(request, 'learning_content/course_detail.html', context)

@login_required
def lesson_detail(request, course_slug, lesson_slug):
    """View for lesson details"""
    course = get_object_or_404(Course, slug=course_slug, is_published=True)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course, is_published=True)
    
    # Get next and previous lessons
    next_lesson = Lesson.objects.filter(
        course=course, 
        is_published=True, 
        order__gt=lesson.order
    ).order_by('order').first()
    
    prev_lesson = Lesson.objects.filter(
        course=course, 
        is_published=True, 
        order__lt=lesson.order
    ).order_by('-order').first()
    
    # Mark lesson as completed if not already
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        course=course,
        lesson=lesson,
        defaults={'completed': True, 'completed_at': timezone.now()}
    )
    
    if not progress.completed:
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()
    
    # Check if lesson has a quiz
    has_quiz = hasattr(lesson, 'quiz')
    
    # Get user progress for all lessons in this course
    user_progress = None
    completed_lessons = []
    completed_percentage = 0
    
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(
            user=request.user,
            course=course
        )
        completed_lessons = user_progress.filter(completed=True).values_list('lesson_id', flat=True)
        
        # Calculate completion percentage
        total_lessons = course.lessons.filter(is_published=True).count()
        if total_lessons > 0:
            completed_percentage = int((len(completed_lessons) / total_lessons) * 100)
    
    context = {
        'course': course,
        'lesson': lesson,
        'next_lesson': next_lesson,
        'prev_lesson': prev_lesson,
        'has_quiz': has_quiz,
        'user_progress': user_progress,
        'completed_lessons': completed_lessons,
        'completed_percentage': completed_percentage,
    }
    return render(request, 'learning_content/lesson_detail.html', context)

@login_required
def take_quiz(request, course_slug, lesson_slug):
    """View for taking a quiz"""
    course = get_object_or_404(Course, slug=course_slug, is_published=True)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course, is_published=True)
    quiz = get_object_or_404(Quiz, lesson=lesson)
    questions = quiz.questions.all()
    
    # Check if user has already completed this quiz
    quiz_attempt = UserQuizAttempt.objects.filter(user=request.user, quiz=quiz, completed=True).first()
    
    if quiz_attempt:
        messages.info(request, f"You've already completed this quiz with a score of {quiz_attempt.score}%")
        return redirect('learning_content:lesson_detail', course_slug=course_slug, lesson_slug=lesson_slug)
    
    # Get user progress for all lessons in this course
    user_progress = None
    completed_lessons = []
    completed_percentage = 0
    
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(
            user=request.user,
            course=course
        )
        completed_lessons = user_progress.filter(completed=True).values_list('lesson_id', flat=True)
        
        # Calculate completion percentage
        total_lessons = course.lessons.filter(is_published=True).count()
        if total_lessons > 0:
            completed_percentage = int((len(completed_lessons) / total_lessons) * 100)
    
    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        
        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
        
        # Calculate percentage score
        percentage_score = int((score / total_questions) * 100) if total_questions > 0 else 0
        
        # Save quiz attempt
        quiz_attempt = UserQuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=percentage_score,
            completed=True
        )
        
        messages.success(request, f"Quiz completed! Your score: {percentage_score}%")
        return redirect('learning_content:lesson_detail', course_slug=course_slug, lesson_slug=lesson_slug)
    
    context = {
        'course': course,
        'lesson': lesson,
        'quiz': quiz,
        'questions': questions,
        'user_progress': user_progress,
        'completed_lessons': completed_lessons,
        'completed_percentage': completed_percentage,
    }
    return render(request, 'learning_content/take_quiz.html', context)

@login_required
def dashboard(request):
    """User dashboard view showing progress and courses"""
    user_courses = Course.objects.filter(
        lessons__userprogress__user=request.user
    ).distinct()
    
    courses_progress = []
    
    for course in user_courses:
        total_lessons = course.lessons.filter(is_published=True).count()
        completed_lessons = UserProgress.objects.filter(
            user=request.user,
            course=course,
            completed=True
        ).count()
        
        progress_percentage = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0
        
        courses_progress.append({
            'course': course,
            'progress': progress_percentage,
            'completed_lessons': completed_lessons,
            'total_lessons': total_lessons,
        })
    
    context = {
        'courses_progress': courses_progress,
    }
    return render(request, 'learning_content/dashboard.html', context)

def category_detail(request, slug):
    """View for category details and its courses"""
    category = get_object_or_404(Category, slug=slug)
    courses = Course.objects.filter(category=category, is_published=True)
    
    context = {
        'category': category,
        'courses': courses,
    }
    return render(request, 'learning_content/category_detail.html', context)

def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome, {user.first_name}! Your account has been created successfully.")
            return redirect('learning_content:home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'learning_content/register.html', {'form': form})
