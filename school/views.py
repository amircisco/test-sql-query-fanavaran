from django.shortcuts import render
from .models import Student, Teacher, Term, Course, Enrollment
from django.db.models import Exists, Q, F, Avg,Max


class Common:
    @staticmethod
    def rnd(request, qs):
        return render(request, 'school/show_loop.html', context={'objects': qs, 'query': qs.query})


def q1(request):
    qs = Student.objects.exclude(id__in=Enrollment.objects.values_list("student", flat=True))
    return Common.rnd(request, qs)


def q2(request):
    qs = Student.objects.filter(enrollment__isnull=True)
    return Common.rnd(request, qs)


def q3(request):
    qs1 = Enrollment.objects.filter(grade__range=(12,18)).distinct("student").values_list("student",flat=True)
    qs2 = Enrollment.objects.exclude(grade__range=(12,18)).distinct("student").values_list("student",flat=True)
    #qs = Student.objects.filter(id__in=qs1).exclude(id__in=qs2)
    qs = Student.objects.filter(Q(id__in=qs1),~Q(id__in=qs2))
    return Common.rnd(request, qs)


def q4(request):
    qs1 = Enrollment.objects.filter(grade__gte=15).distinct("student").values_list("student", flat=True)
    qs2 = Enrollment.objects.filter(grade__lt=15).distinct("student").values_list("student", flat=True)
    # qs = Student.objects.filter(id__in=qs1).exclude(id__in=qs2)
    qs = Student.objects.filter(Q(id__in=qs1),~Q(id__in=qs2))
    return Common.rnd(request, qs)


def q5(request):
    qs = Course.objects.filter(enrollment__isnull=True).values_list("teacher__name", flat=True)
    return Common.rnd(request, qs)


def q6(request):
    qs1 = Enrollment.objects.filter(grade__isnull=True).distinct("course__teacher_id").values_list("course__teacher_id",flat=True)
    qs2 = Enrollment.objects.filter(grade__isnull=False).distinct("course__teacher_id").values_list("course__teacher_id",flat=True)
    qs = Teacher.objects.filter(id__in=qs1).exclude(id__in=qs2)
    return Common.rnd(request, qs)


def q7(request):
    qs1 = Enrollment.objects.filter(grade__gte=10).distinct("course__teacher_id").values_list("course__teacher_id", flat=True)
    qs2 = Enrollment.objects.filter(grade__lt=10).distinct("course__teacher_id").values_list("course__teacher_id", flat=True)
    qs = Teacher.objects.filter(id__in=qs1).exclude(id__in=qs2)
    return Common.rnd(request, qs)


def q8(request):
    qs = Enrollment.objects.values('course__id','course__teacher__name').annotate(average=Avg('grade'))
    return Common.rnd(request, qs)
