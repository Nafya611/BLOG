from django.contrib import admin
#from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Ensure 'users.urls' is included
]
