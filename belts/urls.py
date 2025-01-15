from django.urls import path
from . import views

urlpatterns = [
    path('belts/', views.belt_list, name='belt_list'),
    path('belts/<int:belt_id>/techniques/', views.technique_list, name='technique_list'),
    path('day1/', views.day1_view, name='day1_white'),
]
