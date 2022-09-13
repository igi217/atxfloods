from . import views
from django.urls import path

urlpatterns = [
    path('crossings', views.crossings, name='api.crossings'),
    path('cameras', views.cameras, name='api.closures'),
    path('closures', views.closures, name='api.closures')
]