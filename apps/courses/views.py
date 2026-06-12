from django.shortcuts import render

from .models import Course

def home(request):
    courses = Course.objects.filter(status="Aproved").order_by('-created_at')
    return render(request, 'courses/home.html', {"courses": courses})