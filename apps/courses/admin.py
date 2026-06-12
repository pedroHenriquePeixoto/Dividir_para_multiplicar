from django.contrib import admin
from .models import Course
from .models import Category
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name' , 'description', 'url',)
    list_filter = ('status', 'category',)
    search_fields = ('name', 'description',)



admin.site.register(Category)

