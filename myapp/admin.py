from django.contrib import admin
#import my models
from .models import Question, Choice
from .models import  Book

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Book)