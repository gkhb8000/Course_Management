# courses/views.py

from django.shortcuts import render
from .models import Student, Course, Income, Expense

def 学生管理(request):
    学生 = Student.objects.all()
    return render(request, 'courses/学生管理.html', {'学生': 学生})

def 课程管理(request):
    所有课程 = Course.objects.all()
    return render(request, 'courses/课程管理.html', {'课程': 所有课程})

def 收入管理(request):
    收入 = Income.objects.all()
    return render(request, 'courses/收入管理.html', {'收入': 收入})

def 费用管理(request):
    费用 = Expense.objects.all()
    return render(request, 'courses/费用管理.html', {'费用': 费用})

def 课程列表(request):
    课程 = Course.objects.all()
    return render(request, 'courses/课程列表.html', {'课程': 课程})