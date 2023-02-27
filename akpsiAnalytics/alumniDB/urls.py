from django.urls import path
from .views import AlumniListView, AlumniFilterView, AlumniAddView

urlpatterns = [
    path('', AlumniListView.as_view(), name='alumni_list'),
    path('filter/<str:sphere>/', AlumniFilterView.as_view(), name='alumni_filter'),
    path('add/', AlumniAddView.as_view(), name='alumni_add'),
]
