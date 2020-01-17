from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.indexPage),
    path('verify', views.verifyPage),
]
