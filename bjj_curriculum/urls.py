from django.contrib import admin
from django.urls import path, include
from belts.views import day1_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', day1_view, name='home'),  # default route -> Day 1
    path('belts/', include('belts.urls')),
]
