from django.urls import path, re_path

from .views import get_menu

urlpatterns = [
    path('', get_menu),
    re_path(r'(\w+)', get_menu, name='main'),
]
