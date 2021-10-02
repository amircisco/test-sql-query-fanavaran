from django.db import models
from django.utils import timezone


class CommonDb(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Student(CommonDb):

    class Meta:
        verbose_name = "دانش آموز"
        verbose_name_plural = "دانش آموزان"


class Teacher(CommonDb):

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "اساتید"


class Term(models.Model):
    start_date = models.DateField(default=timezone.now, verbose_name="تاریخ شروع")
    end_date = models.DateField(default=timezone.now, verbose_name="تاریخ پایان")

    def __str__(self):
        return "from {} to {}".format(self.start_date, self.end_date)

    class Meta:
        verbose_name = "ترم"
        verbose_name_plural = "ترم ها"


class Course(CommonDb):
    term = models.ForeignKey(Term, on_delete=models.DO_NOTHING, verbose_name="ترم")
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, verbose_name="معلم")
    capacity = models.IntegerField(verbose_name="ظرفیت")

    def __str__(self):
        return "{} by {} with {} capacity".format(self.name, self.teacher.name, self.capacity)

    class Meta:
        verbose_name = "درس"
        verbose_name_plural = "درس ها"


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name="درس")
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, verbose_name="دانش آموز")
    grade = models.FloatField(verbose_name="نمره", blank=True, default=-1)

    def __str__(self):
        return "{} in course {}  take {}".format(self.student.name, self.course.name, self.grade )

    class Meta:
        verbose_name = "ثبت نام"
        verbose_name_plural = "ثبت نام ها"


Student._meta.get_field('name').verbose_name = "نام دانش آموز"
Teacher._meta.get_field('name').verbose_name = "نام استاد"
Course._meta.get_field("name").verbose_name = "نام درس"