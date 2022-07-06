from django.contrib import admin

from django.contrib import admin
from . import models

@admin.register(models.Group)

class GroupAdmin(admin.ModelAdmin):
	list_display = [
        'name',
        ]

@admin.register(models.Subject)

class SubjectAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text', 
        'is_right'
        ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subject',
        ]
    list_display = [
        'title', 
        'subject',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_right', 
        'question'
        ]
