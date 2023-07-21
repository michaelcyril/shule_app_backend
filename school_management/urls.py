from django.urls import path
from .views import *

app_name = 'school_management'

urlpatterns = [
    path('school', SchoolView.as_view()),
    path('event', EventView.as_view()),
    path('user-school', UserSchoolView.as_view()),
    path('application', ApplicationView.as_view()),
    path('document', DocumentView.as_view()),
]