from django.urls import path
from .views import *

urlpatterns = [
    path('', AlumniListView.as_view(), name='alumni_list'),
    path('add/', AlumniAddView.as_view(), name='alumni_add'),
    path('filter/', AlumniFilterView, name='alumni_filter'),
]
