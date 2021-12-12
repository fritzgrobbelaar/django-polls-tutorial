from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import BlogPost


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('publisher_name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 5
    list_max_show_all = 1000
#    fieldsets = [
#        (None, {'fields':['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]
  #  fields = ['pub_date','question_text']

admin.site.register(BlogPost)
#admin.site.register(Choice)