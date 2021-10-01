from django.contrib import admin
from .models import Student, Teacher, Term, Course, Enrollment


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Term)
admin.site.register(Course)
admin.site.register(Enrollment)
