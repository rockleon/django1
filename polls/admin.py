from django.contrib import admin

from .models import Choice, Question, User


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class UserAdmin(admin.ModelAdmin):
    # model = User
    fieldsets = [
        ('Username', {'fields': ['username']}),
        ('Password', {'fields': ['password']}),
    ]
    list_display = ('username', 'password')
    search_fields = ['username']

admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)