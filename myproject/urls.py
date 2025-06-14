from django.contrib import admin
from django.urls import path
from mainapp.views import show_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_data),
]
