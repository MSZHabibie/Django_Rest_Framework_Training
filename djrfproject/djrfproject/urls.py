from django.contrib import admin
from django.urls import path, include
from .views import TesView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('', TesView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain')
]
