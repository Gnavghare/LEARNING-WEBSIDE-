from django.contrib import admin
from .models import Category, Course, Lesson, Quiz, Question, Answer, UserProgress, UserQuizAttempt, Resource

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    prepopulated_fields = {'slug': ('title',)}

class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1
    fields = ('title', 'resource_type', 'file', 'url', 'description')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'is_published', 'is_featured', 'created_at')
    list_filter = ('category', 'level', 'is_published', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    inlines = [LessonInline, ResourceInline]

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3
    inlines = [AnswerInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'is_published', 'created_at')
    list_filter = ('course', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    inlines = [ResourceInline]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    list_filter = ('quiz',)
    search_fields = ('text',)
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text',)

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'lesson', 'completed', 'completed_at')
    list_filter = ('completed', 'course')
    search_fields = ('user__username', 'course__title', 'lesson__title')

@admin.register(UserQuizAttempt)
class UserQuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'completed', 'created_at')
    list_filter = ('completed', 'quiz')
    search_fields = ('user__username', 'quiz__title')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'course', 'lesson', 'created_at')
    list_filter = ('resource_type', 'course', 'lesson')
    search_fields = ('title', 'description')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'resource_type')
        }),
        ('Association', {
            'fields': ('course', 'lesson')
        }),
        ('Resource', {
            'fields': ('file', 'url')
        }),
    )

# Re-register the models with updated admin classes
admin.site.unregister(Course)
admin.site.unregister(Lesson)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
