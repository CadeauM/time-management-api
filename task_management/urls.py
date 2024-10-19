from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Include your app's URLs
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redirect root to /api/
]

