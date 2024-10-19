from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),  # admin panel
    path('api/', include('tasks.urls')),  #include task app's url under '/api/'
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redirect root to /api/
]

