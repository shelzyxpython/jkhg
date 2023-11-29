from django.urls import path, re_path
from .views import index, error, user

urlpatterns = [
    re_path(r'^user/(?P<username>\w+)/(?P<folder>\w+)/(?P<post_id>\d+)/$', user),
    path('error/', error),
    path('', index, name='home')
]




