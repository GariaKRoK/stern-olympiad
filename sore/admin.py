from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone_number',
                    'class_number', 'name_school',
                    'count', 'paid', )
    list_filter = ('class_number', )
    search_fields = ('user', 'name_school')

class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'answer', 'question', )
    search_fields = ('student', 'answer', 'question')
    
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'correct', )
    search_fields = ('text', )
    list_editable = ('text', 'correct')
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'class_number', )
    search_fields = ('question', )

admin.site.unregister(Group)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
admin.site.register(ClassNumber)
admin.site.register(Student, StudentAdmin)