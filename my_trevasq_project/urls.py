from django.contrib import admin
from django.urls import path
from  quamtum_computing.views import index  # Import your view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Route for the index view
]
