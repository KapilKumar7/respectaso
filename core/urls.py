from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse # Required for the ping response

# This tiny function tells the "ping" service that the app is alive
def ping(request):
    return HttpResponse("OK", content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Add this line for the heartbeat
    path('ping/', ping), 
    
    # 2. Your existing app routes
    path('', include('aso.urls')), 
]
