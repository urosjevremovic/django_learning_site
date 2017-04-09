from django.shortcuts import render, get_object_or_404

from . import models


def course_list(request):
    courses = models.Course.objects.all()
    email = 'urosh43@gmail.com'
    return render(request, 'courses/course_list.html', {'courses': courses, 'email': email})
    # context dictionary


def course_detail(request, pk):
    # course = models.Course.objects.get(pk=pk)
    course = get_object_or_404(models.Course, pk=pk)
    # pk is ID by default
    # request comes in automatically and pk needs to be provided
    return render(request, 'courses/course_detail.html', {'course': course})


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Step, course_id = course_pk, pk = step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

