from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Storefront Home Page!")

urlpatterns = [
    path('', home),  # ✅ root URL
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('__debug__/', include('debug_toolbar.urls')),  # ✅ correct
]
