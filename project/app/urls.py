from django.urls import path, re_path
from .views import index

urlpatterns = [
    re_path(r'^user/(?P<name>\D+)/(?P<age>d+)', index),
    path('user/<str:name>/<int:age>/', index, name='home'),
    path('user/<str:name', index, name='home'),
    path('user', index, name='home')
]
