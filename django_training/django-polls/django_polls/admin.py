from django.contrib import admin
from .models import Question
from .models import Choice

# admin details in manager readme
# Register your models here.
# admin.site.register(Question)



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_text"]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"] #automatically goes to the list display admin page
    list_filter = ["pub_date"] #Auto checks the field type and makes the filter fit. In this case it is date so makes date filters.
    search_fields = ["question_text"]
    list_per_page = 2
    # Lots of other admin site options:
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page
    
admin.site.register(Question,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["choice_text"]}),
        ("Information",{"fields":["question", "votes"]})
    ]
# admin.site.register(Choice,ChoiceAdmin)