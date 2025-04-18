from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.utils.timezone import now

def home(request):
    return JsonResponse({
        "status": "success",
        "message": "Welcome to SokaFix Backend!",
        "timestamp": now().isoformat(),
        "routes": {
            "admin": "/admin/",
            "contact_api": "/api/contact/",
            "newsletter_api": "/api/subscribe/"
        }
    })

urlpatterns = [
    path('', home),  # ✅ Root path for status check
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
