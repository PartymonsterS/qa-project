from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at", "updated_at")
    search_fields = ("title", "body", "author__username")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "author", "is_accepted", "created_at", "updated_at")
    search_fields = ("body", "author__username", "question__title")
    list_filter = ("is_accepted", "created_at")
    ordering = ("-created_at",)