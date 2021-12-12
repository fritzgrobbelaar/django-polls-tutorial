from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 5
    list_max_show_all = 1000
#    fieldsets = [
#        (None, {'fields':['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]
    inlines = [ChoiceInline]
  #  fields = ['pub_date','question_text']

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)