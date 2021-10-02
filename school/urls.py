from django.urls import path
from .views import (
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12
)

app_name = "school"
urlpatterns = [
    path('q1/', q1, name="q1/"),
    path('q2/', q2, name="q2/"),
    path('q3/', q3, name="q3/"),
    path('q4/', q4, name="q4/"),
    path('q5/', q5, name="q5/"),
    path('q6/', q6, name="q6/"),
    path('q7/', q7, name="q7/"),
    path('q8/', q8, name="q8/"),
    path('q9/', q9, name="q9/"),
    path('q10/', q10, name="q10/"),
    path('q11/', q11, name="q11/"),
    path('q12/', q12, name="q12/"),
    # path('q13/', q13, name="q13/"),
    # path('q14/', q14, name="q14/"),
    # path('q15/', q15, name="q15/"),
    # path('q16/', q16, name="q16/"),
    # path('q17/', q17, name="q17/"),
    # path('q18/', q18, name="q18/"),
    # path('q19/', q19, name="q19/"),
    # path('q20/', q20, name="q20/"),
    # path('q21/', q21, name="q21/"),
    # path('q22/', q22, name="q22/"),

]