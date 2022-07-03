from django.contrib import admin
from django.urls import path, include
from .views import TesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('', TesView.as_view(), name='test'),
]
