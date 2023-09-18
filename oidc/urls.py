from django.contrib import admin
from django.urls import path, include

from oidc import views

urlpatterns = [
    path("", views.home, name='home'),
    path('admin/', admin.site.urls),
    path("", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("api/", include("api.urls"))
]
