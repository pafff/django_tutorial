from django.contrib import admin

from .models import Choice, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['text']

admin.site.site_header = 'Polls administration'
admin.site.register(Question, QuestionAdmin)
