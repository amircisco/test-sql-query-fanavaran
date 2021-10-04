from django.shortcuts import render
from .models import Student, Teacher, Term, Course, Enrollment
from django.db.models import Exists, Q, F, Avg,Max, Sum, Count


class Common:
    @staticmethod
    def rnd(request, qs):
        return render(request, 'school/show_loop.html', context={'objects': qs, 'query': qs.query})


def q1(request):
    #qs = Student.objects.exclude(id__in=Enrollment.objects.values_list("student", flat=True))
    qs = Student.objects.filter(enrollment__isnull=True)
    return Common.rnd(request, qs)


def q2(request):
    qs1 = Enrollment.objects.filter(grade__isnull=False).distinct("student").values_list("student", flat=True)
    qs = Enrollment.objects.filter(grade__isnull=True).exclude(student_id__in=qs1).select_related("student").distinct("student").values_list("student__name")
    return Common.rnd(request, qs)


def q3(request):
    qs1 = Enrollment.objects.exclude(grade__range=(12,18)).distinct("student").values_list("student",flat=True)
    qs = Enrollment.objects.filter(grade__range=(12,18)).distinct("student").exclude(student_id__in=qs1).select_related("student")
    return Common.rnd(request, qs)


def q4(request):
    qs1 = Enrollment.objects.filter(grade__lt=15).distinct("student").values_list("student", flat=True)
    qs = Enrollment.objects.filter(grade__gte=15).distinct("student").exclude(student_id__in=qs1).select_related("student").values_list("student__name", flat=True)
    # qs = Enrollment.objects.filter(Q(grade__gte=15),~Q(student_id__in=qs1)).distinct("student").select_related("student").values_list("student__name", flat=True)
    return Common.rnd(request, qs)


def q5(request):
    qs = Course.objects.filter(enrollment__isnull=True).values_list("teacher__name", flat=True)
    return Common.rnd(request, qs)


def q6(request):
    qs1 = Enrollment.objects.filter(grade__isnull=False).distinct("course_id").values_list("course_id",flat=True)
    # qs = Enrollment.objects.filter(grade__isnull=True).distinct("course_id").exclude(course_id__in=qs1).select_related("course").values_list("course__teacher__name", flat=True)
    qs = Enrollment.objects.filter(Q(grade__isnull=True), ~Q(course_id__in=qs1)).distinct("course_id").select_related("course").values_list("course__teacher__name", flat=True)
    return Common.rnd(request, qs)


def q7(request):
    qs1 = Enrollment.objects.filter(grade__lt=10).distinct("course_id").values_list("course_id", flat=True)
    qs = Enrollment.objects.filter(grade__gte=10).exclude(course_id__in=qs1).distinct("course_id").select_related("course").values_list("course__teacher__name",flat=True)
    return Common.rnd(request, qs)


def q8(request):
    qs = Enrollment.objects.values('course__id','course__teacher__name').annotate(average=Avg('grade'))
    return Common.rnd(request, qs)


def q9(request):
    qs = Enrollment.objects.filter(course_id=1).values("course","course__term__start_date","course__term__end_date").annotate(average=Avg("grade"))
    return Common.rnd(request, qs)


def q10(request):
    qs = Enrollment.objects.order_by('-grade').values("student__name","course__name","grade")
    return Common.rnd(request, qs)


def q11(request):
    qs = Enrollment.objects.order_by('-grade').filter(student__name__startswith="a").values("student__name","course__name","grade")
    return Common.rnd(request, qs)


def q12(request):
    # qs = Enrollment.objects.select_related("course").values("course__teacher_id")
    qs = Enrollment.objects.values("course_id").annotate(Count('id')).filter(id__count__gt=1)
    return Common.rnd(request, qs)