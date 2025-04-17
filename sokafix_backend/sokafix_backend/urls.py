from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "SokaFix Backend is Live!"})

urlpatterns = [
    path('', home),  # ✅ Root path
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
